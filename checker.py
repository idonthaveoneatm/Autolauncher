import psutil
import subprocess as sp
import keyboard

WEBHOOK = False #Toggle True or False

if WEBHOOK:
	#Discord webhook information
	discordid = "" #If you dont know how to get it google it
	webhookurl = "" #Your webhook
	
	from discord_webhook import DiscordWebhook, DiscordEmbed
	content = f"<@!{discordid}>"
	allowed_mentions = {"users": [f"{discordid}"]}
	webhook = DiscordWebhook(url=webhookurl,content=content,allowed_mentions=allowed_mentions)
	webhook.add_embed(DiscordEmbed(title='Game Restarted',description='The game shouldve restarted for you',color='a49ae6'))


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
		if WEBHOOK: 
			response = webhook.execute()
