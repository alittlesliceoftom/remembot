import random
import configparser
import os
from slack_bot import send_message_to_slack, MsgStatus
import json


def get_config(section):
    config = configparser.ConfigParser()
    path = os.path.dirname(os.path.realpath(__file__))
    config.read(os.path.join(path, 'config.ini'))

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
        messageReference = random.randint(1, l)
    return conf[str(messageReference)]


def get_message_from_json(data, msgSection='quotes', quoteValue=None):
    array = data[msgSection]
    if not quoteValue:
        ##get a random quote if no quote requested
        l = len(array)
        quoteValue = random.randint(0, l - 1)
    message = array[quoteValue]
    return message


def read_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def add_quote(data, s=None, msgSection='quotes', ):
    '''
    adds a quote to the json object "data"
    :param data:
    :param s: if provided add this quote, if not ask for user input
    :param msgSection:
    :return:
    '''
    if not s:
        # if no strin provided request input
        s = input("Add your quote here: ")
    if s == '':
        return
    array = data[msgSection]
    array.append(s)
    data[msgSection] = array
    return data



if __name__ == "__main__":
    filename = "quotes.json"
    data = read_json(filename)
    # data = add_quote(data)
    msg = get_message_from_json(data)
    print(msg)
    g = get_config('slackbot')
    channel = g['channel']

    #add a quotew
    # filename = "quotes.json"
    # data = read_json(filename)
    # data = add_quote(data)
    # with open(filename,'w') as f:
    #     json.dump(data, f)
    # print(data)  # print out the data we have now

    send_message_to_slack(message=msg, channel='@tomoneill', status=MsgStatus.OK)
    print(msg)
    # for (i, s) in conf.items():
    #     print(s)
    #     print(i)
