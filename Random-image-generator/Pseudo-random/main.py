import os as meowl
import random as babyoil
import tkinter as diddy
from PIL import Image as dogshit
import time as shopataldiis
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : 
Version : [0]:V1st
Release-description : using pseudo-random
Author : tromoSM
"""     
fileform="png"
name="gurt"
location=""
path=f"{location}{name}.{fileform}"
res=1

meth='pseudo-random'
ye=shopataldiis.time()
fuh=int(diddy.Tk().winfo_screenwidth()*res)
nih=int(diddy.Tk().winfo_screenheight()*res)
diddyblud=dogshit.new('RGB',(fuh,nih),color='black')
dumbass=diddyblud.load()
fuhnih=0 
for gurt in range(fuh):
    for dih in range(nih):
        r=babyoil.randint(0,255)
        g=babyoil.randint(0,255)
        b=babyoil.randint(0,255)
        print(f'{r,g,b}[{fuhnih}]')       
        dumbass[gurt,dih]=(r,g,b)
        fuhnih+=1
diddyblud.show()
corndogcat=shopataldiis.time()
diddyblud.save(path,fileform)
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
