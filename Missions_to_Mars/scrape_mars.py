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
# URL of page to be scraped
    browser = init_browser()
    mars_dict = ()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

# Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # mars["news_title"] = soup.find('div', class_ ='content_title').get_text()
    p_news = soup.find('div', class_= 'article_teaser_body')
    p_news = p_news.text.strip()
    mars_dict["p_news"] = p_news

    # return mars


#     browser = Browser('chrome', headless = False)
    url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    
    featured_image = soup.find(class_="thumb")
    featured_image_url='https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23503_hires.jpg'

    

#     browser = Browser('chrome', headless = False)
#     url = 'https://twitter.com/marswxreport?lang=en'
#     browser.visit(url)

#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find_all(class_ ='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather.text.strip()
    mars_dict["mars_weathers"] = mars_weather
#     return mars_weather

#     browser = Browser('chrome', headless = False)
#     url = 'https://space-facts.com/mars/'
#     browser.visit(url)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     
    mars_facts = pd.read_html("https://space-facts.com/mars/")
    mars_facts_df=mars_facts[0]
    mars_dict["mars_fact"] = mars_fact
    mars_facts_df.columns=['MARS PLANET PROFILE', 'Description']
    mars_facts_df.set_index('MARS PLANET PROFILE', inplace=True)
    mars_facts_df

# #Mars Hemispheres
#     browser = Browser('chrome', headless = False)
    url2 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('div',class_= 'result-list')
    hemisphere_info = results.find_all('div', class_='item')

    titles = []
    hemisphere_image_urls_dict = []

    
for hemisphere in hemisphere_info:
        title = hemisphere.find('h3').text
        titles.append(title)
        hemis_url =hemisphere.find('a')['href']
        h_url = "https://astrogeology.usgs.gov/" + hemis_url
        
        browser.visit(h_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
    
        find_image = soup.find('div', class_ = 'downloads')
        same_hemisphere_url = find_image.find('a')['href']
        hemisphere_image_urls_dict.append({"Title": title, "img_url":same_hemisphere_url })
    
    mars_Data["hemisphere_image_urls_dict"] = hemisphere_image_urls_dict
# Close the browser after scraping

mars_dict = {
    #"News_Title": para
    "News_Paragraphs": p_news,
    "Mars_weathers": mars_weather,
    "Mars_fact": mars_fact
}
