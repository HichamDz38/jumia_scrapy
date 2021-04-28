#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import sys
import requests
import sys
import json
import logging

url = "https://food.jumia.dz/restaurants"
header = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
payload={'username':"",
"OLB_REMEMBER_USERNAME":"Y",
"screen":"banking"}

if __name__=='__main__':
    try:
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('log-level=3')
        prefs={"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option('prefs', prefs)
        prefs={'disk-cache-size': 10240}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        wait(driver, 50).until(EC.presence_of_element_located((By.TAG_NAME, 'article')))
        article =driver.find_elements_by_tag_name("article")
        print(len(article))
        #L=driver.getWindowHandles()
        #driver.switch_to_alert()
        # print(L)	
    except Exception as e:
        print(e)
        driver.quit()
        time.sleep(1)
        driver = webdriver.Chrome(chrome_options=options)
    #driver.quit()