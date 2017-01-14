# -*= coding: utf-8 -*-

from twitter import *
from time import sleep

def Init():
    token = "<< token >>"
    token_secret = "<< token_secret >>"
    consumer_key = "<< consumer_key >>"
    consumer_secret = "<< consumer_secret >>"
    
    #premise
    user_name = input("Please enter username: \n")
    maximum = int(input("Please enter maximum page(200 users in one page: \n")) #maximum pages

    return Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret)), user_name, maximum

def main(t, user, maximum_page):
    _cursor = -1 #default
    num = 200 #maximum of count
    current = 0 #order
    page = 0 # current page
    
    while page < maximum_page:
        statusUpdate = t.followers.list(screen_name= user, cursor=_cursor, count=num)
        users = statusUpdate['users']
        for name in users:
            current += 1
            print(str(current)+" :"+name['name'])
            sleep(0.5)
        page += 1
        _cursor=statusUpdate['next_cursor']

if __name__ == '__main__':
    t, user, maximum_page = Init()
    main(t, user, maximum_page)
