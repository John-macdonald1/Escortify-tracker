from selenium import webdriver 
from discord_webhook import DiscordWebhook
from selenium.webdriver.common.by import By
import time

URL = 'https://escortify.co.nz/wellington-escorts/alicia-23780' 
DISCORD_URL = "https://discord.com/api/webhooks/1214092858085343232/RuZkmA2DyJ6zLMXsYh57PDI6A9IDBT55UPUAFsOCHGyf9BppsmhhM7lrUNdhu_3PcA6L"

class escortmonitor:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.last_online = None
        self.initial_likes = None

    def get_formatted_time (self):
        current_time = time.time()
        return time.strftime("%b %d %a at %I:%M %p", time.localtime(current_time))
    
    def send_discord_message(self,content):
        webhook = DiscordWebhook(url=DISCORD_URL, content=content)
        webhook.execute()
 
    def escort_monitor(self):
        while True:
            driver = webdriver.Chrome(options=self.options)
            driver.get(URL)
            time.sleep(4) 
            status = driver.find_element(By.XPATH, '//*[@id="contact"]/div[2]/p/span[2]/span').text 
            like_button = driver.find_element(By.XPATH, '//*[@id="voting_plugin"]/div/a/span').text
            escort_name = driver.find_element(By.XPATH, '//*[@id="xxx"]/h1').text
            current_likes = like_button

            if self.last_online != status:   
                if status == "OFFLINE":
                    message = f"{escort_name} is now offline - {self.get_formatted_time()}"
                else:
                    message = f"{escort_name} is now online - {self.get_formatted_time()}"
                self.send_discord_message(message)
            self.last_online = status

            if self.initial_likes is None:
                self.initial_likes = current_likes
            elif current_likes > self.initial_likes:
                like_message = f"New like added for {escort_name} at {self.get_formatted_time()}! Total likes: {current_likes}"
                self.send_discord_message(like_message)
            self.initial_likes = current_likes

            time.sleep(600)

monitor = escortmonitor()
monitor.escort_monitor()
