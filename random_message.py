import random
import configparser
import os
from slack_bot import send_message_to_slack, MsgStatus

def get_config(section):
    config = configparser.ConfigParser()
    path = os.path.dirname(os.path.realpath(__file__))
    config.read(os.path.join(path,'config.ini') )

    if section in config.sections():
        return config[section]
    else:
        raise Exception('Config for {} does not exist'.format(section))

def get_message(messageReference = None):
    '''Config contains quotes'''
    ##could improve by using a hierarchical json, then can do logic which
    conf = get_config('quotes')
    l = len(conf.items())
    if messageReference == None:
        messageReference = random.randint(1,l)
    return conf[str(messageReference)]


if __name__ == "__main__":
    msg = get_message()
    print(msg)
    g = get_config('slackbot')
    channel = g['channel']

    send_message_to_slack(message = msg, channel = '@tomoneill', status = MsgStatus.OK)

    # send_message_to_slack(message = msg, channel = channel, status = MsgStatus.OK)
