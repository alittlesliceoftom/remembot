from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from remembot.remembot_classes import *  #note dodgy chained import!

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    message.send('I can help everybody!')

    # Start a thread on the original message
    message.reply("Here's a threaded reply", in_thread=True)


@respond_to('remind me')
def send_message(message):
    filename = "quotes.json"
    data = read_json(filename)
    msg = get_message_from_json(data)
    date = '20180101 - example date'  #@todo replace this with call to object metadata
    msg = 'Sure thing remember this, added on {}:\n'.format(date) + msg
    message.send(msg)

@respond_to('remember (.*)')
def add_message(message_object, param_string):
    """
    Adds the message to the list of items that the user wants to remember
    :param message:
    :return:
    """
    filename = "quotes.json"
    messages = read_json(filename)
    messages = add_quote(messages = messages, s = param_string)
    with open(filename,'w') as f:
        json.dump(messages, f)

    message_object.reply('added that to the memory bank')
    return