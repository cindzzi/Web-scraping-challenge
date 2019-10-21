import os
import requests 
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_info = {}
# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

# Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_info["news_title"] = soup.find('div', class_ ='content_title').get_text()
    mars_info["p_news"] = soup.find('div', class_= 'article_teaser_body').get_text()



    return mars_info
