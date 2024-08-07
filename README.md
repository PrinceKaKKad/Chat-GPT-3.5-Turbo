# Telegram Chat GPT Bot 3.5 Turbo

This repository contains the code for a Telegram Chat GPT Bot 3.5 Turbo. This bot utilizes the power of OpenAI's GPT-3.5 model to provide conversational responses in real-time.

## Getting Started

To use the Telegram Chat GPT Bot, follow the steps below:

1. Obtain the API keys:
   - **Chat GPT API**: Visit [https://openai.com/](https://openai.com/) to get the API key for Chat GPT.
   - **Telegram Bot API**: Create a bot using [BotFather](https://telegram.me/BotFather) on Telegram to obtain the API token.

2. Clone the repository:
git clone https://github.com/PrinceKaKKad/Chat-GPT-3.5-Turbo.git

3. Navigate to the project directory:
   - cd Chat-GPT-3.5-Turbo-main

4. Go to `config.py` file:
- Change the following lines to the `config.py` file:
  ```python
  # Chat GPT API
  api_key = "YOUR_CHAT_GPT_API_KEY"

  # Telegram Bot API
  telegram_token = "YOUR_TELEGRAM_BOT_TOKEN"
  ```

- Replace `YOUR_CHAT_GPT_API_KEY` with your actual Chat GPT API key.
- Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual Telegram Bot API token.

5. log files:
- Log files: `chat_id.log`, `conversation.log`, and `error.log`.
- These files will store the chat IDs, conversation history, and error logs, respectively.

6. Run the bot:
- python main.py

  
## Code Map

The repository is organized as follows:

- `__log__`: Directory to store log files.
- `chat_id.log`: Stores the chat IDs of users who have communicated with the bot.
- `conversation.log`: Stores the conversation history between users and the bot.
- `error.log`: Stores any errors encountered during bot operation.

- `config.py`: Configuration file that holds the API keys.

- `main.py`: Main script that initializes and runs the Telegram Chat GPT Bot.

## License

 Author: Prince Kakkad

 Copyright 2020-2023 codeestro.com, Inc.

 Copyright reserved by codeestro.com

 Commercial use is prohibited without permission.

So that you know, commercial use of this code is strictly prohibited without permission.

If you have any questions or requests, please contact [info@codeestro.com](mailto:info@codeestro.com).
