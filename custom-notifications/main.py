import time as gurt
from windows_toasts import AudioSource,Toast,ToastAudio,ToastDisplayImage,WindowsToaster

"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : Custom-notifications
Version : V1.05st
Release-description : None
Author : tromoSM
User preferences : input(all) 
"""  
BlankTools={"Repo":"tromoSM/BlankTools/","Forked":"False", "Version":"V1.05st","Release-des":"None","Author":"tromoSM","Preferences":"input(all)","Killswitch":"False","Additional-advice":"None"}   
SafeMode='not available'
print(f'''
                                  ┳┓┓    ┓ ┏┳┓    ┓   ┓               ┏┓┳┳┓
                                  ┣┫┃┏┓┏┓┃┏ ┃ ┏┓┏┓┃┏  ┣┓┓┏  ╋┏┓┏┓┏┳┓┏┓┗┓┃┃┃
                                  ┻┛┗┗┻┛┗┛┗ ┻ ┗┛┗┛┗┛  ┗┛┗┫  ┗┛ ┗┛┛┗┗┗┛┗┛┛ ┗
                                                         ┛                 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ Kill switch : {BlankTools["Killswitch"]}\n│ Safe mode : {SafeMode}\n\n''')
Apptitle="BlankTools"
mainTITLE=""
description=''
img_main="./get_ui/fallbackmyahh.jpg"
audio=AudioSource.Default
audioLOOP=False
silent=False
#PREFF
a1=input(' • Enter an app title : ')
Apptitle=a1
a2=input(' • Enter an title : ')
mainTITLE=a2
a3=input(' • Enter an description : ')
description=a3
a4=input(' • Enter an path for your icon : ')
img_main=a4
print('''
   0 => None      
   1 => Window default notification
   2 => Instant message recieved
   3 => Mail notification
   4 => Reminder alert
\n   5 => Alarm 1
   6 => Alarm 2
   7 => Alarm 3
\n   8 => Calling ring 1 
   9 => Calling ring 2
   10 => Calling ring 3
''')
a5=int(input(' • Choose an audio choice(int) : '))
if a5==0:
  audio=AudioSource.Default
  silent=True
elif a5==1:
  audio=AudioSource.Default
elif a5==2:
  audio=AudioSource.IM
elif a5==3:
  audio=AudioSource.Mail
elif a5==4:
  audio=AudioSource.Reminder
elif a5==5:
  audio=AudioSource.Alarm
elif a5==6:
  audio=AudioSource.Alarm2
elif a5==7:
  audio=AudioSource.Alarm6
elif a5==8:
  audio=AudioSource.Call
elif a5==9:
  audio=AudioSource.Call6 
elif a5==10:
  audio=AudioSource.Call7 
print('\n')  
a6=input(' • Looping audio after playback ? (y/n/BOOL): ')
if a6.upper()=="TRUE" or a6.upper()=="y":
 audioLOOP=True
else:
  audioLOOP=False

print('''
  ex 0 => None      
  ex 1 => 1s
  ex 15 => 15s 
   ''')
a7=int(input(' • Notification Delaying (int) : '))
dih=a7
 
def vro(): 
 gurt.sleep(dih)
 burnttoast = WindowsToaster(Apptitle)
 TotЯ=Toast()
 TotЯ.text_fields=[mainTITLE,description]
 TotЯ.AddImage(ToastDisplayImage.fromPath(f'{img_main}'))
 TotЯ.audio=ToastAudio(audio, looping=audioLOOP,silent=silent)
 burnttoast.show_toast(TotЯ)

vro()
