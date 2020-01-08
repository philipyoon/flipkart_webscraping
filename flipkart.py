from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/Users/philipyoon/Downloads/chromedriver")

products = [] # list to store name of product
prices = []
ratings = []
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")

# find() returns first instance of tag 'div'
# find_all() returns a list of all tagged with 'a', have to iterate through

for a in soup.find_all('a',href=True, attrs={'class':'_31qSD5'}):
    name = a.find('div', attrs={'class':'_3wU53n'})
    price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    print((name.get_text))
    products.append(name.get_text())
    prices.append(price.get_text())
    ratings.append(rating.get_text()) 

'figure out how to get text from whatever a.find() returns'