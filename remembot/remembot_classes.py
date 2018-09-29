from remembot.random_message import *

class item_to_remember():

    def __init__(self, name, msg, link = None):
        self.name = name
        self.views = 0
        self.msg = msg
        if link:
            self.link  = link

    def increment_item_view_count(self):
        self.view += 1


class user():

    def __init__(self, name, reminder_freq = 'Daily', user_handle = "@tomoneill"):
        self.user_handle = user_handle
        self.reminder_freq = reminder_freq ## preference of user
        self.items_to_remember = []#None

    def remember_item(self, item):
        # if self.items_to_remember:
        self.items_to_remember.append({'name':item.name, 'item':item})
        # else:
        #     self.items_to_remember = [{'name':item.name, 'item':item}]


    def remind_user(self, item_name):
        print(self.items_to_remember)
        item = list(filter(lambda x: x['name'] == item_name, self.items_to_remember))[0]['item']  #https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
        print(item)
        send_message_to_slack(message=item.msg,  channel=self.user_handle , status=MsgStatus.OK)
