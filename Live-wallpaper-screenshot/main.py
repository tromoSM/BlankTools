import ctypes
import os
import time as bruv
import pyautogui
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : Live wallpaper screenshot 
Version : V1.0st
Release-description : ∞ no kill switch
Author : tromoSM
User preferences : var(wait), var(tempName), var(SafeMode)
"""  
BlankTools={"Repo":"tromoSM/BlankTools/","Forked":"False", "Version":"V1.0st","Release-des":"∞ no kill switch","Author":"tromoSM","Variable":"var(wait), var(tempName), var(SafeMode)","Killswitch":"False","Additional-advice":"None"}   
wait=0.1
tempName="temp"
tempfile=f"{tempName}.bmp"
SafeMode=False

ass=0
print(f'''
                                  ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓
                                  ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃
                                  ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗
                                                         ┛                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Temporary image path : {os.path.abspath(tempfile)}\n│ Kill switch : {BlankTools["Killswitch"]}\n│ Safe mode : {SafeMode}\n
      '''
      )

def SafeModeLoader():
     txt="Exiting safe mode "
     waitahh=0.3
     bruv.sleep(waitahh)
     loadcont=f"{txt}                ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓"
     print(loadcont)
     bruv.sleep(waitahh)
     loadcont=f"{txt}                ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃"
     print(loadcont)
     bruv.sleep(waitahh)
     loadcont=f"{txt}                ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗"
     print(loadcont)
     bruv.sleep(waitahh)
     loadcont=f"{txt}                                       ┛                 "
     print(loadcont)
     bruv.sleep(waitahh)
     loadcont=f"\n"
     print(loadcont)
    
if SafeMode==True :
    yo=input("Do you want to exit safe mode (y/n)? ")
    if yo.upper()=="Y" :
     SafeModeLoader()
    elif yo.upper()=="N":
     print("Exiting BlankTools...")
     bruv.sleep(0.5)
     exit()
    elif yo.upper()=="-INFO":
      print("This tool is currently in safe mode. You must exit safe mode to use this tool. Answer with 'y' or 'n' when prompted.\n")
      bruv.sleep(0.5)
      fuhhh=input("Do you want to exit safe mode (y/n)? ")
      if fuhhh.upper()=="Y":
        SafeModeLoader()
      elif fuhhh.upper()=="N":
          print("Exiting BlankTools...")
          bruv.sleep(0.5)
          exit()
      else :
         print("Warning : value must be 'y' or 'n'.")
         bruv.sleep(0.5)
         print("Exiting BlankTools...")
         bruv.sleep(1)
         exit()
    else : 
     gurt= input("Value must be 'y' or 'n'. Do you want to exit safe mode (y/n)?")
     if gurt.upper()=="Y":
       SafeModeLoader()
     else:
      print("Exiting BlankTools...")
      bruv.sleep(0.5)
      exit()
     
while True :
    ass+=1
    if os.path.exists(tempfile) :
     os.remove(tempfile) 
    dawg=pyautogui.screenshot()        
    dawg.save(tempfile)
    ctypes.windll.user32.SystemParametersInfoW(20 , 0,os.path.abspath(tempfile),0x01|0x02)
    bruv.sleep(wait)
    print(ass)
