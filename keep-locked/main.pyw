import ctypes
try:
  while True:
    ctypes.windll.user32.LockWorkStation()
except PermissionError:
    print("Permission error. Run as admin")
