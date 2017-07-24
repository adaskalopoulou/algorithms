import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

response = requests.get("http://www.sciencemag.org/")
doc = BeautifulSoup(response.text, 'html.parser')

stories = doc.find_all('article', { 'class': 'media' })

all_stories = []

for story in stories:
    headline = story.find('h2', {'class': 'media__headline'})
    if headline:
        headline_text = headline.text.strip()
        this_story = { 'headline': headline_text }
        byline = story.find('p', {'class': 'byline'})
        link = story.find('a')
        if byline:
           byline_text = byline.text.strip()
           this_story['byline'] = byline_text 
        if headline:
            this_story['link'] = link['href']

        all_stories.append(this_story)

all_stories[0:10]

my_10 = all_stories[0:10]
stories_df = pd.DataFrame(my_10)

stories_df['news_link'] = "http://www.sciencemag.org/"+ stories_df.link
del stories_df['link']
stories_df.to_csv("science.csv")


datestring = time.strftime("%Y-%m-%d-%H-%M")

filename = "science-data-" + datestring + ".csv"
stories_df.to_csv(filename, index=False)
