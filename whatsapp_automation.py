from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json

c=open('Contact.json',)

Contact =json.load(c)

driver=webdriver.Chrome()

count=0

driver.get("https://web.whatsapp.com/")
input("Press enter after login into Whatsapp web")
share = str(input("Enter link:"))

for i in Contact:
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(i["number"]) + '&text=' + share
        sent= False

        driver.get(url)
        try:
            click_btn =WebDriverWait(driver,35).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span'))
            )
        except Exception as e:
            print("Sorry message could not sent to " + i["name"])
        else:
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ' + i["name"])
        count = count + 1
    except Exception as e:
        print('Failed to send message to ' + i["name"])
driver.quit()
print("The script executed successfully.")
