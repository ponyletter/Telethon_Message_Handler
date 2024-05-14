# Telegram Message Handler

This is a Python script for handling incoming messages on Telegram using Telethon.

## Dependencies
- Python 3.7.6
- Telethon 1.26.0
- aiofiles 23.1.0
- asyncio 3.7.6

## Configuration
Before running the script, make sure to fill out the `config.yaml` file in the `config/` directory with your Telegram API credentials and other necessary information.

## Usage
1. Install the required dependencies using `pip install -r requirements.txt`.
2. Fill out the `config.yaml` file in the `config/` directory with your Telegram API credentials and other necessary information.
3. Run the script using `python src/main.py`.


## Mermaid

```graph TD
 graph TD
    A[Start] --> B[Start Telegram Client]
    B --> C[Add Event Handler]
    C --> D[Start Client]
    D --> E[Run Client]
    E --> F[Handle Incoming Messages]
    F --> G[Check if Message Starts with hi]
    G --> H[ Create Tasks to Send Message]
    H --> I[Limit Concurrent Operations]
    H --> J[Send Message to Chat Username 1]
    H --> K[Send Message to Chat Username 2]
    H --> L[Send Message to Chat Username ...]
    J --> M[Put Message in Queue]
    K --> M
    L --> M
    M --> N[Process Message in Worker Function]
    N --> O[Write Message to File]
    O --> P[Task Done]
    P --> Q[Repeat for Next Message]
    Q --> F
    Q -.-> R[Stop Client]
    R --> S[Stop]x 
```



