#!/usr/bin/env python3.7

import requests
from bs4 import BeautifulSoup
import os
import numpy as np

def form_url(want, have):
    url = os.getenv('pt_base')
    want = "&want=%s" % (want)
    have = "&have=%s" % (have)
    full_url = url + want + have
    return full_url

def load_page(url):
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
    deal_list = []
    for deal in data:
        amounts = deal.split("⇐")
        buy_amount = int(amounts[0])
        pay_amount = int(amounts[1])
        ratio = buy_amount / pay_amount
        deal_list.append(ratio)
        #print("Buy %s fuse for %s chaos at %s ratio" % (buy_amount, pay_amount, ratio))
    return np.mean(deal_list)

url = form_url(2, 4)
url2 = form_url(4,2)

page = load_page(url)
page2 = load_page(url2)

maths = parse_page(page)
maths2 = parse_page(page2)

buy = calculate_ratio(maths)
sell = calculate_ratio(maths2)
print("Buy value for fusing orbs: %s per chaos orb" % (buy))
print("Buy value for chaos orbs: %s per fusing orb" % (sell))
