# -*- coding: utf-8 -*-

__version__ = '0.1'
__author__ = 'thinkerleo'

#自动发微博工具
import time
from api import APIClient #新浪微博SDK By @Liaoxuefeng
import webbrowser
import urllib
import whether

APP_KEY = 'XXXXXXXXX'    # 填写申请的APP_KEY
APP_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'    # 填写申请的APP_SECRET
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

# 获取微博授权
def getclient():
    url = client.get_authorize_url()

    print webbrowser.open(url)    # 浏览器打开该url，取得code='xxx'

    code = raw_input('Enter code >')

    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in

    client.set_access_token(access_token, expires_in)


# 发微博，text为微博内容
def posttext(text):
    utext = unicode(text, "UTF-8")
    client.statuses.update.post(status=utext)
    print '微博发送成功'

if __name__ == '__main__':
     while True:
         getclient()
         posttext(raw_input('请输入要发送的文字： '))
         time.sleep(60)
