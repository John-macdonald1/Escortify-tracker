# Escortify-tracker
Tracks your fav escorts to see when they come online/ofline


Download all the modules required:

`pip install -r requirements.txt
`


To start the bot just do

`escortify.py
`

URL = 'https://escortify.co.nz' - add escort URL you wish to track

NOTE - CODE ONLY WORKS FOR ESCORTIFY
-
DISCORD_URL = "your discord webhook" - https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks "how to add webhooks"


checks URL given every 10 minutes, can be adjusted at bottom 

`time.sleep(600)`

adjust numbers to liking, numbers in seconds 

code works for aus escortify as well to some extent. does not show when they go ofline as escortify.au does not have the same ofline value as nz. 
