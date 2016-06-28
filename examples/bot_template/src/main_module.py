from mc import MC


def main_handler(ctx):
    """
    :param ctx:
     Dict
     ctx is the context object containing message data, the user who owns the bot instance, and

    :return:
        The bot's return value will be POSTed to its specified webhook address, if one is provided.
    """
    # First create an instance of the API interface
    api = MC(ctx)
    # Replace 'pass' with your code.
    # Try uncommenting the line(s) below to send an email to yourself with the original message.
    # api.send_email(ctx['user']['email'], "Original message:\n" + str(ctx['message']),
    #                                  subject='Hello from Machine Colony!')
    pass
