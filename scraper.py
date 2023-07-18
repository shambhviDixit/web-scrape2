from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome()
time.sleep(10)


browser.get(START_URL)
page=requests.get(START_URL)
soup=BeautifulSoup(page.text,'html.parser')
star=soup.find_all('table')
table_rows=star_table[7].find_all('tr')

dwarf_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Loop to find element using XPATH
        for td_tag in soup.find_all("td", attrs={"class", "dwarf"}):

            
           
            temp_list = []

            for index, td_tag in enumerate(td_tag):

                if index == 0:                   
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")

            dwarf_data.append(temp_list)

        # Find all elements on the page and click to move to the next page
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

# Calling Method    
scrape()

# Define Header
headers = ["star_name", "radius", "star_mass", "distance", "discovery_date"]

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(dwarf_data, columns=headers)

# Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
