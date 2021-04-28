"""
jumia food restaurants scraper
written by : Hicham Dachir
date : 27/04/2021
"""
import time
import requests
from bs4 import BeautifulSoup

page = requests.get("https://food.jumia.dz/restaurants")
soup = BeautifulSoup(page.text, 'html.parser')

articles = soup.select(".columns .is-multiline")
print(articles)