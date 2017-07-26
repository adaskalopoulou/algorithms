
# coding: utf-8

# In[30]:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from twilio.rest import Client


# In[34]:

account_sid = "XXXXXXX"
auth_token = "XXXXXX"
client = Client(account_sid, auth_token)


# In[31]:

response = requests.get("https://www.nytimes.com/")
doc = BeautifulSoup(response.text, 'html.parser')


# In[32]:

story = doc.find_all('h2', { 'class': 'story-heading' })
headline = story[0].text.strip()
print(headline)


# In[41]:

prior = open("my_nyt.txt")
prior_headline = prior.read().strip()
print(prior_headline)


if headline != prior_headline:
# https://programminghistorian.org/lessons/working-with-text-files
  f = open("my_nyt.txt", "w")
  f.write(headline)
  f.close()
  message = client.api.account.messages.create(to="XXXX",
                                             from_="XXXX",
                                             body="NEW HEADLINE:"+ headline)
  print(message.sid)




