from remembot.random_message import *

if __name__ == '__main__':
    filename = "quotes.json"
    data = read_json(filename)
    msg = get_message_from_json(data)
    print(msg)
    g = get_config('slackbot')
    channel = g['channel']

    send_message_to_slack(message=msg, channel='@tomoneill', status=MsgStatus.OK)
    print(msg)