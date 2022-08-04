#!/usr/bin/env python
# coding: utf-8

# In[107]:


#importing libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[108]:


#pulling in the data from website 

URL = 'https://www.naaptol.com/non-calling-tablets/i-kall-entertainment-education-wi-fi-tablet-with-stand-n7/p/12610389.html?ntzoneid=9282&nts=Cat_Now_Trending&ntz=Cat_Now_Trending'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","DNT":"1","Connection":"close","Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='header').get_text()

price = soup2.find(id='square_Details').get_text()


print(title)
print(price)


# In[109]:


#clean some data to make it readable
price = price.strip()[1:]
title = title.strip()

print(price)
print(title)


# In[110]:


#creating timestamp of data collection

import datetime 
today = datetime.date.today()
print(today)


# In[111]:


#creating a csv file

import csv

header = ['title','price','date']

data = [title,price,today]
with open('NaaptolCsvDataset.csv','w',newline = '',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[112]:


#using pandas library to read the created data file which is empty right now
import pandas as pd
df = pd.read_csv(r'C:\Users\cs166\NaaptolCsvDataset.csv')
print(df)


# In[113]:


#append data to the empty csv file 

with open('NaaptolCsvDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[114]:


#combining all the actions taken into one function 

def check_price():
    URL = 'https://www.naaptol.com/non-calling-tablets/i-kall-entertainment-education-wi-fi-tablet-with-stand-n7/p/12610389.html?ntzoneid=9282&nts=Cat_Now_Trending&ntz=Cat_Now_Trending'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","DNT":"1","Connection":"close","Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='header').get_text()

    price = soup2.find(id='square_Details').get_text()

    price = price.strip()[1:]
    title = title.strip()

    import datetime 
    today = datetime.date.today()


    import csv

    header = ['title','price','date']

    data = [title,price,today]
    
    with open('NaaptolCsvDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


#checking and updating price after a certain time in our case its every 24 hours means 86400 seconds

while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


#now to again read the relatively new modified file we will use pandas

import pandas as pd
df = pd.read_csv(r'C:\Users\cs166\NaaptolCsvDataset.csv')
print(df)

#MadeByCHIRAG.SHARMA

