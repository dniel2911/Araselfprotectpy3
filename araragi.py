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
araragiayane = LINE()
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
admin=['u9cdc29cb1452168cadae627171b7a6ee','u6b8aa4b01a80fba3649facb2d5e02c6e','u46915e425cf18d6cbf9391214f6ae02d','u67505d68093db806a1cf5a488d277671',araragiayaneMID]
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
    print ("[ Bot ] Restart")
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
    araragiayane.log("[ Eror ] " + str(text))
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
    helpMessage = """╭─────────────────
│├﴾༈⃟🛡️⃟🛡️⃟࿖₳ŗᎯ℟ăᏭᎥ࿖⃟🛡️⃟🛡️⃟༈﴿
│├─────────────────
││࿐【.help】
│├࿐【.HelpTag】
││࿐【.HelpKick】
│├─────────────────
│├﴾Araragi bot﴿
│├─────────────────
││࿐【.rebot】
│├࿐【.runtime】
│├࿐【.speed】
│├࿐【.set】
│├࿐【.about】
││࿐【.creator】
│├─────────────────
│├﴾Araragi Sett﴿
│├─────────────────
││࿐【.add On/Off】
│├࿐【.join On/Off】
│├࿐【.leave On/Off】
│├࿐【.read On/Off】
│├࿐【.inviteprotect】
│├࿐【.reread On/Off】
│├࿐【.qr On/Off】
│├࿐【.qrjoin On/Off】
│├࿐【.ck On/Off】
│├࿐【.groupprotect】
│├࿐【.kc On/Off】
││࿐【.ptt On/Off】
│├─────────────────
│├﴾Araragi self﴿
│├─────────────────
││࿐【.me】
│├࿐【.myMid】
│├࿐【.myName】
│├࿐【.myBio】
│├࿐【.myPicture】
│├࿐【.myCover】
│├࿐【.contact @】
│├࿐【.mid @】
│├࿐【.name @】
│├࿐【.bio @】
│├࿐【.picture @】
│├࿐【.cover @】
││࿐【.friendlist】
│├─────────────────
│├﴾Araragi Group﴿
│├─────────────────
││࿐【.gowner】
│├࿐【.gurl】
│├࿐【.o/Curl】
│├࿐【.lg】
│├࿐【.gb】
│├࿐【.ginfo】
│├࿐【.ri @】
│├࿐【.ri:mid】
│├࿐【.tk @】
│├࿐【.mk @】
│├࿐【.vk @】
│├࿐【.vk:mid】
│├࿐【.nk Name】
│├࿐【.Kickall】
│├࿐【.Uk mid】
│├࿐【.NT Name】
│├࿐【.zk】
│├࿐【.zt】
│├࿐【.zm】
│├࿐【.cancel】
│├࿐【.gcancel】
│├࿐【.gn Name】
│├࿐【.gc @】
│├࿐【.inv mid】
│├࿐【.ban @】
│├࿐【.unban @】
│├࿐【.mb:mid】
│├࿐【.mub:mid】
│├࿐【.clear Ban】
│├࿐【.kill Ban】
│├࿐【.killbanall】
│├࿐【.Zk】
│├࿐【.banlist】
│├࿐【.sc gid】
││࿐【.mc mid】
│├─────────────────
│├﴾Araragi owner﴿
│├─────────────────
││࿐【.tagall】
│├࿐【.sr/DR】
│├࿐【.lr】
│├࿐【.F/Gbc】
│├࿐【/invitemeto:】
│├࿐【.op @】
│├࿐【.deop @】
│├࿐【.mop:mid】
│├࿐【.mdp:mid】
│├࿐【.opmid】
││࿐【.oplist】
╰─────────────────"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""╭─────────────────
├﴾༈⃟🛡️⃟🛡️⃟࿖₳ŗᎯ℟ăᏭᎥ࿖⃟🛡️⃟🛡️⃟༈﴿
├─────────────────
│╭࿐【.ri @】
│├࿐【.tk @】
│├࿐【.mk @】
│├࿐【.vk @】
│├࿐【.gc @】
│├࿐【.mid @
│├࿐【.name @】
│├࿐【.Bio @】
│├࿐【.Picture @】
│├࿐【.Cover @】
│├࿐【.ban @】
│╰࿐【.unban @】
╰─────────────────"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""╭─────────────────
├﴾༈⃟🛡️⃟🛡️⃟࿖₳ŗᎯ℟ăᏭᎥ࿖⃟🛡️⃟🛡️⃟༈﴿
├─────────────────
│╭࿐【.ri  @】
│├࿐【.tk @】
│├࿐【.mk @】
│├࿐【.vk @】
│├࿐【.vk:mid】
│├࿐【.nk Name】
│├࿐【.uk mid】
│├࿐【.kill ban】
│╰࿐【.zk】
╰─────────────────"""
    return helpMessageKick
    
    
    
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#


