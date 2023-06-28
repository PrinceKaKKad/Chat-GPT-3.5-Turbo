'''
Author: Prince Kakkad
Copyright 2020-2023 Princekakkad.tech, Inc.
Copyright reserved by princekakkad.tech

Commercial use is prohibited without permission.
'''
import time
import logging
import config
import pyfiglet
from backoff import on_exception, expo

# configure the logging module
logging.basicConfig(filename=config.error_log, level=logging.DEBUG)

@on_exception(expo, Exception, max_time=1, max_tries=3)
def run_code():

    import telegram
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
    import openai
    import datetime


    # Set up OpenAI API key
    openai.api_key = config.api_key

    # Create a new Telegram bot object
    bot = telegram.Bot(token=config.telegram_token)

    current_time = datetime.datetime.now().strftime("(%Y-%m-%d %H:%M:%S)")


    # Function to send a message to the OpenAI chatbot model and return its response
    def send_message(message_log):
        # Use OpenAI's ChatCompletion API to get the chatbot's response
        response = openai.ChatCompletion.create(
            model=config.model,  # The name of the OpenAI chatbot model to use
            messages=message_log,   # The conversation history up to this point, as a list of dictionaries
            max_tokens=2048,        # The maximum number of tokens (words or subwords) in the generated response
            stop=None,              # The stopping sequence for the generated response, if any (not used here)
            temperature=1,        # The "creativity" of the generated response (higher temperature = more creative Max 2)
        )

        # Find the first response from the chatbot that has text in it (some responses may not have text)
        for choice in response.choices:
            if "text" in choice:
                return choice.text

        # If no response with text is found, return the first response's content (which may be empty)
        return response.choices[0].message.content


    # Function to handle Telegram commands
    def start(update, context):
        # Send a welcome message to the user
        update.message.reply_text("Hello! I am an AI assistant. How can I help you today?")

    def description(update, context):
        # Send a welcome message to the user
        update.message.reply_text("You can Direcly send the problem to me and I will try to solve it. If you want to know more about me please type /author. Thank you for using this bot.")

    def author(update, context):
        # Send a welcome message to the user
        update.message.reply_text("Hello I am Prince Kakkad. I am the author of this bot. Hope you Liked this bot. If you have any suggestions or queries please contact me on my email id: princekakkad10@gmail.com. Thank you for using this bot.")


    # Function to handle Telegram messages
    def echo(update, context):
        # Get the user's message and add it to the conversation history
        user_input = update.message.text
        message_log = context.user_data.get("message_log", [])
        message_log.append({"role": "user", "content": user_input})
        context.user_data["message_log"] = message_log

        # Send the conversation history to the chatbot and get its response
        response = send_message(message_log)

        # Add the chatbot's response to the conversation history and send it to the user
        message_log.append({"role": "assistant", "content": response})
        context.user_data["message_log"] = message_log
        update.message.reply_text(response)

        # Log the conversation to a file
        with open(config.conversation_log, "a") as f:
            f.write(f" ==================================================== \n *********** Prince Chat_GPT_Telegram_bot *********** \n ==================================================== \n\n")
            f.write(f"{current_time}: {update.message.chat.username or update.message.chat.first_name} [{update.message.chat.id}]: {user_input}\n")
            f.write(f"{current_time}: {bot.username}: {response}\n\n --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")

        chat_id = update.message.chat.id
        chat_id_log = config.chat_log

        # read the existing chat IDs from the log file
        with open(chat_id_log, "r") as f:
            chat_ids = set(map(int, f.read().splitlines()))

        # check if the chat ID is already in the set
        if chat_id not in chat_ids:
            # if the chat ID is not in the set, append it to the log file and the set
            with open(chat_id_log, "a") as f:
                f.write(str(chat_id) + "\n")
            chat_ids.add(chat_id)
           


    # Main function that runs the Telegram bot
    def main():
        # Create an Updater object to receive updates from Telegram
        updater = Updater(token=config.telegram_token, use_context=True)

        # Get the Dispatcher object to register handlers
        dispatcher = updater.dispatcher

        # Register a handler for the /start command
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("description", description))
        dispatcher.add_handler(CommandHandler("author", author))

        # Register a handler for messages (all messages that are not commands)
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        # Start the bot
        updater.start_polling()

        # Run the bot until Ctrl-C is pressed or the process is interrupted
        updater.idle()

    print(config.banner1)
    print(config.banner2)
    
    # Call the main function if this file is executed directly (not imported as a module)
    if __name__ == "__main__":
        main()

    return
run_code()
