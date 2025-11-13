import pyfiglet
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('aoos')
print(Z+logo)

loo = pyfiglet.figlet_format('AOOS')
print(F+loo)

k=("----+----+-----+------+-----+")
 
print(C+k)

lo=("Tele:@wwnww3\nCh Tele:@wwnww3")
print(X+lo)

i=("----+----+-----+------+-----+")
print(C+i)
o=("#====================================##============================")

print(B+o)




import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print("@wwnww3")
ch = "@Jackthe_ripper_bot"
api_id = '37196000'
api_hash = '8a86ccc80baef754ef1111d3422ed705'
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(sheko.txt","r").read().split("\n"):
    try:
        client.send_message(ch ,f"/chk {cc}")
        time.sleep(random.randint(20,20))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            t = str(mssag[0].message).split("again after ")[1]
            t = t.split("seconds")[0]
            t = int(t)
            print(f"Done Sleep : {t+2}")
            time.sleep(t+2)
        print(mssag[0].message)
        time.sleep(1)
    except:
        print(False)
