#!/usr/bin/env python
# coding: utf-8

# In[46]:


from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

URL = 'https://www.amazon.com/Harley-Davidson-Military-Graphic-T-Shirt-Ghoulish/dp/B08B8WZM3H/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1%3Aamzn1.sym.1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1&crid=23MQ2FABX0S3O&cv_ct_cx=t-shirt&keywords=t-shirt&pd_rd_i=B08B8WZM3H&pd_rd_r=cb9fc297-940e-4ec4-aca0-ffd797cfa892&pd_rd_w=OUgq0&pd_rd_wg=QjYqi&pf_rd_p=1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1&pf_rd_r=WWK0GWGPY1ATNATA6NRA&qid=1664087297&qu=eyJxc2MiOiIxMS42MiIsInFzYSI6IjExLjAxIiwicXNwIjoiMTAuMTkifQ%3D%3D&sprefix=t+shir%2Caps%2C730&sr=1-1-7a20b37c-bac4-487e-94ed-c51f283b3c9e-spons&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title=soup2.find(id='productTitle').get_text()


price_parent=soup2.find('span','a-price a-text-price a-size-medium apexPriceToPay')
price=price_parent.find('span','a-offscreen').text
price=price.strip()[1:]
title=title.strip()
price=float(price)

print(title)
print(price)
type(price)


# In[7]:


import datetime

today = datetime.date.today()

print(today)


# In[8]:


import csv
header=['Title','Price','Date']
data=[title,price,today]

with open("AmazonWebScraperDataset.csv",'w',newline='',encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
 



# In[9]:


import pandas as pd

df = pd.read_csv(r'E:\Class\VSC\Programs\Helloworld\AmazonWebScraperDataset.csv')

print(df)


# In[17]:


with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[47]:


import requests
def check_price():
    URL = 'https://www.amazon.com/Harley-Davidson-Military-Graphic-T-Shirt-Ghoulish/dp/B08B8WZM3H/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1%3Aamzn1.sym.1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1&crid=23MQ2FABX0S3O&cv_ct_cx=t-shirt&keywords=t-shirt&pd_rd_i=B08B8WZM3H&pd_rd_r=cb9fc297-940e-4ec4-aca0-ffd797cfa892&pd_rd_w=OUgq0&pd_rd_wg=QjYqi&pf_rd_p=1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1&pf_rd_r=WWK0GWGPY1ATNATA6NRA&qid=1664087297&qu=eyJxc2MiOiIxMS42MiIsInFzYSI6IjExLjAxIiwicXNwIjoiMTAuMTkifQ%3D%3D&sprefix=t+shir%2Caps%2C730&sr=1-1-7a20b37c-bac4-487e-94ed-c51f283b3c9e-spons&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    
    title=soup2.find(id='productTitle').get_text()
    price_parent=soup2.find('span','a-price a-text-price a-size-medium apexPriceToPay')
    price=price_parent.find('span','a-offscreen').text
    price=price.strip()[1:]
    title=title.strip()
    price=float(price)



    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(int(price)<35):
        send_mail()
 
 





    


# In[48]:


while(True):
    check_price()
    time.sleep(5)


# In[42]:


import pandas as pd

df = pd.read_csv(r'E:\Class\VSC\Programs\Helloworld\AmazonWebScraperDataset.csv')

print(df)


# In[34]:


import os
from email.message import EmailMessage
import ssl

def send_mail():
    email_sender='sender@gmail.com'      // change this to senders email address
    email_password='tvuhbiuhijod'        // paste your token here
    email_receiver='reciever@gmail.com'  // change this to recievers email address
    
    subject="The price has dropped. Buy fast."
    body="The link:https://www.amazon.com/Harley-Davidson-Military-Graphic-T-Shirt-Ghoulish/dp/B08B8WZM3H/ref=sxin_17_pa_sp_search_thematic_sspa?content-id=amzn1.sym.1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1%3Aamzn1.sym.1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1&crid=23MQ2FABX0S3O&cv_ct_cx=t-shirt&keywords=t-shirt&pd_rd_i=B08B8WZM3H&pd_rd_r=cb9fc297-940e-4ec4-aca0-ffd797cfa892&pd_rd_w=OUgq0&pd_rd_wg=QjYqi&pf_rd_p=1e9acbaa-83a5-4aa4-a92d-ec6cd1a07fc1&pf_rd_r=WWK0GWGPY1ATNATA6NRA&qid=1664087297&qu=eyJxc2MiOiIxMS42MiIsInFzYSI6IjExLjAxIiwicXNwIjoiMTAuMTkifQ%3D%3D&sprefix=t+shir%2Caps%2C730&sr=1-1-7a20b37c-bac4-487e-94ed-c51f283b3c9e-spons&psc=1"
    
    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Sub']=subject
    em.set_content(body)
    
    context=ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        
   
     
    
    
    
   


# In[ ]:





# In[ ]:




