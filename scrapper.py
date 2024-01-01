# Contains functions to scrape data from websites
from urls import url_3, url_1, url_2

import requests
from bs4 import BeautifulSoup
import re


def get_hashrate(url):
    # send get
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error reaching the website: {e}"

    # parising
    soup = BeautifulSoup(response.text, 'html.parser')

    # search for the needed tag
    abbr_tag = soup.find('abbr')
    if abbr_tag:
        # extract number
        match = re.search(r'(\d+\.\d+)', abbr_tag.get_text())
        if match:
            return match.group(1)

    return "no tag found"


def get_preis(url):
    # send get
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error reaching website: {e}"

    # Parsing
    soup = BeautifulSoup(response.text, 'html.parser')

    # search for the needed tag
    preis_tag = soup.find('span', {'class':'currency-pricestyles__Price-sc-1v249sx-0 jobFak'})

    # Extrct number
    if preis_tag:
        price_text = preis_tag.get_text(strip=True)
        return price_text
    else:
        return "Price tag not found"



def get_market_cap(url):
    # send get
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error reaching the website: {e}"

    # Parsing
    soup = BeautifulSoup(response.text, 'html.parser')

    # look for tag
    preis_tag = soup.find('h4', {'class':'text-dark marketcap'})
    # extract data
    if preis_tag:
        price_text = preis_tag.get_text(strip=True)
        return price_text
    else:
        return "Price tag not found"

# scrape function
def scrape_full():
    print("Hashrate:" , (get_hashrate(url_1)))
    print("Btc-Preis [USD]: ", (get_preis(url_2)))
    print("Market-Cap: " , (get_market_cap(url_3)))

