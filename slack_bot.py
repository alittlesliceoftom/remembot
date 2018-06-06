import requests
import json

from enum import Enum
import configparser
from python_logger import logger_set_up
from data_connections import get_config

log = logger_set_up(__file__)

class MsgStatus(Enum):
    ERROR = '#D00000'  # Red
    WARNING = '#ff8000'  # Amber
    INFO = '#bbbbbb'  # Grey
    OK = '#00D000'  # Green


def send_message_to_slack(message,
                          title='',
                          channel='@tom.oneill',
                          status=MsgStatus.INFO,
                          attachment=True):
    """Send a message to Slack from TradingBot.
    By default, messages are sent as an attachment with an error highlight (i.e. red) to the
    #tribe_trading channel.  Markdown formatting is supported in the message body but not in
    the message title.
    Args:
        message (str): The message content; markdown formatting is supported.
        title (str): Optional argument that will be shown as the title of the Slack message;
            the title is ignored if the message is sent with attachment=False; markdown
            formatting is not supported in the title.
        channel (str): The destination channel e.g. '#some_channel' or '@some_person'; the
            default is '#tribe_trading'.
        status (MsgStatus): Set the message status (a colour highlight to the left of the text);
            options are MsgStatus.ERROR, MsgStatus.WARNING, MsgStatus.INFO or MsgStatus.OK; this
            setting is ignored if the message is sent with attachment=False.
        attachment (bool): Set to False to send as a regular message rather than as an
            attachment; the default is True, as attachments support more formatting features.
    Returns:
        None
    """

    msg = {
        'username': 'Remembot',
        'icon_emoji': ':rick:',
        'channel': channel
    }

    if attachment:

        if type(status) != MsgStatus:  # Assume INFO status on bad status input
            status = MsgStatus.INFO

        msg['attachments'] = [{
                'fallback': title,
                'color': status.value,
                'text': message,
                'title': title,
                'mrkdwn_in': ['text']
            }]

    else:
        msg['text'] = message

    hook = _get_slack_hook()

    if hook:
        try:
            response = requests.post(hook,
                                     headers={'Content-Type': 'application/json'},
                                     data=json.dumps(msg))
            response.raise_for_status()
        except Exception as e:
            log.exception('OMG - something went wrong!\n{}'.format(e))


def _get_slack_hook():
    """Gets the Slack hook from the config file.
    Returns:
        str|False:  A string containing the Slack hook, or False if there was a
            problem retrieving it
    """
    try:
        return get_config('slackbot')['hook']
    except Exception as e:
        log.exception("OMG - something went wrong!\n{}".format(e))

    return False

