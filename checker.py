import psutil
import subprocess as sp
import keyboard
import time as t
print("griffindoescooking: \nHello and thank you for using my relauncher if the button isnt clicking in the right spot edit the main.bat file")
print("\nNow we wait for it to crash...")
def checkblox():
	for proc in psutil.process_iter(['pid','name']):
		if proc.info['name'] == 'Windows10Universal.exe':
			return False
	print("Roblox Crashed!")
	return True
while keyboard.is_pressed('q') == False:
	if checkblox():
		sp.call(['main.bat'])
