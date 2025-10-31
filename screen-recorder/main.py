import threading
import pyautogui 
import numpy as cannadih
import cv2 as vro
import tkinter as meowl
import win32api
import os
import time
from pynput import keyboard
from colorama import Fore, Style
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : Screen recorder
Version : V1.0st
Release-description : none
Author : tromoSM
User preferences : var(filename), var(fileformat), var(codec), var(fps), var(Notify)
"""  
BlankTools={"Repo":"tromoSM/BlankTools/","Forked":"False", "Version":"V1.0st","Release-des":"none","Author":"tromoSM","Variable":" var(filename), var(fileformat), var(codec), var(fps), var(Notify)","Killswitch":"global(Esc),console(`q`)","Additional-advice":"None"}   

filename="Recording"
fileformat="mp4"
codec="mp4v"
fps=30.0
Notify=True


individual_id=int(time.time())
print(f'''
                                  ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓
                                  ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃
                                  ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗
                                                         ┛                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Filename : {filename}\n│ individual id : {individual_id}\n│ Path : {os.getcwd()}\\{filename}-{individual_id}.{fileformat}\n│ File format : {fileformat}\n│ Codec : {codec}\n│ Fps : {int(fps)}\n│ Notify : {Notify}\n│ Kill switch : {BlankTools["Killswitch"]}\n│
      '''
      )
faw=meowl.Tk()
faw.withdraw()
tgpu=(faw.winfo_screenwidth(),faw.winfo_screenheight())
yeisthegoat=vro.VideoWriter_fourcc(*f'{codec}')
guessmyass=f'{filename}-{individual_id}.{fileformat}'
fuckme=fps
monalisatypeshit=vro.VideoWriter(guessmyass,yeisthegoat,fuckme,tgpu)
sleepbruv=threading.Event()

def bruh(key):
  if key == keyboard.Key.esc:
    sleepbruv.set()
    return False

ear=keyboard.Listener(on_press=bruh)
ear.start()

while not sleepbruv.is_set() :
 jblfucker=cannadih.array(pyautogui.screenshot())
 jblfucker=vro.cvtColor(jblfucker,vro.COLOR_BGR2RGB)
 monalisatypeshit.write(jblfucker)
 if vro.waitKey(1)& 0xFF==ord('q'):
       if Notify==True: 
        win32api.Beep(150,200) 
       print(Fore.LIGHTBLUE_EX+f"Saving file to '{os.getcwd()}\\{filename}-{individual_id}.{fileformat}'"+Style.RESET_ALL)
       break
 
try:
  print(Fore.LIGHTBLUE_EX+f"Saving file to '{os.getcwd()}\\{filename}-{individual_id}.{fileformat}'"+Style.RESET_ALL)
  time.sleep(0.1)
  ear.stop()
  print(Fore.LIGHTGREEN_EX+f"Saved to '{os.getcwd()}\\{filename}-{individual_id}.{fileformat}'"+Style.RESET_ALL)
  time.sleep(1)
except Exception:
  pass  
monalisatypeshit.release()
vro.destroyAllWindows()
faw.destroy()
if Notify==True: 
   win32api.Beep(150,200) 
