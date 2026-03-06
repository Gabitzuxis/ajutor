import json

with open("backend/config.json") as f:
    USERS = json.load(f)["users"]

def check_login(username,password):

    for u in USERS:
        if u["username"]==username and u["password"]==password:
            return True

    return False
