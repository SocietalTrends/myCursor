from twitter import *
from time import sleep

token = "<< token >>"
token_secret = "<< token_secret >>"
consumer_key = "<< consumer_key >>"
consumer_secret = "<< consumer_secret >>"
user_name = input("Please enter username: \n")
maximum_page = int(input("Please enter maximum page: \n")) #$B$$$/$D$^$G%Z!<%8$r?J$a$k$+(B
_cursor = -1 #default
num = 200 #maximum
current = 0 #$B=xNs(B
page = 0 #$B8=:_%Z!<%8(B

t = Twitter(
        auth = OAuth(token, token_secret, consumer_key, consumer_secret)
        )

while page < maximum_page:
    statusUpdate = t.followers.list(screen_name= user_name, cursor=_cursor, count=num)
    users = statusUpdate['users']
    for name in users:
        current += 1
        print(str(current)+" :"+name['name'])
        sleep(0.5)
    page += 1
    _cursor=statusUpdate['next_cursor']
