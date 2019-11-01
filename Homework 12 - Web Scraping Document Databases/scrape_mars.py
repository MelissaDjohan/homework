#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time


def scrape():
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=r"C:\Users\melis\Downloads\chromedriver.exe", options=chrome_options)

    url = "https://mars.nasa.gov/news/"
    driver.get(url)
    time.sleep(1)

    # Scrape page into Soup
    html = driver.page_source
    soup = bs(html, 'html.parser')

    print(soup.prettify())

    titles = soup.find_all('div', class_="content_title")
    print(titles)

    body = soup.find_all('div', class_="rollover_description")
    print(body)

    # collect the latest News Title and Paragraph Text
    results = soup.find_all('div', class_="slide")
    for result in results:
        titles = result.find('div', class_="content_title")
        title = titles.find('a').text
        bodies = result.find('div', class_="rollover_description")
        body = bodies.find('div', class_="rollover_description_inner").text
        print('----------------')
        print(title)
        print(body)
    return results

# In[7]:





# In[7]:




