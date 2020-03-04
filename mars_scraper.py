from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser

browser = Browser('chrome', headless=False)
#####################################
nasa_url = 'https://mars.nasa.gov/news/'
browser.visit(nasa_url)
html = requests.get(nasa_url)
soup = bs(html.text, 'html.parser')

news_title = soup.find('div', class_='content_title').find('a').text
print(news_title)
news_p = soup.find(class_='rollover_description_inner').text
print(news_p)

#####################################
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)
html = requests.get(jpl_url)
soup = bs(html.text, 'html.parser')

featured_img_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
print(featured_img_url)
# Website Url 
main_url = 'https://www.jpl.nasa.gov'
# Concatenate website url with scrapped route
featured_img_url = main_url + featured_img_url
# Display full link to featured image
featured_img_url

#######################################
mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_url)
html = requests.get(mars_weather_url)
soup = bs(html.text, 'html.parser')
mars_weather = soup.find('div', class_="js-tweet-text-container").text[1:-1]
print(mars_weather)

######################################
mars_facts_url = 'https://space-facts.com/mars/'
mars_facts = pd.read_html(mars_facts_url)
mars_df = mars_facts[0]
mars_str = mars_df.to_html
mars_str

######################################
mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(mars_hemi_url)
html = requests.get(mars_hemi_url)
soup = bs(html.text, 'html.parser')
mars_dict = []
items = soup.find_all('div', class_="item")
items
base_url = 'https://astrogeology.usgs.gov'
for i in items:
    title = i.find('h3').text
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    browser.visit(base_url + partial_img_url)
    partial_img_html = browser.html
    soup = bs(partial_img_html, 'html.parser')
    img_url = base_url + soup.find('img', class_='wide-image')['src']
    mars_dict.append({"title" : title, "img_url" : img_url})
    mars_dict