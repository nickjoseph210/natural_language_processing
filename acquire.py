from requests import get
from bs4 import BeautifulSoup
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

urls = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/',
        'https://codeup.com/data-science-myths/',
        'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
        'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
        'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']

def get_blog_articles(urls, cache=False):
    '''
    This function takes in a list of Codeup Blog urls and a parameter
    with default cache == False which returns a df from a csv file.
    If cache == True, the function scrapes the title and text for each url, 
    creates a list of dictionaries with the title and text for each blog, 
    converts list to df, and returns df.
    '''
    if cache == False:
        df = pd.read_csv('big_blogs.csv', index_col=0)
    else:
        headers = {'User-Agent': 'Codeup Bayes Data Science'} 

        # Create an empty list to hold dictionaries
        articles = []

        # Loop through each url in our list of urls
        for url in urls:

            # get request to each url saved in response
            response = get(url, headers=headers)

            # Create soup object from response text and parse
            soup = BeautifulSoup(response.text, 'html.parser')

            # Save the title of each blog in variable title
            title = soup.find('h1', itemprop='headline').text

            # Save the text in each blog to variable text
            text = soup.find('div', itemprop='text').text

            # Create a dictionary holding the title and text for each blog
            article = {'title': title, 'content': text}

            # Add each dictionary to the articles list of dictionaries
            articles.append(article)
            
        # convert our list of dictionaries to a df
        df = pd.DataFrame(articles)

        # Write df to csv file for faster access
        df.to_csv('big_blogs.csv')
    
    return df

# I'm going to hit Codeup's main blog page to scrape the urls

url = 'https://codeup.com/resources/#blog'
headers = {'User-Agent': 'Codeup Data Science'} 

# Request the HTML
response = get(url, headers=headers)

# Create the soup object to parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

def get_all_urls():
    '''
    This function scrapes all of the Codeup blog urls from
    the main Codeup blog page and returns a list of urls.
    '''
    # The main Codeup blog page with all the urls
    url = 'https://codeup.com/resources/#blog'
    
    headers = {'User-Agent': 'Codeup Data Science'} 
    
    # Send request to main page and get response
    response = get(url, headers=headers)
    
    # Create soup object using response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Create empty list to hold the urls for all blogs
    urls = []
    
    # Create a list of the element tags that hold the href/links
    link_list = soup.find_all('a', class_='jet-listing-dynamic-link__link')
    
    # get the href/link from each element tag in my list
    for link in link_list:
        
        # Add the link to my urls list
        urls.append(link['href'])
        
    return urls