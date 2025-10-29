import time as bruv
from colorama import Fore, Style
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : x
Version : V1.0st
Release-description : x
Author : tromoSM
User preferences : var(x)
"""  
BlankTools={"Repo":"tromoSM/BlankTools/","Forked":"False", "Version":"V1.0st","Release-des":"x","Author":"tromoSM","Variable":"var(x)","Killswitch":"False","Additional-advice":"None"}   
SafeMode=False
print(f'''
                                  ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓
                                  ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃
                                  ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗
                                                         ┛                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Kill switch : {BlankTools["Killswitch"]}\n│ Safe mode : {SafeMode}
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
     print(Fore.RED+"Exiting BlankTools..."+Style.RESET_ALL)
     bruv.sleep(0.5)
     exit()
    elif yo.upper()=="-INFO":
      print("This tool is currently in safe mode. You must exit safe mode to use this tool. Answer with 'y' or 'n' when prompted.\n")
      bruv.sleep(0.5)
      fuhhh=input("Do you want to exit safe mode (y/n)? ")
      if fuhhh.upper()=="Y":
        SafeModeLoader()
      elif fuhhh.upper()=="N":
          print(Fore.RED+"Exiting BlankTools..."+Style.RESET_ALL)
          bruv.sleep(0.5)
          exit()
      else :
         print("Warning : value must be 'y' or 'n'.")
         bruv.sleep(0.5)
         print(Fore.RED+"Exiting BlankTools..."+Style.RESET_ALL)
         bruv.sleep(1)
         exit()
    else : 
     gurt= input("Value must be 'y' or 'n'. Do you want to exit safe mode (y/n)?")
     if gurt.upper()=="Y":
       SafeModeLoader()
     else:
      print(Fore.RED+"Exiting BlankTools..."+Style.RESET_ALL)
      bruv.sleep(0.5)
      exit()
