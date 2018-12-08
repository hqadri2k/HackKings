import itertools
import pynder

number = 0;
session = None;
nearby = None;

def login(FBTOKEN, FBID):
    try:
        session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)
    except:
        return None
    find_nearby()

def find_nearby():
    nearby = session.nearby_users()

def get_next_user():
    user = users[number]
    number++
    return json.dumps(user, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def like():
    users[number-1].like()

def dislike(user):
    users[number-1].dislike()

def getSession():
    return session

def getNumber():
    return number
