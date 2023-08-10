from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import os
from pathlib import Path

import re

df=pd.read_json('Contact.json')

def isValid(s):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    match = Pattern.match(s)
    if match:
        return match.group()
    return None




df=pd.read_json('Contact.json')


#Driver setup
local_app_data_path = os.getenv('LOCALAPPDATA')
edge_user_data_path = Path(local_app_data_path) / 'Microsoft' / 'Edge' / 'User Data'




options = Options()
options.add_argument(f"user-data-dir={edge_user_data_path}")
options.add_argument("profile-directory=whatsapp_automation");
driver = webdriver.Edge(options = options)

driver.get("https://web.whatsapp.com/")



driver.get("https://web.whatsapp.com/")



share=df.loc[0,"msg"]

df=pd.json_normalize(df['data'])

wait = WebDriverWait(driver, 100)

try:
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')))
    print("Logged in successfully.")
except:
    print("Login failed or took too long.")


for index,row in df.iterrows():
    phone = isValid(str(row["phone"]))
    if phone:
        if len(phone) > 10:
            if phone.startswith("0"):
                phone = phone[1:]
            elif phone.startswith("91"):
                phone = phone[2:] 
        try:
            url = 'https://web.whatsapp.com/send?phone=' + str(phone) + '&text=' + share
            driver.get(url)
            try:
                click_btn =WebDriverWait(driver,35).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))
                )
            except Exception as e:
                print("Sorry message could not sent to " + phone)
            else:   
                sleep(5)
                click_btn.click()
                sleep(3)
                print('Message sent to: ' + phone)
        except Exception as e:
            print('Failed to send message to ' + phone)
    else:
        print("Invalid Number:"+ str(row["phone"]))


for index,row in df.iterrows():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(row["phone"]) + '&text=' + share
        
        driver.get(url)

        try:
            click_btn =WebDriverWait(driver,35).until(
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
print("The script executed successfully.")
