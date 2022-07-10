from forwardsbot import bot

if __name__ == '__main__':
    """
    Run bot with polling method
    """
    bot.remove_webhook()
    bot.polling(skip_pending=True)
