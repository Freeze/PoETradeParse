#!/usr/bin/env python3.7

import requests
from bs4 import BeautifulSoup
import os

def load_page():
    url = os.getenv('pt_url')
    page = requests.get(url)
    return page.text

def parse_page(page):
    deals = []
    soup = BeautifulSoup(page, 'lxml')
    trades = soup.find_all('div', class_='displayoffer ')
    for trade in trades[:5]:
        deal = trade.find('div', class_='displayoffer-middle')
        deals.append(deal.text)
    return deals

def calculate_ratio(data):
    for deal in data:
        amounts = deal.split("⇐")
        buy_amount = int(amounts[0])
        pay_amount = int(amounts[1])
        ratio = buy_amount / pay_amount
        print("Buy %s regret for %s chaos at %s ratio" % (buy_amount, pay_amount, ratio))
        
page = load_page()
maths = parse_page(page)
calculate_ratio(maths)
