from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

Token = "Make your telegram bot token here"

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = 'Hi, I\'m a Telegram bot that help you to get your Identifier (ID) in telegram App,\nyou\'re welcome.')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = 'Hello Mr ' + str(update.effective_chat.effective_name) +',\nYour Identifier (ID) in telegrame is : ' + str(update.effective_chat.id))

if __name__ == '__main__':
    application = ApplicationBuilder().token(Token).build()

    #command handlers
    help_handler = CommandHandler('help', help)
    start_handler = CommandHandler('start', start)

    #register commands
    application.add_handler(help_handler)
    application.add_handler(start_handler)

    application.run_polling()
