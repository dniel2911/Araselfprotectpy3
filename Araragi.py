# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator

#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#

# di larang untuk merubah bagian ini untuk menghargai saya yang membuat created : Araragi kanega
# thank for :
# Agy pascha (nvstarbot) 
# Hanavi koplaxs
# NadyaTjia
# dan teman teman lainya yang sudah membantu dan memberi saya sc segaligus saran
# gunakan bot ini dengan bijak.  Jangan berharap lebih, scrib ini masih mau di revisi dan belom sempurna
# jika memerlukan atau ada yang ingin di tanyakan hubungi ➡ id line : araragi.  (pakai titik)  ◀ 

#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#


botStart = time.time()
araragiayane = LINE('Etgb7UIMhF9qGsqaGnze.NnWPYXrsfOYTRMjXCBEM7G.eBdwQBq3VIcFj7p7Zr0msYdwKyS7/RzymGqwGw+AnHQ=')
araragiayane.log("Auth Token : " + str(araragiayane.authToken))


oepoll = OEPoll(araragiayane)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = araragiayane.getSettings()
araragiayaneProfile = araragiayane.getProfile()
araragiayaneMID = araragiayane.profile.mid
myProfile["displayName"] = araragiayaneProfile.displayName
myProfile["statusMessage"] = araragiayaneProfile.statusMessage
myProfile["pictureStatus"] = araragiayaneProfile.pictureStatus
admin=['u9cdc29cb1452168cadae627171b7a6ee','u529ed08e968ba9d107784186eb66b76a','ua5f2cbc325816777be5ef529eb920c50',araragiayaneMID]
msg_dict = {}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
bl = [""]

#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#


