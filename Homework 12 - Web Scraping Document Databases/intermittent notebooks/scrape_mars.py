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

    # collect the latest News Title
    latest_title = soup.find_all('div', class_="content_title")[0].text
    print(latest_title)

    # collect the latest Paragraph Text
    latest_text = soup.find_all('div', class_="rollover_description")[0].text
    print(latest_text)

    # collect the all News Titles and Paragraph Text
    results = soup.find_all('div', class_="slide")
    for result in results:
        titles = result.find('div', class_="content_title")
        title = titles.find('a').text
        bodies = result.find('div', class_="rollover_description")
        body = bodies.find('div', class_="rollover_description_inner").text
        print('----------------')
        print(title)
        print(body)

    # JPL Mars Space Images - Featured Image
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    driver.get(images_url)
    time.sleep(1)

    # Scrape page into Soup
    jpl_html = driver.page_source
    jpl_soup = bs(jpl_html, 'html.parser')

    # to find the featured image
    featured = jpl_soup.find('div', class_="img").find('img').get('src')
    print(featured)

    # to create url
    feature_url = images_url + featured
    print(feature_url)

    # Mars Weather
    weather_url = "https://twitter.com/marswxreport?lang=en"
    driver.get(weather_url)
    time.sleep(1)

    # Scrape page into Soup
    weather_html = driver.page_source
    weather_soup = bs(weather_html, 'html.parser')

    latest_weather = weather_soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[
        0].text
    print(latest_weather)

    driver.quit()
