#importing libararies
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import datetime
import smtplib

#Connect to website
URL='https://www.amazon.com/Samsung-SM-155M-DSN-Unlocked-International/dp/B0CSB22F9C/ref=sr_1_4?crid=EO1DSEJBE3JR&dib=eyJ2IjoiMSJ9.Vp-ma2M9nNeTqLdK9Pb13vOhQ_IoyKhCoz4sgD00iOuw9fe40aTosakuIGfi91Pt2AFgjpQ5VZ0e2zu7NwUOcei-V5XCTRDYwchLBhVpEmcOf85KVU7o8VwLUb5_7kd4wIMcT3GIUbClFr_GsaLCRabi4V2eUUbK66_-Ms8Y7W3x8SpMjdYhLV1p7RUGB9AL73CG22CJaR0DKscSX7H9sBM0-V5hHO1aIT_zdtzmnCw._xeC8nxBqDhW4JNCKuRqJBCnaiSoiGuJIBpOYcwN92U&dib_tag=se&keywords=cellphones&qid=1735509880&sprefix=cellphones%2Caps%2C239&sr=8-4&th=1'

# Define headers as a dictionary
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" 
}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find("span", attrs={"id":"productTitle"}).get_text().strip()

# Check if the price element exists before trying to extract text
price = soup2.find("span", attrs={"class":"a-offscreen"}).get_text().strip() 



print(title)
print(price)

import datetime

today = datetime.date.today()

print(today)

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