def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ INFO ] BOT RESETED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    araragiayane.log("[ EROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        araragiayane.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
        
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#

def helpmessage():
    helpMessage = """╔═══════════
╠ [ AraragyAyane]
╠✪➠➠〘 help 〙 ﷽
╠☂⃟☂࿐「Help」
╠☂⃟☂࿐「HelpTag」
╠☂⃟☂࿐「HelpKick」
╠✪➠➠〘 Bot 〙 ﷽
╠☂⃟☂࿐「Rebot」
╠☂⃟☂࿐「Runtime」
╠☂⃟☂࿐「Speed」
╠☂⃟☂࿐「Set」
╠☂⃟☂࿐「About」
╠✪〘 Sett 〙 ﷽
╠☂⃟☂࿐「Add」
╠☂⃟☂࿐「Join」
╠☂⃟☂࿐「Leave」
╠☂⃟☂࿐「Read」
╠☂⃟☂࿐「Inviteprotect」
╠☂⃟☂࿐「Reread」
╠☂⃟☂࿐「Qr」
╠☂⃟☂࿐「Qrjoin」
╠☂⃟☂࿐「Ck」
╠☂⃟☂࿐「Groupprotect」
╠☂⃟☂࿐「Kc」
╠☂⃟☂࿐「Ptt」
╠✪➠➠〘 Self 〙 ﷽
╠☂⃟☂࿐「Me」
╠☂⃟☂࿐「MyMid」
╠☂⃟☂࿐「MyName」
╠☂⃟☂࿐「MyBio」
╠☂⃟☂࿐「MyPicture」
╠☂⃟☂࿐「MyCover」
╠☂⃟☂࿐「Contact @」
╠☂⃟☂࿐「Mid @」
╠☂⃟☂࿐「Name @」
╠☂⃟☂࿐「Bio @」
╠☂⃟☂࿐「Picture @」
╠☂⃟☂࿐「Cover @」
╠☂⃟☂࿐「Removeallchat」
╠☂⃟☂࿐「Frienlist」
╠✪➠➠〘 Group 〙✪ ﷽
╠☂⃟☂࿐「Gowner」
╠☂⃟☂࿐「Gurl」
╠☂⃟☂࿐「O/Curl」
╠☂⃟☂࿐「Lg」
╠☂⃟☂࿐「Gb」
╠☂⃟☂࿐「Ginfo」
╠☂⃟☂࿐「Ri @」
╠☂⃟☂࿐「Tk @」
╠☂⃟☂࿐「Mk @」
╠☂⃟☂࿐「Vk @」
╠☂⃟☂࿐「Vk:mid」
╠☂⃟☂࿐「Nk Name」
╠☂⃟☂࿐「Uk mid」
╠☂⃟☂࿐「NT Name」
╠☂⃟☂࿐「Zk」
╠☂⃟☂࿐「Zt」
╠☂⃟☂࿐「Zm」
╠☂⃟☂࿐「Cancel」
╠☂⃟☂࿐「Gn Name」
╠☂⃟☂࿐「Gc @」
╠☂⃟☂࿐「Inv mid」
║☂⃟☂࿐「Ban @」
║☂⃟☂࿐「Unban @」
║☂⃟☂࿐「clear Ban」
║☂⃟☂࿐「Kill Ban」
╠☂⃟☂࿐「Zk」
╠✪➠➠〘 Khusus 〙 ﷽
╠☂⃟☂࿐「Tagall」
╠☂⃟☂࿐「S N/F/R」
╠☂⃟☂࿐「R」
╠☂⃟☂࿐「F/Gbc」
╠☂⃟☂࿐「/invitemeto:」
╠☂⃟☂࿐「invite」
╠☂⃟☂࿐「Op @」
╠☂⃟☂࿐「Deop @」
╠☂⃟☂࿐「Mop:mid」
╠☂⃟☂࿐「Mdp:mid」
╠☂⃟☂࿐「Opmid」
╠☂⃟☂࿐「Oplist」
╚═[ Araragy ]"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""╔══[ Help Tagger ]
╠☂⃟☂࿐「Ri @」
╠☂⃟☂࿐「Tk @」
╠☂⃟☂࿐「Mk @」
╠☂⃟☂࿐「Vk @」
╠☂⃟☂࿐「Gc @」
╠☂⃟☂࿐「Mid @」
╠☂⃟☂࿐「Name @」
╠☂⃟☂࿐「Bio @」
╠☂⃟☂࿐「Picture @」
╠☂⃟☂࿐「Cover @」
║☂⃟☂࿐「Ban @」
║☂⃟☂࿐「Unban @」
╚═[ Help Tagger ]"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""╔══[ Help kicker ]
╠☂⃟☂࿐「Ri @」
╠☂⃟☂࿐「Tk @」
╠☂⃟☂࿐「Mk @」
╠☂⃟☂࿐「Vk @」
╠☂⃟☂࿐「Vk:mid」
╠☂⃟☂࿐「Nk Name」
╠☂⃟☂࿐「Uk mid」
╠☂⃟☂࿐「Kill ban」
╠☂⃟☂࿐「Zk」
╚═[ Help kicker ]"""
    return helpMessageKick
    
    
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#



def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = araragiayane.getContact(op.param1)
            print ("[ 5 ] NOTICED ADDERS CONTACT: " + contact.displayName)
            if settings["autoAdd"] == True:
                araragiayane.findAndAddContactsByMid(op.param1)
                araragiayane.sendMessage(op.param1, "Cie kakak add aku diem diem ya 😳 {} dedek jadi malu hehe！".format(str(contact.displayName)))
                araragiayane.sendMessage(op.param1, "Salam kenal ya kakak^^")
        if op.type == 11:
            group = araragiayane.getGroup(op.param1)
            contact = araragiayane.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = araragiayane.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    araragiayane.updateGroup(gs)
                    invsend = 0
                    araragiayane.sendMessage(op.param1,araragiayane.getContact(op.param2).displayName + "Heh kutil baby jagan Mainan group seenak nya ")
                    araragiayane.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][target] = True
        if op.type == 13:
            contact1 = araragiayane.getContact(op.param2)
            contact2 = araragiayane.getContact(op.param3)
            group = araragiayane.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    araragiayane.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    araragiayane.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    araragiayane.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][target] = True
            if araragiayaneMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "Makasih kakak udah undang aku ya 😄\nSalam kenal ya... \nHai kamu sider salam kenal juga buat mu 😜"
                        araragiayane.acceptGroupInvitation(op.param1)
                        araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        araragiayane.sendMessage(op.param1, "Created ：")
                        araragiayane.sendContact(op.param1, "u9cdc29cb1452168cadae627171b7a6ee")
                    except Exception as error:
                        print(error)
            if araragiayaneMID in op.param3:
                if settings["autoPtt"] == True:
                    araragiayane.acceptGroupInvitation(op.param1)
                    araragiayane.sendMessage(op.param1, "waduh group apa nih coy main invit aje kampret\ngw di suruh out nih sama tuan ku\nbye bye kalian semua mampir lewat ya.... Se you\nNgenng.... ")
                    araragiayane.sendMessage(op.param1, "Created ：")
                    araragiayane.sendContact(op.param1, "u9cdc29cb1452168cadae627171b7a6ee")
                    araragiayane.leaveGroup(op.param1)
        if op.type == 15:
            contact1 = araragiayane.getContact(op.param2)
            group = araragiayane.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('waduh ada yang baper :v\n')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Selamat Tinggal Semoga Betah di alam sana. Jangan balik lagi ke {} 🙅".format(str(group.name))
                    araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = araragiayane.getContact(op.param2)
            group = araragiayane.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('Haee brroooo.. ')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + " Welkam di group {} Jangan lupa cek note ya nyett,Baca and Taati rules ato gw bacok ！".format(str(group.name))
                    araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = araragiayane.getContact(op.param2)
            group = araragiayane.getGroup(op.param1)
            contact2 = araragiayane.getContact(op.param3)
            print ("[19] KICK OUT FROM GROUP: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('Dangger!! ')
                            arr = []
                            mention1 = "@Araragi"
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + 'Menendang '
                            mention2 = "@kick "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            araragiayane.kickoutFromGroup(op.param1,[op.param2])
                            settings["blacklist"][op.param2] = True
                            time.sleep(0.1)
                            araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        araragiayane.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('Dangger !! ')
                        arr = []
                        mention1 = "@araragi "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + 'Menendang  '
                        mention2 = "@kick "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                else:
                    pass
        if op.type == 22:
            print ("[ 22 ] NOTICED LEAVE GROUP")
            if settings["autoLeave"] == True:
                araragiayane.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1] NOTICED FILE KONFIGURASI")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != araragiayane.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ INFO ]"
                    ret_ += "\nID   : {}".format(stk_id)
                    ret_ += "\nID   : {}".format(pkg_id)
                    ret_ += "\nURL  : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\nWEB  ：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ INFO ]"
                    araragiayane.sendMessage(to, str(ret_))
                    araragiayane.sendImageWithURL(to, path)
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = araragiayane.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = araragiayane.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        araragiayane.sendMessage(msg.to,"[NAMA]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Check]:\n" + contact.statusMessage + "\n[URL]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[COVER]:\n" + str(cu))
                    else:
                        contact = araragiayane.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = araragiayane.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        araragiayane.sendMessage(msg.to,"[NAMA]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Check]:\n" + contact.statusMessage + "\n[URL]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[COVER]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s\n%s\n"%("---[Share Post]---","[Creator]:")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[Keterangan]:\n" + msg.contentMetadata["text"] + "\n(Hanya Menampilkan kan 💯 kata)" + "\n[Url]:\n" + msg.contentMetadata["postEndUrl"]
                            araragiayane.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "---[Post]---\n[Created ]:\n" + msg.contentMetadata["text"] + "\n(Hanya menampilkan 💯 kata)"
                        ret_ += "\n[Url]:\n" + msg.contentMetadata["postEndUrl"]
                        araragiayane.sendMessage(msg.to, str(ret_))


#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
       
                        
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if msg.text in ["help"]:
                    helpMessage = helpmessage()
                    araragiayane.sendMessage(to, str(helpMessage))
                    araragiayane.sendMessage(to, "My Creator:")
                    araragiayane.sendContact(to, "u9cdc29cb1452168cadae627171b7a6ee")
                elif text.lower() == 'helptag':
                    helpMessageTag = helpmessagetag()
                    araragiayane.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    araragiayane.sendMessage(to, str(helpMessageKick))
                elif text.lower() == 'creator':
                    araragiayane.sendMessage(to, "My Creator:")
                    araragiayane.sendContact(to, "u9cdc29cb1452168cadae627171b7a6ee")
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = araragiayane.getAllContactIds()
                    for manusia in t:
                        araragiayane.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = araragiayane.getGroupIdsJoined()
                    for manusia in n:
                        araragiayane.sendMessage(manusia,(bctxt))
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = araragiayane.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    araragiayane.kickoutFromGroup(to,[target])
                                    araragiayane.findAndAddContactsByMid(target)
                                except:
                                    pass
                elif "Ri:" in msg.text:
                    midd = text.replace("Ri:","")
                    araragiayane.kickoutFromGroup(to,[midd])
                    araragiayane.findAndAddContactsByMid(midd)
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    araragiayane.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                araragiayane.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = araragiayane.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    araragiayane.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = araragiayane.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    araragiayane.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = araragiayane.getGroup(to)
                            araragiayane.sendMessage(to, "Jangan benci jangan dendam ya kakak")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            araragiayane.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "Zk" in msg.text:
                    gs = araragiayane.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    araragiayane.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    araragiayane.kickoutFromGroup(msg.to,[midd])
                    araragiayane.findAndAddContactsByMid(midd)
                    araragiayane.inviteIntoGroup(msg.to,[midd])
                    araragiayane.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = araragiayane.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    araragiayane.kickoutFromGroup(msg.to,[target])
                                    araragiayane.findAndAddContactsByMid(target)
                                    araragiayane.inviteIntoGroup(msg.to,[target])
                                    araragiayane.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = araragiayane.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        araragiayane.sendMessage(to,mc)
                elif text.lower() == 'zt':
                    gs = araragiayane.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'zm':
                    gs = araragiayane.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = "Mid："
                        for mi_d in targets:
                            mc += "\n->" + mi_d
                        araragiayane.sendMessage(to,mc)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    araragiayane.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = araragiayane.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak Dikenal"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Open"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragiayane.reissueGroupTicket(group.id)))
                    else:
                        gQr = "Close"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragiayane.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Info Group ]"
                    ret_ += "\n╠ group Nama : {}".format(str(group.name))
                    ret_ += "\n╠ Id : {}".format(group.id)
                    ret_ += "\n╠ creator : {}".format(str(gCreator))
                    ret_ += "\n╠ Members : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Pendingan : {}".format(gPending)
                    ret_ += "\n╠ Qr : {}".format(gQr)
                    ret_ += "\n╠ Tiket : {}".format(gTicket)
                    ret_ += "\n╚══[ End ]"
                    araragiayane.sendMessage(to, str(ret_))
                    araragiayane.sendImageWithURL(to, path)
                    
                    
