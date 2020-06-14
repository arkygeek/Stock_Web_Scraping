import requests
from bs4 import BeautifulSoup
import time

def UPS_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/UPS?p=UPS&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(price)

def Mircrosoft_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(price)

def RY_Canada_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/RY?p=RY&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(price) 

def Coca_Cola_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/KO?p=KO&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(price)

def Nintendo_Tracker():
    URL = 'https://uk.finance.yahoo.com/quote/NTDOY?p=NTDOY&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    print(price)


while True:
    UPS_Tracker()
    Mircrosoft_Tracker()
    RY_Canada_Tracker()
    Coca_Cola_Tracker()
    Nintendo_Tracker()
    time.sleep(2)
