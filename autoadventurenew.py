import time
import datetime
import threading
import requests
import json
import getpass
import os
import datetime

print()
print('-----------------------------------------------------------------------------------------------------')
print()

user = getpass.getuser()
path = (f'C:/Users/{user}/autoadventure')
if os.path.exists(path) == True:
    pass
else:
    os.mkdir(path)
boosters = input('Do you have boosters enabled? Y/N ').upper()
adv = int(input('Which adventure did you want to idle? '))
leng = adv * 3600
chng = input('Are you using a different channel than last use? Y/N: ').upper()
if chng == 'Y':
    channelid = input('Input Channel ID for discord: ')
    f = open(f'C:/Users/{user}/autoadventure/channelid.txt', 'w+')
    f.write(f'{channelid}')
    f.close()
else:
    f = open(f'C:/Users/{user}/autoadventure/channelid.txt', 'r+')
    channelid = f.read()
    f.close()
auth = input('Has your authorization key changed? Y/N: ').upper()
if auth == 'Y':
    f = open(f'C:/Users/{user}/autoadventure/authkey.txt', 'w+')
    authcode = input('Please enter your authorization key: ')
    f.write(f'{authcode}')
    f.close()
else:
    f = open(f'C:/Users/{user}/autoadventure/authkey.txt', 'r+')
    authcode = f.read()
    f.close()
if boosters == 'Y':
    leng = leng/2
convert = datetime.timedelta(seconds=leng)

# payloads

url = f'https://discord.com/api/v9/channels/{channelid}/messages'

adventurecont = {
    'content': f"<@424606447867789312> adventure {adv}"
}
stealcont = {
    'content': f"<@424606447867789312> steal"
}
praycont = {
    'content': f"<@424606447867789312> pray"
}
statuscont = {
    'content': f"<@424606447867789312> status"
}
headers = {
        'authorization': f'{authcode}'
    }

def adventure():
    global adv
    msg= []
    counter = 0
    while True:
        time.sleep(5)
        r = requests.post(url, headers=headers, data=adventurecont,)
        print(f'Adventure Started | Level {adv} | Length {convert}')
        time.sleep(leng)
        r = requests.post(url, headers=headers, data=statuscont,)
        counter = counter+1
        time.sleep(3)
        r2 = requests.get(url, headers=headers,)
        info = json.loads(r2.text)
        for value in info:
            msg.append(value['content'])
        check = msg[0]
        lvl = (f"You reached a new level: **{adv+1}** :star:! You received a special weapon as a reward :tada:!")
        if check == lvl:
            adv = adv+1
            print(f'You leveled up! advancing to adventure {adv}!')
        print(check)
        print()
        print(datetime.datetime.now())
        print()
        print(f'Adventure {adv} Complete!')
        print(f'You have completed {counter} adventure(s) this session!')
def pray():
    while True:
        time.sleep(10)
        r = requests.post(url, headers=headers, data=praycont,)
        print(f'Pray attempted, will try again in 5 hours')
        time.sleep(18000)

def steal():
    while True:
        time.sleep(15)
        r = requests.post(url, headers=headers, data=stealcont,)
        print(f'Steal attempted, will try again in 1 hour')
        time.sleep(3600)

if __name__ == "__main__":
    p1 = threading.Thread(target=adventure)
    p2 = threading.Thread(target=pray)
    p3 = threading.Thread(target=steal)

    p1.start()
    p2.start()
    p3.start()