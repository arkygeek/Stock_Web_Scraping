# This project is going to look at the cost of different stocks.
# We will use Yahoo finance to recieve the information

import requests
from bs4 import BeautifulSoup
import time
import sys
from time import sleep
import os

# Each of the following functions pulls information from each unique URL
# It then, in real time, will give the output
# which corresponds with the amount on Yahoo


# Definitions


def _trackerUPS():
    URL = 'https://uk.finance.yahoo.com/quote/UPS?p=UPS&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all(
        'div',
        {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
        0].find('span').text
    return price


def _trackerMicrosoft():
    URL = 'https://uk.finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all(
        'div',
        {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
        0].find('span').text
    return price


def _trackerRYCanada():
    URL = 'https://uk.finance.yahoo.com/quote/RY?p=RY&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all(
        'div',
        {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
        0].find('span').text
    return price


def _trackerCocaCola():
    URL = 'https://uk.finance.yahoo.com/quote/KO?p=KO&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all(
        'div',
        {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
        0].find('span').text
    return price


def _trackerNintendo():
    URL = 'https://uk.finance.yahoo.com/quote/NTDOY?p=NTDOY&.tsrc=fin-srch'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'lxml')
    price = soup.find_all(
        'div',
        {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[
        0].find('span').text
    return price


def _Countdown(theValue):
    while 0 < theValue:
        sys.stdout.write("\r s to wait \r%d" % theValue)
        sys.stdout.flush()
        theValue -= 1
        sleep(1)
    sys.stdout.write("\r...continuing...\r")
    sys.stdout.flush()


def _scrape(theNumberOfCyclesToRun):
    sys.stdout.write("\r...Scraping Data...\r")  # gets removed below

    _trackerUPS()
    _trackerMicrosoft()
    _trackerRYCanada()
    _trackerCocaCola()
    _trackerNintendo()

    sys.stdout.flush()  # removes Scraping Data notice

    print("UPS Tracker = " + _trackerUPS())
    print("Microsoft Tracker = " + _trackerMicrosoft())
    print("RY Tracker = " + _trackerRYCanada())
    print("Coke Tracker = " + _trackerCocaCola())
    print("Nintendo Tracker = " + _trackerNintendo())
    print("\r")


# Executing Code


def main():
    os.system('cls')

    myUserEnteredMaxCycles = input("Enter number of cycles to run (max 15): ")
    myUserEnteredTime = input("Enter time interval between cycles (seconds): ")

    myCycleCounter = 1

    while myCycleCounter < int(myUserEnteredMaxCycles) + 1:
        _Countdown(int(myUserEnteredTime))
        sys.stdout.write("Cycle ")
        sys.stdout.write(str(myCycleCounter))
        sys.stdout.write("               \n")
        # no need for flush this time because we *want* to use this (as a title)
        _scrape(myUserEnteredMaxCycles)
        # let's 'increment' it after the fact (for a change)
        myCycleCounter += 1

    print("Thanks for testing this!")


main()

