import tkinter
import cv2
import numpy
from pynput import mouse,keyboard
import time
"""
                                            ████████ ██████   ██████  ███    ███  ██████  ███████ ███    ███                                             
                                               ██    ██   ██ ██    ██ ████  ████ ██    ██ ██      ████  ████                                             
                                               ██    ██████  ██    ██ ██ ████ ██ ██    ██ ███████ ██ ████ ██                                             
                                               ██    ██   ██ ██    ██ ██  ██  ██ ██    ██      ██ ██  ██  ██                                             
                                               ██    ██   ██  ██████  ██      ██  ██████  ███████ ██      ██                                             
                                                                                                                                                         

Repo :  tromoSM/BlankTools/
Forked : false
Name : Cursor-tracker
Version : V1.0
Release-description : default
Author : tromoSM
User preferences : None
"""     

pointsize=10
last=time.time()
tk=tkinter.Tk()
tk.withdraw()
size=(tk.winfo_screenwidth(),tk.winfo_screenheight())
print(size)
cnv=numpy.zeros((size[1],size[0],3),dtype=numpy.uint8)
cnv[:]=[255,255,255]

def stoptracker(ev):
    if ev==keyboard.Key.esc:
        mouseev.stop()
        return False
    
def point(x,y):
    if int(time.time())-last>2:
     cv2.circle(cnv,(x,y),pointsize,(255,0,0),-1)
    else:
     cv2.circle(cnv,(x,y),pointsize,(0,0,255),-1)

def clickev(x,y):
     cv2.circle(cnv,(x,y),15,(38,84,255),-1) 

def scrollerev(x,y,dx,dy):
       global pointsize
       lastpoint=pointsize
       if dy<0:
           if pointsize>0:
            pointsize-=1
       else:
           pointsize+=1

       print(f'pointer size changed from {lastpoint} to {pointsize}')
   
mouseev=mouse.Listener(on_move=point,on_click=clickev,on_scroll=scrollerev)
mouseev.start()
with keyboard.Listener(on_press=stoptracker) as keyev:
    keyev.join()

mouseev.join()
cv2.imshow('Cur',cnv)
cv2.waitKey(0)
cv2.destroyAllWindows()
