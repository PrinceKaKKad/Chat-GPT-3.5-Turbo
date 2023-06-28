import pyfiglet

# OpenAI Api key and telegram token
api_key = "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"
telegram_token = "5962841735:AAGou6LgH3wX1JTdbunvpJ2xotyHkGj_jjk"


# GPT MODEL
model = "gpt-3.5-turbo"


# LOGGING
error_log = "__log__\error.log"
conversation_log ="__log__\conversation.log"
chat_log = "__log__\chat_id.log"

project = 'Telegram Chat GPT 3.5 Turbo bot'
holder = 'Holder: Prince Kakkad'

banner1 = pyfiglet.figlet_format(project, font = "slant")
banner2 = pyfiglet.figlet_format(holder, font = "mini")