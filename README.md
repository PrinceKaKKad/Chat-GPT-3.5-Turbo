# Telegram Chat GPT Bot 3.5 Turbo

This repository contains the code for a Telegram Chat GPT Bot 3.5 Turbo. This bot utilizes the power of OpenAI's GPT-3.5 model to provide conversational responses in real-time.

## Getting Started

To use the Telegram Chat GPT Bot, follow the steps below:

1. Obtain the API keys:
   - **Chat GPT API**: Visit [https://openai.com/](https://openai.com/) to get the API key for Chat GPT.
   - **Telegram Bot API**: Create a bot using [BotFather](https://telegram.me/BotFather) on Telegram to obtain the API token.

2. Clone the repository:
git clone https://github.com/your-username/telegram-chat-gpt-bot.git

3. Navigate to the project directory:
cd telegram-chat-gpt-bot

4. Create a `config.py` file:
- Create a new file named `config.py`.
- Add the following lines to the `config.py` file:
  ```python
  # Chat GPT API
  CHAT_GPT_API_KEY = "YOUR_CHAT_GPT_API_KEY"

  # Telegram Bot API
  TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
  ```

- Replace `YOUR_CHAT_GPT_API_KEY` with your actual Chat GPT API key.
- Replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual Telegram Bot API token.

5. Set up log files:
- Create three log files: `chat_id.log`, `conversation.log`, and `error.log`.
- These files will store the chat IDs, conversation history, and error logs, respectively.

6. Run the bot:
