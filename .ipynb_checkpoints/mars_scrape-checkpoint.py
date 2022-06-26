from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
from selenium import webdriver

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

##news
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('div', class_='list_text')
    result = results[0]

    todays_date = result.find('div', class_= 'list_date').text
    todays_news = result.find('div', class_='content_title').text
    news_result = result.find('div', class_='article_teaser_body').text
____________________________________________________
##space images
____________________________________________________
image_url = 'https://spaceimages-mars.com/'
browser.visit(feat_image_url)
html = browser.html
soup = bs(html, 'html.parser')

browser.links.find_by_partial_text('FULL IMAGE').click()

html = browser.html
soup = bs(html, 'html.parser')

image_box = soup.find('div', class_='fancybox-inner')
image_url =image_url.replace('index.html', '') + image_box.img['src']
__________________________________________________________
##facts
__________________________________________________________
facts_url = 'https://galaxyfacts-mars.com'
mars_facts = pd.read_html(facts_url,header =0)[0]
the_facts = pd.DataFrame(mars_facts)
the_facts = the_facts.reset_index(drop=True)
the_facts = the_facts.set_index("Mars vs. Earth Comparison")
tables = pd.DataFrame.to_html(facts_df)
_______________________________________________________
##hemispheres
_______________________________________________________
hemisphere_url = 'https://marshemispheres.com/'
browser.visit(hemis_url)
html = browser.html
soup = bs(html, 'html.parser')

hemisphere_img_ = []
download_img = []

results = soup.find("div", class_ = "result-list" )
hemispheres = results.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end = hemisphere.find("a")["href"]
        image_link = "https://marshemispheres.com/" + end    
        browser.visit(image_link)
        html = browser.html
        soup = bs(html, "html.parser")
    
       
Download = soup.find("div", class_="downloads")
img_url = Download.find("a")["href"]
    
description = soup.find("div", class_="description")
download_image= description.find("a")["href"]
    
download_img.append({"title": title, "download_url": hemisphere_url+download_image})
hemisphere_img.append({"title": title, "img_url": hemisphere_url+img_url})
_________________________________________________________________
# Print image title and url
_________________________________________________________________
hemisphere_img_df = pd.DataFrame(hemisphere_img)
hemisphere_img_df.head()

##add to new list
    mars_data = {
        "Todays_date" : todays_date,
        "Todays_news": todays_news,
        "Todays_result": todays_result
        "image_url": image_url,
        "mars_facts": tables,
        "hemisphere_image": hemisphere_img,
        "download_images" : download_img
    }
____________________________________________________________________
# Close the browser after scraping
____________________________________________________________________
 browser.quit()
________________________________________________
# Return result
________________________________________________
    return mars_data