#________________________________________________________________________________________________________________#                       
                    
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = araragiayane.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = araragiayane.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            araragiayane.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        araragiayane.sendMessage(to, "Batal\nWaktu: %s Seconds" % (elapsed_time))
                        araragiayane.sendMessage(to, "Jumlah:" + sinvitee)
                    else:
                        araragiayane.sendMessage(to, "Tidak ada daftar pendingan")
                        
#________________________________________________________________________________________________________________#                        
                        
                elif text.lower() == 'gcancel':
                    gid = araragiayane.getGroupIdsInvited() 
                    start = time.time()
                    for i in gid:
                        araragiayane.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    araragiayane.sendMessage(to, "Semua Undangan Dibatalkan")
                    araragiayane.sendMessage(to, "Waktu: %s Seconds" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = araragiayane.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        araragiayane.updateGroup(X)
                    else:
                        araragiayane.sendMessage(msg.to,"Hanya di group")
                elif text.lower().startswith('op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        araragiayane.sendMessage(to, "Target Telah di tambahkan dalam daftar admin")
                elif text.lower().startswith('deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        araragiayane.sendMessage(to, "Target Telah di hapus dari Daftar Admin")
                elif text.lower().startswith('mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        araragiayane.sendMessage(to, "Target Telah di tambahkan dalam daftar admin") 
                        backupData()
                elif text.lower().startswith('mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        araragiayane.sendMessage(to, "Target Telah di hapus dari Daftar Admin") 
                        backupData()
                elif text.lower() == 'opmid':
                    if admin == []:
                        araragiayane.sendMessage(to, "Tidak Ada Admin")
                    else:
                        mc = "Daftar admin："
                        for mi_d in admin:
                            mc += "\n-> " + mi_d
                        araragiayane.sendMessage(to, mc)
                elif text.lower() == 'oplist':
                    if admin == []:
                        araragiayane.sendMessage(to, "Admin Kosong")
                    else:
                        mc = "Daftar Admin："
                        for mi_d in admin:
                            mc += "\n ➡ " + araragiayane.getContact(mi_d).displayName
                        araragiayane.sendMessage(to, mc)
                        
#________________________________________________________________________________________________________________#                        
                        
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = araragiayane.getContact(u)
                        cu = araragiayane.getProfileCoverURL(mid=u)
                        try:
                            araragiayane.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nurl :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nSampul :\n" + str(cu))
                        except:
                            araragiayane.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nStatus:\n" + contact.statusMessage + "\n\nsampul:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    araragiayane.findAndAddContactsByMid(midd)
                    araragiayane.inviteIntoGroup(msg.to,[midd])
                elif "take" in msg.text:
                    list_ = msg.text.split(":")
                    try:
                        araragiayane.acceptGroupInvitationByTicket(list_[1],list_[2])
                        G = araragiayane.getGroup(list_[1])
                        if G.preventedJoinByTicket == True:
                            pass
                        else:
                            G.preventedJoinByTicket = True
                            araragiayane.updateGroup(G)
                    except:
                        araragiayane.sendMessage(msg.to,"error\n"+list_[1]+'\n'+list_[2])      
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] Banned Sukses")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    araragiayane.sendMessage(to, "Target Ditambahkan dalam daftar blacklist")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] Unbanned sukses")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    araragiayane.sendMessage(to, "Target telah di hapus dari daftar blacklist ")
                                except:
                                    pass
                elif "Mb:" in msg.text:
                    midd = msg.text.replace("Mb:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        araragiayane.sendMessage(to, "Target Ditambahkan dalam daftar blacklist")
                    except:
                        pass
                elif "Mub:" in msg.text:
                    midd = msg.text.replace("Mub:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        araragiayane.sendMessage(to, "Target telah di hapus dari daftar blacklist")
                    except:
                        pass
                        
#________________________________________________________________________________________________________________#                       
                        
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    araragiayane.sendMessage(to, "Daftar Blacklist Telah di bersihkan")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        araragiayane.sendMessage(to, "Kosong")
                    else:
                        mc = "Daftar Blacklist："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + araragiayane.getContact(mi_d).displayName
                        araragiayane.sendMessage(to, mc)
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        araragiayane.sendMessage(to, "Kosong")
                    else:
                        mc = "Daftar Mid dalam Blacklist ："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + mi_d
                        araragiayane.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = araragiayane.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            araragiayane.sendMessage(to, "Blacklist kosong")
                            return
                        for jj in matched_list:
                            araragiayane.kickoutFromGroup(to, [jj])
                            araragiayane.sendMessage(to, "Berhasil menyingkirkan para pidana")
                elif text.lower() == 'killbanall':
                    gid = araragiayane.getGroupIdsJoined()
                    group = araragiayane.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        araragiayane.sendMessage(to, "Kosong")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                araragiayane.kickoutFromGroup(i, [jj])
                            araragiayane.sendMessage(i, "Berhasil menyingkirkan para pidana di semua group")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        araragiayane.sendMessage(to, "Silahakan masukan ID group target")
                    else:
                        try:
                            araragiayane.findAndAddContactsByMid(msg._from)
                            araragiayane.inviteIntoGroup(gid,[msg._from])
                        except:
                            araragiayane.sendMessage(to, "Eror 404")
                elif msg.text in ["Friendlist"]:
                    anl = araragiayane.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+araragiayane.getContact(q).displayName + "\n"
                    araragiayane.sendMessage(msg.to,"「 Daftar 」\n"+ap+"Nomor : "+str(len(anl)))
                elif text.lower() == 'sp':
                    start = time.time()
                    araragiayane.sendMessage(to, "Sedang Memproses...")
                    elapsed_time = (time.time() - start)/1000
                    araragiayane.sendMessage(to,format(str(elapsed_time)) + " mili/detik")
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    araragiayane.sendMessage(to,'Speeds up the system \n' + str1 + ' Seconds')
                    elapsed_time = time.time() - start
                    araragiayane.sendMessage(to,'Commands Reaction \n' + format(str(elapsed_time)) + ' Seconds')
                elif text.lower() == 'rebot':
                    araragiayane.sendMessage(to, "Proses Restart dikerjakan...")
                    time.sleep(5)
                    araragiayane.sendMessage(to, "Program berhasil di restart")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    araragiayane.sendMessage(to, "Program Processing {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u9cdc29cb1452168cadae627171b7a6ee"
                        creator = araragiayane.getContact(owner)
                        contact = araragiayane.getContact(araragiayaneMID)
                        grouplist = araragiayane.getGroupIdsJoined()
                        contactlist = araragiayane.getAllContactIds()
                        blockedlist = araragiayane.getBlockedContactIds()
                        ret_ = "╔══[ About Self ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Beta Test"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ ༈⃟🛡️⃟🛡️⃟࿖₳ŗᎯ℟ăᏭᎥ࿖⃟🛡️⃟🛡️⃟༈ ]"
                        araragiayane.sendMessage(to, str(ret_))
                    except Exception as e:
                        araragiayane.sendMessage(msg.to, str(e))
                        
#________________________________________________________________________________________________________________#                        
                        
                elif text.lower() == 'set':
                    try:
                        ret_ = "[ STATUS ]"
                        if settings["autoAdd"] == True: ret_ += "\nAutoAdders ✅"
                        else: ret_ += "\nAutoAdders salah ❌"
                        if settings["autoJoin"] == True: ret_ += "\nAuto Joined ✅"
                        else: ret_ += "\nAuto Joined ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\nJoined ticktet ✅"
                        else: ret_ += "\nJoined ticktet ❌"
                        if settings["autoLeave"] == True: ret_ += "\nAuto leave group ✅"
                        else: ret_ += "\nAuto leave group ❌"
                        if settings["autoRead"] == True: ret_ += "\nRead messages ✅"
                        else: ret_ += "\nRead messages ❌"
                        if settings["protect"] == True: ret_ += "\nProtected ✅"
                        else: ret_ += "\nProtected ❌"
                        if settings["inviteprotect"] == True: ret_ += "\nProtect Invit ✅"
                        else: ret_ += "\nProtect Invite ❌"
                        if settings["qrprotect"] == True: ret_ += "\nQr Protection ✅"
                        else: ret_ += "\nQr Protection ❌"
                        if settings["contact"] == True: ret_ += "\nKontack ✅"
                        else: ret_ += "\nKontak ❌"
                        if settings["reread"] == True: ret_ += "\nUnsend Message ✅"
                        else: ret_ += "\nUnsend Messages ❌"
                        if settings["detectMention"] == False: ret_ += "\nDetect Mention ✅"
                        else: ret_ += "\nDetect mention ❌"
                        if settings["checkSticker"] == True: ret_ += "\nCheck Stikers ✅"
                        else: ret_ += "\nCheck stikers ❌"
                        if settings["kickContact"] == True: ret_ += "\nKick kontak ✅"
                        else: ret_ += "\nKick kontak ❌"
                        if settings["autoPtt"] == True: ret_ += "\nAutomatically Ptt ✅"
                        else: ret_ += "\nAutomatically Ptt ❌"
                        araragiayane.sendMessage(to, str(ret_))
                    except Exception as e:
                        araragiayane.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    araragiayane.sendMessage(to, "System Auto add di hidupkan ")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    araragiayane.sendMessage(to, "System auto add di matikan")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    araragiayane.sendMessage(to, "System join otomatis di hidupkan")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    araragiayane.sendMessage(to, "System joim otomatis di matikan")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    araragiayane.sendMessage(to, "System Otomatis leave di hidupkan")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    araragiayane.sendMessage(to, "System otomatis leave di matikan")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    araragiayane.sendMessage(to, "System Cek kontak di hidupkan")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    araragiayane.sendMessage(to, "System cek kontak di matikan")
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    araragiayane.sendMessage(to, "System protection group di hidupkan")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    araragiayane.sendMessage(to, "System Protection group di matikan")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    araragiayane.sendMessage(to, "System Protect invite di hidupkan")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    araragiayane.sendMessage(to, "System Protect invite di matikan ")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    araragiayane.sendMessage(to, "System Protect qr di hidupkan")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    araragiayane.sendMessage(to, "System protect qr di matikan")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    araragiayane.sendMessage(to, "System unsend di hidupkan")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    araragiayane.sendMessage(to, "System unsend di matikan")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    araragiayane.sendMessage(to, "System otomatis read di hidupkan")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    araragiayane.sendMessage(to, "System otomatis read di matikan")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    araragiayane.sendMessage(to, "System join otomatis via qr di hidupkan")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    araragiayane.sendMessage(to, "System join otomatis via qr di matikan")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = False
                    araragiayane.sendMessage(to, "System respon summon di hidupkan")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = True
                    araragiayane.sendMessage(to, "System respon summon di matikan")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    araragiayane.sendMessage(to, "System Check stikers di hidupkan")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    araragiayane.sendMessage(to, "System check stikers di matikan")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    araragiayane.sendMessage(to, "System kick kontak di hidupkan")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    araragiayane.sendMessage(to, "")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    araragiayane.sendMessage(to, "System leave otomatis di hidupkan")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    araragiayane.sendMessage(to, "System leave otomatis di matikan")
                    
#________________________________________________________________________________________________________________#                    
                    
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    araragiayane.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    araragiayane.sendMessage(msg.to,"" +  sender)
                elif text.lower() == 'myname':
                    me = araragiayane.getContact(sender)
                    araragiayane.sendMessage(msg.to,"" + me.displayName)
                elif text.lower() == 'mybio':
                    me = araragiayane.getContact(sender)
                    araragiayane.sendMessage(msg.to,"" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = araragiayane.getContact(sender)
                    araragiayane.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = araragiayane.getContact(sender)
                    cover = araragiayane.getProfileCoverURL(sender)
                    araragiayane.sendImageWithURL(msg.to, cover)
                elif text.lower() == 'removeallchat':
                    araragiayane.removeAllMessages(op.param2)
                    araragiayane.sendMessage(to, "Berhasil hapus semua chat")    
                    
#________________________________________________________________________________________________________________#                    
                    
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = araragiayane.getContact(ls)
                            mi_d = contact.mid
                            araragiayane.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        araragiayane.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = araragiayane.getContact(ls)
                            araragiayane.sendMessage(msg.to, "" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = araragiayane.getContact(ls)
                            araragiayane.sendMessage(msg.to, "" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + araragiayane.getContact(ls).pictureStatus
                            araragiayane.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("mpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + araragiayane.getContact(ls).pictureStatus
                            araragiayane.sendVideoWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = araragiayane.getProfileCoverURL(ls)
                                araragiayane.sendImageWithURL(msg.to, str(path))
                                
#________________________________________________________________________________________________________________#                                
                                
                elif text.lower() == 'gowner':
                    group = araragiayane.getGroup(to)
                    GS = group.creator.mid
                    araragiayane.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = araragiayane.getGroup(to)
                    araragiayane.sendMessage(to, "[ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = araragiayane.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = araragiayane.reissueGroupTicket(to)
                            araragiayane.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            araragiayane.sendMessage(to, "Silahkan Buka Url terlebih dahulu".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = araragiayane.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            araragiayane.sendMessage(to, "Url group sudah di aktifkan")
                        else:
                            G.preventedJoinByTicket = False
                            araragiayane.updateGroup(G)
                            araragiayane.sendMessage(to, "Berhasil mengaktifkan url group oleh system")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = araragiayane.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            araragiayane.sendMessage(to, "Url group sudah di Nonaktifkan")
                        else:
                            G.preventedJoinByTicket = True
                            araragiayane.updateGroup(G)
                            araragiayane.sendMessage(to, "Berhasil menonaktifkan url group oleh system")
                elif text.lower() == 'ginfo':
                    group = araragiayane.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak Di kenal"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Open"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragiayane.reissueGroupTicket(group.id)))
                    else:
                        gQr = "Close"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(araragiayane.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    araragiayane.sendMessage(to, str(ret_))
                    araragiayane.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = araragiayane.getGroup(to)
                        ret_ = "[Daftar anggota]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[Total： {} Ekor]".format(str(len(group.members)))
                        araragiayane.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = araragiayane.groups
                        ret_ = "[Daftar Group]"
                        no = 0 + 1
                        for gid in groups:
                            group = araragiayane.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[Total {} group]".format(str(len(groups)))
                        araragiayane.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = araragiayane.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        araragiayane.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'sn':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                araragiayane.sendMessage(msg.to,"Sider siap untuk di cyduk 􀨁􀇝looking right􏿿")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            araragiayane.sendMessage(msg.to, "Setel Titik baca:\n" + readTime)
                elif text.lower() == 'sf':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        araragiayane.sendMessage(msg.to,"Titik baca telah di tutup")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        araragiayane.sendMessage(msg.to, "Berhasil di setting ulang :\n" + readTime)
                elif text.lower() == 'sr':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        araragiayane.sendMessage(msg.to, "Setel ulang point baca:\n" + readTime)
                    else:
                        araragiayane.sendMessage(msg.to, "Titik baca di atur")
                elif text.lower() == 'r':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            araragiayane.sendMessage(receiver,"[ sider ]:\n")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = araragiayane.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Sider ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Waktu ]: \n" + readTime
                        try:
                            araragiayane.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        araragiayane.sendMessage(receiver,"Atur titik baca njerrr..")
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        araragiayane.log("[%s]"%(msg._from)+msg.text)
                    else:
                        araragiayane.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            araragiayane.sendMessage(at,"[Terpidana unsend messaging]\n%s\n[Messages]\n%s"%(araragiayane.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["Ingat Pesan"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != araragiayane.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    araragiayane.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in araragiayaneMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if araragiayaneMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = araragiayane.getContact(sender)
                                    araragiayane.sendMessage(to, "Ngapain summon gw sih ?? Sok kenal aja luuh")
                                break
        if op.type == 55:
            print ("[ 55 ] Reader")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
