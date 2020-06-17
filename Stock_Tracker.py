# This project is going to look at the cost of different stocks.
# We will use Yahoo finance to recieve the information
# This project makes use of the request and BeautifulSoup modules

import requests
from bs4 import BeautifulSoup
import time

# Each of the following functions pulls information from each unique URL
# It then, in real time, will give the output which corresponds with the amount on Yahoo

def UPS_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/UPS?p=UPS&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

def Mircrosoft_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

def RY_Canada_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/RY?p=RY&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

def Coca_Cola_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/KO?p=KO&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

def Nintendo_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/NTDOY?p=NTDOY&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

# Finally the while loop is what keeps the numbers continue to be scraped from Yahoo
# The time.sleep() variable tells us how many seconds in between each scraping the while loop should rest

while True:
    print(UPS_Tracker())
    print(Mircrosoft_Tracker())
    print(RY_Canada_Tracker())
    print(Coca_Cola_Tracker())
    print(Nintendo_Tracker())
    time.sleep(5)
