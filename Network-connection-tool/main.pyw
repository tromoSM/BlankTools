
#                                   _________  ________  ________  _____ ______   ________  ________  _____ ______                                        
#                                  |\___   ___\\   __  \|\   __  \|\   _ \  _   \|\   __  \|\   ____\|\   _ \  _   \                                      
#                                  \|___ \  \_\ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \___|\ \  \\\__\ \  \                                     
#                                       \ \  \ \ \   _  _\ \  \\\  \ \  \\|__| \  \ \  \\\  \ \_____  \ \  \\|__| \  \                                    
#                                        \ \  \ \ \  \\  \\ \  \\\  \ \  \    \ \  \ \  \\\  \|____|\  \ \  \    \ \  \                                   
#                                         \ \__\ \ \__\\ _\\ \_______\ \__\    \ \__\ \_______\____\_\  \ \  \    \ \  \                                  
#                                          \|__|  \|__|\|__|\|_______|\|__|     \|__|\|_______|\_________\ |__|    \ |__|                          
#                                                                                             \|_________|_|__|     \|__|                                               
#  
from urllib import request
from windows_toasts import AudioSource, Toast, ToastAudio, ToastDisplayImage, WindowsToaster
def hellp():
 try:
    request.urlopen("http://www.msftconnecttest.com/connecttest.txt", timeout=8)
 except request.URLError as err: 
          yo()
dawg=1
def yo():
 global dawg
 if dawg==1: 
    dawg=67
    vro()

  
def vro(): 
 burnttoast = WindowsToaster('tromoSM | ')
 TotЯ = Toast()
 TotЯ.text_fields = ['Wifi connection lost']
 TotЯ.AddImage(ToastDisplayImage.fromPath('./wifi-ico-SM.png'))
 TotЯ.audio=ToastAudio(AudioSource.Default, looping=False)
 burnttoast.show_toast(TotЯ)

while True :
    hellp()