def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = araragiayane.getContact(op.param1)
            print ("[ 5 ] Add Contact: " + contact.displayName)
            if settings["autoAdd"] == True:
                araragiayane.findAndAddContactsByMid(op.param1)
                araragiayane.sendMessage(op.param1, "cie kakak diem diem add aku ya 😉{}\nSalam kenal ya kaka semoga betah di belahan hatiku 🤣".format(str(contact.displayName)))
                araragiayane.sendMessage(op.param1, "jangan takut sama tuan kami araragi 😳 ^^")
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
                    araragiayane.sendMessage(op.param1,araragiayane.getContact(op.param2).displayName + "Jangan mainin group gw kutil babi ！")
                    araragiayane.kickoutFromGroup(op.param1,[op.param2])
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
            if araragiayaneMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('Group siapa nih 😲')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "Numpang nama 👌 \nMasih jomblo aje lu pada 🐣 ..."
                        araragiayane.acceptGroupInvitation(op.param1)
                        araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        araragiayane.sendMessage(op.param1, "Created ：")
                        araragiayane.sendContact(op.param1, "u0f26401bbba4a99eff1412a1ac27b213")
                    except Exception as error:
                        print(error)
            if araragiayaneMID in op.param3:
                if settings["autoPtt"] == True:
                    araragiayane.acceptGroupInvitation(op.param1)
                    araragiayane.sendMessage(op.param1, "Group siapa nih njer 😲\n Ijin lewat doang  ")
                    araragiayane.leaveGroup(op.param1)
        if op.type == 15:
            contact1 = araragiayane.getContact(op.param2)
            group = araragiayane.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('Dih ada yang baper 💀 ')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Semoga betah di alam sana 🐣 {}".format(str(group.name))
                    araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = araragiayane.getContact(op.param2)
            group = araragiayane.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('Welcome kakak ')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "Selamat datang di {} jangan lupa cek note ya nyet！".format(str(group.name))
                    araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = araragiayane.getContact(op.param2)
            group = araragiayane.getGroup(op.param1)
            contact2 = araragiayane.getContact(op.param3)
            print ("[19] Kick out from group: " + str(group.name) + "\n" + op.param1 +"\nNama: " + contact1.displayName + "\nMid:" + contact1.mid + "\nNama: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('Dangger! ')
                            arr = []
                            mention1 = "@arasi "
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
                        text = "%s " %('Dangger!! ')
                        arr = []
                        mention1 = "@arasi "
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
                        araragiayane.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                else:
                    pass
        if op.type == 22:
            print ("[ 22 ] Leave group")
            if settings["autoLeave"] == True:
                araragiayane.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1] Notice file Konfigurasi ")
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
                    ret_ += "\nID : {}".format(stk_id)
                    ret_ += "\nID : {}".format(pkg_id)
                    ret_ += "\nUrlPic: line://shop/detail/{}".format(pkg_id)
                    ret_ += "\nWeb：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n[ END ]"
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
                        araragiayane.sendMessage(msg.to,"[Nama]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Bio]:\n" + contact.statusMessage + "\n[Url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[Cover]:\n" + str(cu))
                    else:
                        contact = araragiayane.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = araragiayane.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        araragiayane.sendMessage(msg.to,"[Nama]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[Bio]:\n" + contact.statusMessage + "\n[Url]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[Cover]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s\n%s\n"%("---[Share Post]---","[Created]:")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[Keterangan]:\n" + msg.contentMetadata["text"] + "\n(Hanya dapat menamlilkan 100 karakter)" + "\n[Url]:\n" + msg.contentMetadata["postEndUrl"]
                            araragiayane.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "---[Share Post]---\n[Created]:\n" + msg.contentMetadata["text"] + "\n(Hanya dapat menampilkan 100 karakter )"
                        ret_ += "\n[Ingat Pesan]:\n" + msg.contentMetadata["postEndUrl"]
                        araragiayane.sendMessage(msg.to, str(ret_))
                        
                        
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#


            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if msg.text in [".help"]:
                    helpMessage = helpmessage()
                    araragiayane.sendMessage(to, str(helpMessage))
                    araragiayane.sendMessage(to, "My Creator:")
                    araragiayane.sendContact(to, "u9cdc29cb1452168cadae627171b7a6ee")
                elif text.lower() == '.helptag':
                    helpMessageTag = helpmessagetag()
                    araragiayane.sendMessage(to, str(helpMessageTag))
                elif text.lower() == '.helpkick':
                    helpMessageKick = helpmessagekick()
                    araragiayane.sendMessage(to, str(helpMessageKick))
                elif text.lower() == '.creator':
                    araragiayane.sendMessage(to, "My Creator:")
                    araragiayane.sendContact(to, "u9cdc29cb1452168cadae627171b7a6ee")
                elif ".fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = araragiayane.getAllContactIds()
                    for manusia in t:
                        araragiayane.sendMessage(manusia,(bctxt))
                elif ".gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = araragiayane.getGroupIdsJoined()
                    for manusia in n:
                        araragiayane.sendMessage(manusia,(bctxt))
                elif ".Ri " in msg.text:
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
                elif ".ri:" in msg.text:
                    midd = text.replace("Ri:","")
                    araragiayane.kickoutFromGroup(to,[midd])
                    araragiayane.findAndAddContactsByMid(midd)
                elif ".uk " in msg.text:
                    midd = text.replace("Uk ","")
                    araragiayane.kickoutFromGroup(to,[midd])
                elif ".tk " in msg.text:
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
                elif ".mk " in msg.text:
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
                elif ".nk " in msg.text:
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
                elif ".kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = araragiayane.getGroup(to)
                            araragiayane.sendMessage(to, "Please Maaaf numpang lewat jangan baper ya kakak")
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
                elif ".zk" in msg.text:
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
                elif ".vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    araragiayane.kickoutFromGroup(msg.to,[midd])
                    araragiayane.findAndAddContactsByMid(midd)
                    araragiayane.inviteIntoGroup(msg.to,[midd])
                    araragiayane.cancelGroupInvitation(msg.to,[midd])
                elif ".vk " in msg.text:
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
                elif ".nt " in msg.text:
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
                elif text.lower() == '.zt':
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
                elif text.lower() == '.zm':
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
                        
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
                        
                elif ".mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    araragiayane.sendContact(to, mmid)
                elif ".sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = araragiayane.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak di kenal "
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
                    ret_ = "[INFO GROUP]"
                    ret_ += "\nNama : {}".format(str(group.name))
                    ret_ += "\IＤ : {}".format(group.id)
                    ret_ += "\nCreator : {}".format(str(gCreator))
                    ret_ += "\nMembers : {}".format(str(len(group.members)))
                    ret_ += "\nPending : {}".format(gPending)
                    ret_ += "\nUrl : {}".format(gQr)
                    ret_ += "\nTicket: {}".format(gTicket)
                    ret_ += "\n[END INFO]"
                    araragiayane.sendMessage(to, str(ret_))
                    araragiayane.sendImageWithURL(to, path)
                elif msg.text in [".c",".C",".cancel",".Cancel"]:
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
                        araragiayane.sendMessage(to, "Tidak Ada pendingan ！！")
                elif text.lower() == '.gcancel':
                    gid = araragiayane.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        araragiayane.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    araragiayane.sendMessage(to, "Semua undangan di batalkan")
                    araragiayane.sendMessage(to, "Waktu: %s Second" % (elapsed_time))
                elif ".gn " in msg.text:
                    if msg.toType == 2:
                        X = araragiayane.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        araragiayane.updateGroup(X)
                    else:
                        araragiayane.sendMessage(msg.to,"Hanya dapat di gunakan di group")
                elif text.lower().startswith('.op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        araragiayane.sendMessage(to, "Daftar Admim berhasil Di tambahkan")
                elif text.lower().startswith('.deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        araragiayane.sendMessage(to, "Target telah di hapus dari daftar Admin")
                elif text.lower().startswith('.mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        araragiayane.sendMessage(to, "Target Telah di tambahkan dalam daftar admin") 
                        backupData()
                elif text.lower().startswith('.mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        araragiayane.sendMessage(to, "Target Telah di hapus dari daftar Admin！") 
                        backupData()
                elif text.lower() == '.opmid':
                    if admin == []:
                        araragiayane.sendMessage(to, "Tidak Ada admin")
                    else:
                        mc = "Daftar admin："
                        for mi_d in admin:
                            mc += "\✅ " + mi_d
                        araragiayane.sendMessage(to, mc)
                elif text.lower() == '.oplist':
                    if admin == []:
                        araragiayane.sendMessage(to, "Tidak ada admin")
                    else:
                        mc = "Daftar Admin："
                        for mi_d in admin:
                            mc += "\n✅ " + araragiayane.getContact(mi_d).displayName
                        araragiayane.sendMessage(to, mc)
                elif ".gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = araragiayane.getContact(u)
                        cu = araragiayane.getProfileCoverURL(mid=u)
                        try:
                            araragiayane.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nBio:\n" + contact.statusMessage + "\n\nUrl :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nSampul :\n" + str(cu))
                        except:
                            araragiayane.sendMessage(msg.to,"Nama:\n" + contact.displayName + "\n\nMid:\n" + contact.mid + "\n\nBio:\n" + contact.statusMessage + "\n\nSampul:\n" + str(cu))
                elif ".inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    araragiayane.findAndAddContactsByMid(midd)
                    araragiayane.inviteIntoGroup(msg.to,[midd])
                elif ".ban" in msg.text:
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
                                    araragiayane.sendMessage(to, "Target di masukan dalam blacklist")
                                except:
                                    pass
                elif ".unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
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
                                    araragiayane.sendMessage(to, "Target di lepaskan dalam blackist")
                                except:
                                    pass
                elif ".mb:" in msg.text:
                    midd = msg.text.replace("Mb:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        araragiayane.sendMessage(to, "Target Ditambahkan dalam daftar blacklist")
                    except:
                        pass
                elif ".mub:" in msg.text:
                    midd = msg.text.replace("Mub:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        araragiayane.sendMessage(to, "Target telah di hapus dari daftar blacklist")
                    except:
                        pass
                elif text.lower() == '.clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    araragiayane.sendMessage(to, "Dartar blacklist berhasil di bersihkan")
                elif text.lower() == '.banlist':
                    if settings["blacklist"] == {}:
                        araragiayane.sendMessage(to, "Tidak Ada")
                    else:
                        mc = "Daftar Balcklist："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + araragiayane.getContact(mi_d).displayName
                        araragiayane.sendMessage(to, mc)
                elif text.lower() == '.banmid':
                    if settings["blacklist"] == {}:
                        araragiayane.sendMessage(to, "Tidak ada")
                    else:
                        mc = "Daftar mid dalam blacklist："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + mi_d
                        araragiayane.sendMessage(to, mc)
                elif text.lower() == '.kill ban':
                    if msg.toType == 2:
                        group = araragiayane.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            araragiayane.sendMessage(to, "Kosong")
                            return
                        for jj in matched_list:
                            araragiayane.kickoutFromGroup(to, [jj])
                            araragiayane.sendMessage(to, "Daftar blacklist berhasil di singkirkan")
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
                            araragiayane.sendMessage(i, "Daftar blacklist di singkirkan dari semua group")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        araragiayane.sendMessage(to, "Silahkan masukan ID")
                    else:
                        try:
                            araragiayane.findAndAddContactsByMid(msg._from)
                            araragiayane.inviteIntoGroup(gid,[msg._from])
                        except:
                            araragiayane.sendMessage(to, "Eror 404")
                elif msg.text in [".friendlist"]:
                    anl = araragiayane.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+araragiayane.getContact(q).displayName + "\n"
                    araragiayane.sendMessage(msg.to,"「 Daftar 」\n"+ap+"Nomor : "+str(len(anl)))
                    
                    
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#


                elif text.lower() == '.sp':
                    start = time.time()
                    araragiayane.sendMessage(to, "Sedang di proses...")
                    elapsed_time = (time.time() - start)/100
                    araragiayane.sendMessage(to,format(str(elapsed_time)) + " Seconds")
                elif text.lower() == '.speed':
                    start = time.time()
                    araragiayane.sendMessage(to, "Sedang di proses...")
                    elapsed_time = (time.time() - start)/100
                    araragiayane.sendMessage(to,format(str(elapsed_time)) + " Seconds")
                elif text.lower() == '.rebot':
                    araragiayane.sendMessage(to, "System Reset.. ")
                    time.sleep(5)
                    araragiayane.sendMessage(to, "Program berhasil di Restart ")
                    restartBot()
                elif text.lower() == '.runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    araragiayane.sendMessage(to, "System bekerja selama {}".format(str(runtime)))
                elif text.lower() == '.about':
                    try:
                        arr = []
                        owner = "u0f26401bbba4a99eff1412a1ac27b213"
                        creator = araragiayane.getContact(owner)
                        contact = araragiayane.getContact(araragiayaneMID)
                        grouplist = araragiayane.getGroupIdsJoined()
                        contactlist = araragiayane.getAllContactIds()
                        blockedlist = araragiayane.getBlockedContactIds()
                        ret_ = "[INFO] "
                        ret_ += "\nNama : {}".format(contact.displayName)
                        ret_ += "\nGroupList : {}".format(str(len(grouplist)))
                        ret_ += "\nContact : {}".format(str(len(contactlist)))
                        ret_ += "\nBlock : {}".format(str(len(blockedlist)))
                        ret_ += "\n《Tentang》"
                        ret_ += "\nBot : Araragi v3"
                        ret_ += "\nCreator: {}".format(creator.displayName)
                        ret_ += "\n[END INFO] "
                        araragiayane.sendMessage(to, str(ret_))
                    except Exception as e:
                        araragiayane.sendMessage(msg.to, str(e))
                elif text.lower() == '.set':
                    try:
                        ret_ = "[ STATUS ]"
                        if settings["autoAdd"] == True: ret_ += "\nAutoAdders ✔"
                        else: ret_ += "\nAutoAdders ✘"
                        if settings["autoJoin"] == True: ret_ += "\nAuto Joined ✔"
                        else: ret_ += "\nAuto Joined ✘"
                        if settings["autoJoinTicket"] == True: ret_ += "\nJoined ticktet ✔"
                        else: ret_ += "\nJoined ticktet ✘"
                        if settings["autoLeave"] == True: ret_ += "\nAuto leave group ✔"
                        else: ret_ += "\nAuto leave group ✘"
                        if settings["autoRead"] == True: ret_ += "\nRead messages ✔"
                        else: ret_ += "\nRead messages ✘"
                        if settings["protect"] == True: ret_ += "\nProtected ✔"
                        else: ret_ += "\nProtected ✘"
                        if settings["inviteprotect"] == True: ret_ += "\nProtect Invit ✔"
                        else: ret_ += "\nProtect Invite ✘"
                        if settings["qrprotect"] == True: ret_ += "\nQr Protection ✔"
                        else: ret_ += "\nQr Protection ✘"
                        if settings["contact"] == True: ret_ += "\nKontack ✔"
                        else: ret_ += "\nKontak ✘"
                        if settings["reread"] == True: ret_ += "\nUnsend Message ✔"
                        else: ret_ += "\nUnsend Messages ✘"
                        if settings["detectMention"] == False: ret_ += "\nDetect Mention ✔"
                        else: ret_ += "\nDetect mention ✘"
                        if settings["checkSticker"] == True: ret_ += "\nCheck Stikers ✔"
                        else: ret_ += "\nCheck stikers ✘"
                        if settings["kickContact"] == True: ret_ += "\nKick kontak ✔"
                        else: ret_ += "\nKick kontak ✘"
                        if settings["autoPtt"] == True: ret_ += "\nAutomatically Ptt✔"
                        else: ret_ += "\nAutomatically Ptt ✘"
                        araragiayane.sendMessage(to, str(ret_))
                    except Exception as e:
                        araragiayane.sendMessage(msg.to, str(e))
                elif text.lower() == '.add on':
                    settings["autoAdd"] = True
                    araragiayane.sendMessage(to, "System Auto add di hidupkan ")
                elif text.lower() == '.add off':
                    settings["autoAdd"] = False
                    araragiayane.sendMessage(to, "System auto add di matikan")
                elif text.lower() == '.join on':
                    settings["autoJoin"] = True
                    araragiayane.sendMessage(to, "System join otomatis di hidupkan")
                elif text.lower() == '.join off':
                    settings["autoJoin"] = False
                    araragiayane.sendMessage(to, "System joim otomatis di matikan")
                elif text.lower() == '.leave on':
                    settings["autoLeave"] = True
                    araragiayane.sendMessage(to, "System Otomatis leave di hidupkan")
                elif text.lower() == '.leave off':
                    settings["autoLeave"] = False
                    araragiayane.sendMessage(to, "System otomatis leave di matikan")
                elif text.lower() == '.contact on':
                    settings["contact"] = True
                    araragiayane.sendMessage(to, "System Cek kontak di hidupkan")
                elif text.lower() == '.contact off':
                    settings["contact"] = False
                    araragiayane.sendMessage(to, "System cek kontak di matikan")
                elif text.lower() == '.groupprotect on':
                    settings["protect"] = True
                    araragiayane.sendMessage(to, "System protection group di hidupkan")
                elif text.lower() == '.groupprotect off':
                    settings["protect"] = False
                    araragiayane.sendMessage(to, "System Protection group di matikan")
                elif text.lower() == '.inviteprotect on':
                    settings["inviteprotect"] = True
                    araragiayane.sendMessage(to, "System Protect invite di hidupkan")
                elif text.lower() == '.inviteprotect off':
                    settings["inviteprotect"] = False
                    araragiayane.sendMessage(to, "System Protect invite di matikan ")
                elif text.lower() == '.qr on':
                    settings["qrprotect"] = True
                    araragiayane.sendMessage(to, "System Protect qr di hidupkan")
                elif text.lower() == '.qr off':
                    settings["qrprotect"] = False
                    araragiayane.sendMessage(to, "System protect qr di matikan")
                elif text.lower() == '.reread on':
                    settings["reread"] = True
                    araragiayane.sendMessage(to, "System unsend di hidupkan")
                elif text.lower() == '.reread off':
                    settings["reread"] = False
                    araragiayane.sendMessage(to, "System unsend di matikan")
                elif text.lower() == '.read on':
                    settings["autoRead"] = True
                    araragiayane.sendMessage(to, "System otomatis read di hidupkan")
                elif text.lower() == '.read off':
                    settings["autoRead"] = False
                    araragiayane.sendMessage(to, "System otomatis read di matikan")
                elif text.lower() == '.qrjoin on':
                    settings["autoJoinTicket"] = True
                    araragiayane.sendMessage(to, "System join otomatis via qr di hidupkan")
                elif text.lower() == '.qrjoin off':
                    settings["autoJoinTicket"] = False
                    araragiayane.sendMessage(to, "System join otomatis via qr di matikan")
                elif text.lower() == '.tag on':
                    settings["detectMention"] = False
                    araragiayane.sendMessage(to, "System respon summon di hidupkan")
                elif text.lower() == '.tag off':
                    settings["detectMention"] = True
                    araragiayane.sendMessage(to, "System respon summon di matikan")
                elif text.lower() == '.ck on':
                    settings["checkSticker"] = True
                    araragiayane.sendMessage(to, "System Check stikers di hidupkan")
                elif text.lower() == '.ck off':
                    settings["checkSticker"] = False
                    araragiayane.sendMessage(to, "System check stikers di matikan")
                elif text.lower() == '.kc on':
                    settings["kickContact"] = True
                    araragiayane.sendMessage(to, "System kick kontak di hidupkan")
                elif text.lower() == '.kc off':
                    settings["kickContact"] = False
                    araragiayane.sendMessage(to, "")
                elif text.lower() == '.ptt on':
                    settings["autoPtt"] = True
                    araragiayane.sendMessage(to, "System leave otomatis di hidupkan")
                elif text.lower() == '.ptt off':
                    settings["autoPtt"] = False
                    araragiayane.sendMessage(to, "System leave otomatis di matikan")
                elif text.lower() == '.me':
                    sendMessageWithMention(to, sender)
                    araragiayane.sendContact(to, sender)
                elif text.lower() == '.mymid':
                    araragiayane.sendMessage(msg.to,"" +  sender)
                elif text.lower() == '.myname':
                    me = araragiayane.getContact(sender)
                    araragiayane.sendMessage(msg.to,"" + me.displayName)
                elif text.lower() == '.mybio':
                    me = araragiayane.getContact(sender)
                    araragiayane.sendMessage(msg.to,"[Bio]: " + me.statusMessage)
                elif text.lower() == '.mypicture':
                    me = araragiayane.getContact(sender)
                    araragiayane.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == '.mycover':
                    me = araragiayane.getContact(sender)
                    cover = araragiayane.getProfileCoverURL(sender)
                    araragiayane.sendImageWithURL(msg.to, cover)
                    
                    
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#


                elif msg.text.lower().startswith(".contact "):
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
                elif msg.text.lower().startswith(".mid "):
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
                elif msg.text.lower().startswith(".name "):
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
                elif msg.text.lower().startswith(".bio "):
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
                            araragiayane.sendMessage(msg.to, "[ Bio ]\n" + contact.statusMessage)
                elif msg.text.lower().startswith(".picture "):
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
                elif msg.text.lower().startswith(".mpicture "):
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
                elif msg.text.lower().startswith(".cover "):
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
                elif text.lower() == '.gowner':
                    group = araragiayane.getGroup(to)
                    GS = group.creator.mid
                    araragiayane.sendContact(to, GS)
                elif text.lower() == '.gid':
                    gid = araragiayane.getGroup(to)
                    araragiayane.sendMessage(to, "[ID : ]\n" + gid.id)
                elif text.lower() == '.gurl':
                    if msg.toType == 2:
                        group = araragiayane.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = araragiayane.reissueGroupTicket(to)
                            araragiayane.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            araragiayane.sendMessage(to, "Silahakn buka url dahulu".format(str(settings["keyCommand"])))
                elif text.lower() == '.ourl':
                    if msg.toType == 2: 
                        G = araragiayane.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            araragiayane.sendMessage(to, "Url group sudah di aktifkan")
                        else:
                            G.preventedJoinByTicket = False
                            araragiayane.updateGroup(G)
                            araragiayane.sendMessage(to, "Berhasil mengaktifkan url group oleh system")
                elif text.lower() == '.curl':
                    if msg.toType == 2:
                        G = araragiayane.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            araragiayane.sendMessage(to, "Url group sudah di Nonaktifkan")
                        else:
                            G.preventedJoinByTicket = True
                            araragiayane.updateGroup(G)
                            araragiayane.sendMessage(to, "Berhasil menonaktifkan url group oleh system")
                elif text.lower() == '.curl':
                    if msg.toType == 2:
                        G = araragiayane.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            araragiayane.sendMessage(to, "Url group sudah di Nonaktifkan")
                        else:
                            G.preventedJoinByTicket = True
                            araragiayane.updateGroup(G)
                            araragiayane.sendMessage(to, "Berhasil menonaktifkan url group oleh system")
                elif text.lower() == '.ginfo':
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
                    ret_ = " Info "
                    ret_ += "\nNama       : {}".format(str(group.name))
                    ret_ += "\nId group   : {}".format(group.id)
                    ret_ += "\nCreator    : {}".format(str(gCreator))
                    ret_ += "\nMember     : {}".format(str(len(group.members)))
                    ret_ += "\nPending    : {}".format(gPending)
                    ret_ += "\nUrl        : {}".format(gQr)
                    ret_ += "\nTicket     : {}".format(gTicket)
                    ret_ += "\nInfo End"
                    araragiayane.sendMessage(to, str(ret_))
                    araragiayane.sendImageWithURL(to, path)
                elif text.lower() == '.gb':
                    if msg.toType == 2:
                        group = araragiayane.getGroup(to)
                        ret_ = "[Daftar anggota]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[Total： {} Ekor]".format(str(len(group.members)))
                        araragiayane.sendMessage(to, str(ret_))
                elif text.lower() == '.lg':
                        groups = araragiayane.groups
                        ret_ = "[Daftar Group]"
                        no = 0 + 1
                        for gid in groups:
                            group = araragiayane.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[Total {} group]".format(str(len(groups)))
                        araragiayane.sendMessage(to, str(ret_))
                elif text.lower() == '.tagall':
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
                elif msg.text in [".sr","Setread"]:
                    araragiayane.sendMessage(msg.to, "System siap menciduk 􀨁􀄻sip􏿿􀜅􀅔laugh􏿿")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("System Mengintai")
                elif msg.text in [".dr","Delread"]:
                    araragiayane.sendMessage(to, "System Menghapus data pembacaan 􀨁􀄻sip􏿿􀜅􀅔laugh􏿿")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        print ("Terbaca")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        araragiayane.sendMessage(msg.to, "[Reader]:\n%s\nTime:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        araragiayane.sendMessage(msg.to, "Setting ke system cyduk dahulu")
                        
                        
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#
#════════════════════════════════════════════════════════════════════════════════════════════════════════════════#


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
                                    araragiayane.sendMessage(to, "Jangan summon nanti cinta 􀜅􀄃hmm􏿿 susah move on 􁄁􀆹pisau􏿿􀜅􀅔laugh􏿿")
                                    sendMessageWithMention(to, contact.mid)
                                break
        if op.type == 55:
            print ("[ 55 ] Noticed")
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
            try:
                if op.param1 in wait2['readPoint']:
                    Name = araragiayane.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        print (time.time() + name)
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