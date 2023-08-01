from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import os
from pathlib import Path
import urllib.parse

df=pd.read_json('Contact.json')

#Driver setup
local_app_data_path = os.getenv('LOCALAPPDATA')
edge_user_data_path = Path(local_app_data_path) / 'Microsoft' / 'Edge' / 'User Data'

options = Options()
options.add_argument(f"user-data-dir={edge_user_data_path}")
options.add_argument("profile-directory=whatsapp_automation");
driver = webdriver.Edge(options = options)

driver.get("https://web.whatsapp.com/")

os.system("notepad input.txt")

f=open("input.txt","r")

share=urllib.parse.quote(f.read())

input("Press enter after writng the message to send")

for index,row in df.iterrows():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(row["phone"]) + '&text=' + share
        
        driver.get(url)

        try:
            click_btn =WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))
            )
        except Exception as e:
            print("Sorry message could not sent to " + row["username"])
        else:   
            sleep(2)
            click_btn.click()
            sleep(3)
            print('Message sent to: ' + row["username"])
    except Exception as e:
        print('Failed to send message to ' + row["username"])
driver.quit()
f.close()
print("The script executed successfully.")
