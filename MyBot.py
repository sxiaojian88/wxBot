#!/usr/bin/env python
# coding: utf-8

import time
import string
from wxbot import *

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            if string.find(msg['content']['user']['name'], u'孙晓健') != -1:
                if string.find(msg['content']['data'],u'.jd.') != -1 :
                    self.send_msg_by_uid(u'hi', msg['user']['id'])

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.run()

if __name__ == '__main__':
    main()