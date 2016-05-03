import mc


def main_handler(ctx):
    """
    :param ctx:
     Dict
     ctx is the context object of where the bot is being run.

     It contains, at a minimum, the following parameters:
        'user': Dict. The user object of whoever owns the bot instance
        'bot_instance': Dict. The entire bot instance object
        'bot_type': Dict. The bot type object
        'message': Dict. The original message passed to the bot, e.g. data from a webhook or a scheduled run
        'botfile': Dict. The bot type's botfile.json, as a dictionary.

    :return:
     Main handlers do not return. Typically a bot will call back a webhook address, send notifications,
     or trigger other bots, passing data along a chain.
    """
    # Replace 'pass' with your code.
    # Try uncommenting the line(s) below to send an email to yourself with the original message.
    # mc.utils.notifications.send_email(ctx['user']['email'], "Original message:\n" + str(ctx['message']),
    #                                  subject='Hello from Machine Colony!')
    pass
