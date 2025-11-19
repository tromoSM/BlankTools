import os as dih
import time as diddyblud
from tkinter import Tk,filedialog
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : hide-files
Version : V1.0st
Release-description : 1.0
Author : tromoSM
User preferences : input(Hide or unhide), file-input(multiple), input(Enter file path here..)
"""  
BlankTools={"Repo":"tromoSM/BlankTools/","Forked":"False", "Version":"V1.0st","Release-des":"1.0","Author":"tromoSM","Variable":"input(Hide or unhide), file-input(multiple), input(Enter file path here..)","Killswitch":"False","Additional-advice":"Multiple file selection is supported when hiding files."}   
print(f'''
                                  ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓
                                  ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃
                                  ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗
                                                         ┛                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Kill switch : {BlankTools["Killswitch"]}\n│ Additional-info : {BlankTools['Additional-advice']}
      '''
      )
maindih=int(input('    0 => Hide\n    1 => Unhide\nHide or unhide :'))
if maindih==0:
 fuh=Tk()
 fuh.withdraw()
 gurteatinmyassrn=list(filedialog.askopenfilenames())
 for dihs in gurteatinmyassrn :
    crackmetwin=dih.path.normpath(dihs)
    dih.system(f'attrib +s +h +i "{crackmetwin}"')
    print(f'{crackmetwin} is now hidden from file explorer and windows search even if the "show hidden items" is turned on')
elif maindih==1:
 gurteatinmyassrn=input('Enter file path here..  :')
 crackmetwin=dih.path.normpath(gurteatinmyassrn)
 dih.system(f'attrib -s -h -i "{crackmetwin}"')
 print(f'{crackmetwin} is now visible to file explorer and windows search.')
else:
  print(f'ERROR : input value must be 0 or 1.{maindih} is not a acceptable value')
