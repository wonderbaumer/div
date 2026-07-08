import win32com.client as comclt
import time

while True:
    wsh = comclt.Dispatch("WScript.Shell")
    # wsh.AppActivate("Notepad") # select another application
    wsh.SendKeys("{CAPSLOCK}") # send the keys you want
    current_time = time.localtime()
    time.sleep(3 * 60) #update every 3 mins
    


    
