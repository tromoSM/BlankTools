import os as meowl
import secrets as babyoil
import tkinter as diddy
import time as shopataldiis
from PIL import Image as dogshit
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : 
Version : [1]:V1st
Release-description : using cryptographically-secure-pseudo-random
Author : tromoSM
User preferences : var(location),var(res),var(fileform),var(name)
"""     
fileform="png"
name="gurt"
location=""
path=f"{location}{name}.{fileform}"
res=1

ye=shopataldiis.time()
meth='cryptographically-secure-pseudo-random'
fuh= int(diddy.Tk().winfo_screenwidth()*res)
nih=int(diddy.Tk().winfo_screenheight()*res) 
diddyblud=dogshit.new('RGB',(fuh,nih),color='black')
dumbass=diddyblud.load()
fuhnih=0
for gurt in range(fuh):
    for dih in range(nih):
        r=babyoil.randbelow(255)
        g=babyoil.randbelow(255)
        b=babyoil.randbelow(255)
        print(f'{r,g,b}[{fuhnih}]')
        fuhnih+=1  
        dumbass[gurt,dih]=(r,g,b)
diddyblud.show()
corndogcat=shopataldiis.time()
diddyblud.save(path,fileform)
corndogcat=shopataldiis.time()
print(f'''
                                  ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓
                                  ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃
                                  ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗
                                                         ┛                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Path : {meowl.path.abspath((path))}\n│ Resolution : {diddy.Tk().winfo_screenwidth()*res} × {diddy.Tk().winfo_screenheight()*res}\n│ Compression method : {fileform}\n│ Runtime : {round((corndogcat-ye)/60,2)}min
│ Size : {meowl.path.getsize(path)//1024}kb ({meowl.path.getsize(path)} bytes)
│ Method : {meth}
      '''
      )
