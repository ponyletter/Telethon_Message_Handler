import asyncio
import aiofiles

# Create an asyncio Semaphore to limit concurrent operations
semaphore = asyncio.Semaphore(5)  # Example: limit concurrent operations to 5

# Create an asyncio Queue to hold incoming messages
message_queue = asyncio.Queue()

# Define the worker function to process messages
async def worker():
    while True:
        message = await message_queue.get()
        if message:
            await asyncio.to_thread(write_message_to_file, message)
            message_queue.task_done()

# Define a function to write messages to the file
async def write_message_to_file(message):
    async with aiofiles.open('messages.txt', 'a') as file:
        await file.write(message + '\n')

# Define the event handler
async def event_handler(event):
    if event.raw_text.startswith('hi'):
        async with semaphore:
            # Create tasks to send message to each chat username concurrently
            tasks = [asyncio.create_task(send_message(event.raw_text, chat_username)) for chat_username in chat_usernames]
            await asyncio.gather(*tasks)

async def send_message(message, chat_username):
    await message_queue.put((message, chat_username))
