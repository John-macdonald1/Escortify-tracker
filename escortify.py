from selenium import webdriver 
from discord_webhook import DiscordWebhook
from selenium.webdriver.common.by import By
import time

URL = 'https://escortify.co.nz/auckland-escorts/chanelley-25434'
DISCORD_URL = "https://discord.com"
ESCORT_NAME = 'CHANELLEY'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
last_online = None
initial_likes = None

current_time = time.time()
formatted_time = time.strftime("%b %d %a at %I:%M %p", time.localtime(current_time))

while True:
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(4) 
    status = driver.find_element(By.XPATH, '//*[@id="contact"]/div[2]/p/span[2]/span').text
    like_button = driver.find_element(By.XPATH, '//*[@id="voting_plugin"]/div/a/span').text

    if last_online != status:   
        if status == "OFFLINE":
            message = f"{ESCORT_NAME} is now offline - {formatted_time}"
        else:
            message = f"{ESCORT_NAME} is now 😍🥰online🥰😍 - {formatted_time}"

        webhook_url = DISCORD_URL
        webhook = DiscordWebhook(url=webhook_url, content=message)
        response = webhook.execute()
    last_online = status
    

    current_likes = like_button
    if initial_likes is None:
        initial_likes = current_likes
    else:
        if current_likes > initial_likes:
            like_message = f"New like added for {ESCORT_NAME} at {formatted_time}! Total likes: {current_likes}"
            like_webhook = DiscordWebhook(url=DISCORD_URL, content=like_message)
            like_webhook.execute()

    time.sleep(500)
