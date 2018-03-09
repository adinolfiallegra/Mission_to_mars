
# coding: utf-8

# In[8]:


import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import tweepy
import time


# In[2]:


url = "https://mars.nasa.gov/news/"
# Retrieve page
html = requests.get(url)
# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(html.text, 'html.parser')

news_title = soup.find('div', 'content_title', 'a').text
news_p = soup.find('div', 'rollover_description_inner').text


# In[3]:


news_title


# In[10]:


# JPL Mars URL
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

# Setting up splinter
executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)

# through the pages
time.sleep(5)
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(5)
browser.click_link_by_partial_text('more info')
time.sleep(5)

# BeautifulSoup object (parse with html.parser)
html = browser.html
soup = bs(html, 'html.parser')

# Get featured image
results = soup.find('article')
extension = results.find('figure', 'lede').a['href']
link = "https://www.jpl.nasa.gov"
featured_image_url = link + extension


# In[11]:


featured_image_url


# In[12]:


# Twitter API Keys
consumer_key = "qpzxSq1Dqhe0SA8BQnyOiPm5r"
consumer_secret = "fYVqPUSIxvQmXdIbf9XHVx42BmnuFFJxiov7elb0mvLPazVAZt"
access_token = "864212572505034752-uxNQftgyE4MnfJkl1EH9URBmq33oZEu"
access_token_secret = "K3RnPep01YvMNwAKomsGboKbgyYtwKJ8P8M5txCgPgQb6"

# Tweepy Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User
target_user = "@MarsWxReport"

# Get tweet
tweet = api.user_timeline(target_user, count=1)[0]

# Store weather
mars_weather = tweet['text']


# In[13]:


mars_weather


# In[27]:


url = 'https://space-facts.com/mars/'
html = requests.get(url)
soup = bs(html.text, 'html.parser')

# Empty dict for info.
mars_profile = {}

# Get info
results = soup.find('tbody').find_all('tr')

# Stor info.
for result in results:
    key = result.find('td', 'column-1').text.split(":")[0]
    value = result.find('td', 'column-2').text
    
    mars_profile[key] = value
    
# Creat DataFrame
mars_profile_df = pd.DataFrame([mars_profile]).T.rename(columns = {0: "Value"})
mars_profile_df.index.rename("Description", inplace=True)


# In[28]:


mars_profile_df


# In[29]:


table = mars_profile_df.to_html()


# In[32]:


table.split('\n')


# In[14]:


# Mars Hemispheres URL
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

hemisphere_image_urls = []


# In[27]:



executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)

time.sleep(5)
browser.click_link_by_partial_text('Valles Marineris Hemisphere')
time.sleep(5)

#parse 
html = browser.html
soup = bs(html, 'html.parser')

valles_link = soup.find('div', 'downloads').a['href']

valles_marineris = {
    "title": "Valles Marineris Hemisphere",
    "img_url": valles_link
}

hemisphere_image_urls.append(valles_marineris)
valles_marineris


# In[21]:


#Setting up splinter
executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)

# through pages
time.sleep(5)
browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
time.sleep(5)

# BeautifulSoup object (parse with html.parser)
html = browser.html
soup = bs(html, 'html.parser')

# Store link
cerberus_link = soup.find('div', 'downloads').a['href']

# Create dict
cerberus = {
    "title": "Cerberus Hemisphere",
    "img_url": cerberus_link
}

# Append dict
hemisphere_image_urls.append(cerberus)
cerberus


# In[23]:


executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)


time.sleep(5)
browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
time.sleep(5)


html = browser.html
soup = bs(html, 'html.parser')


schiaparelli_link = soup.find('div', 'downloads').a['href']


schiaparelli = {
    "title": "Schiaparelli Hemisphere",
    "img_url": schiaparelli_link
}


hemisphere_image_urls.append(schiaparelli)


# In[ ]:


schiaparelli


# In[25]:



executable_path = {'executable_path':'/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)

time.sleep(5)
browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
time.sleep(5)


html = browser.html
soup = bs(html, 'html.parser')

syrtis_link = soup.find('div', 'downloads').a['href']

syrtis_major = {
    "title": "Syrtis Major Hemisphere",
    "img_url": syrtis_link
}

hemisphere_image_urls.append(syrtis_major)
syrtis_major

