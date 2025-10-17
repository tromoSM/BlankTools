import ctypes
import tkinter as diddyblud
import time
import cv2
import random
ahh=cv2.VideoCapture("./main.gif")
fuhtwin=diddyblud.Tk()
fuhtwin.withdraw()
fuhni=fuhtwin.winfo_screenwidth()-100
fuhdi=fuhtwin.winfo_screenheight()

while True:
    gurt,fuh = ahh.read()
    if not gurt:
        ahh.set(cv2.CAP_PROP_POS_FRAMES,0)
        continue
   
    ass= random.randint(1,151)
    for i in range(150) :
     if cv2.waitKey(1)!= -1:
       break
     cv2.namedWindow(f'{ass}',cv2.WINDOW_NORMAL)
     cv2.moveWindow(f'{ass}',random.randint(0,fuhni),random.randint(0,fuhdi))
     cv2.setWindowProperty(f'{ass}', cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
     cv2.imshow(f'{ass}',fuh)
     ctypes.windll.user32.SetLayeredWindowAttributes(ctypes.windll.user32.FindWindowW("Main HighGUI class",f'{ass}'),0, 200, 0x2)
     ctypes.windll.user32.SetWindowPos(ctypes.windll.user32.FindWindowW("Main HighGUI class",f'{ass}'),-1,0,0,0,0,0x0001)
fuhtwin.destroy()
cv2.destroyAllWindows() 
