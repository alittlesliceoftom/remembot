import requests
import json
from datetime import datetime
from slack_bot import send_message_to_slack, MsgStatus

def process_location(site, id):

    response = requests.get("http://magicseaweed.com/api/7aa0845eb05ef65f17815efec7b4edaa/forecast/?spot_id={}&fields=localTimestamp,fadedRating, solidRating,period,height".format(id))

    if response.status_code == 200:
        print('request sucessful')
    else:
        raise Exception

    data = response.json()

    s = ''
    #retuns a list of dicts.
    for i, d in enumerate(data):
        d['dateTime'] = datetime.strftime(datetime.fromtimestamp(d['localTimestamp']), '%Y-%m-%d %H:%M')
        if d['solidRating'] >= 3 or d['fadedRating'] > 3:#check if  rating is good. Based on Dyl's recommendations
            s = s + '\n' + str(d)

    #output to slack:
    if s:
        msg = "At {}, the following surf looks good in the next 7 days: \n".format(site)
        msg = msg + s
        print(msg)

        send_message_to_slack(message=msg, channel='@tomoneill', status=MsgStatus.OK)
        send_message_to_slack(message=msg, channel='@dylan.atwell', status=MsgStatus.OK)
    return

if __name__ == '__main__':
    locs = ["Porthcawl", "Woolacombe"]
    ids = [1449,1352]
    sites = dict(zip(locs,ids))
    print(sites)

    for k, v in sites.items():
        process_location(k, v)