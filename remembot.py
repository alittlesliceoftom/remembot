from remembot.random_message import *
from remembot.remembot_classes import *

if __name__ == '__main__':
    # filename = "quotes.json"
    # data = read_json(filename)
    msg = get_message_from_json(data)
    # # print(msg)
    # g = get_config('slackbot')
    # channel = g['channel']

    # send_message_to_slack(message=msg, channel='@tomoneill', status=MsgStatus.OK)
    # print(msg)

    #test setup of classes
    i = item_to_remember(name = "Spotify on engineering", msg = "Innovation >> Predictability ", link = "https://www.youtube.com/watch?v=R2o-Xm3UVjs")
    u = user(name = 'Tom')
    u.remember_items_from_json()
    u.remember_item(i)
    u.remind_user(i.name)