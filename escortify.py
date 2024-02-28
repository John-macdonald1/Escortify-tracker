from selenium import webdriver 
from discord_webhook import DiscordWebhook
from selenium.webdriver.common.by import By
import time

URL = 'https://escortify.co.nz'
DISCORD_URL = "your discord webhook"
ESCORT_NAME = 'Escort'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
last_online = None

current_time = time.time()
formatted_time = time.strftime('%H:%M%p', time.localtime(current_time))     
print(formatted_time)

while True:
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(3) 
    status = driver.find_element(By.XPATH, '//*[@id="contact"]/div[2]/p/span[1]/span').text

    if last_online != status:   
        if status == "offline":
            message = f"{ESCORT_NAME} is now offline at {formatted_time}"
        else:
            message = f"{ESCORT_NAME} is now online at {formatted_time}"

        webhook_url = DISCORD_URL
        webhook = DiscordWebhook(url=webhook_url, content=message)
        response = webhook.execute()
    last_online = status

    time.sleep(600)
