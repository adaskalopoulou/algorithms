
# coding: utf-8

# In[30]:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from twilio.rest import Client


# In[34]:

account_sid = "AC837978a8d6f70d438427814cf2ed60ce"
auth_token = "f8c0f3263a16dac983a9fe76566c9638"
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


# In[43]:

message = client.api.account.messages.create(to="+41763610759",
                                             from_="+41798073572",
                                             body="NEW HEADLINE:"+ headline)


# In[44]:

if headline != last_headline:
    print(message.sid)

