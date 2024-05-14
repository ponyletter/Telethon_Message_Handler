import asyncio
import yaml
from telethon.sync import TelegramClient
from telethon.events import NewMessage
import aiofiles
from telegram_utils import worker, event_handler, send_message

async def start_telegram_client():
    # Load configuration from config.yaml
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # Create a Telegram client
    client = TelegramClient('session_name', config['api_id'], config['api_hash'])

    # Add the event handler
    client.add_event_handler(event_handler, NewMessage(pattern=None))

    # Start the client
    await client.start()

    # Run the client until it's disconnected
    await client.run_until_disconnected()

if __name__ == "__main__":
    # Start the worker function in a separate thread
    asyncio.run(start_telegram_client())
    asyncio.run(worker())
