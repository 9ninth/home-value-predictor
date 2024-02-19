from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up the Chrome WebDriver using the Service class and ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a new browser window to the target URL
url = 'https://zillow.com/orlando-fl'
driver.get(url)

# Wait for the page to load (adjust time as necessary)
time.sleep(5)

# Now you can use BeautifulSoup to parse the page source or continue using Selenium to interact with the page
page_source = driver.page_source

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find all span elements with the specified class and data-test attribute
property_prices = soup.find_all('span', class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr", attrs={"data-test": "property-card-price"})

# Iterate through the found elements and print their text content (the prices)
for price in property_prices:
    print(price.text)

# Remember to close the browser when you're done
driver.quit()
