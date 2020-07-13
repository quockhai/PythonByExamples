#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def  not_relative_uri(href):
	return re.compile('^https://').search(href) is  not  None

url = 'https://vnexpress.net'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

new_feeds = soup.find('section', class_='section section_topstory').find_all('a')
#, class_='', href=not_relative_uri

with open('data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['Title', 'Link'])
	for feed in new_feeds:
		writer.writerow([feed.get('title'), feed.get('href')])

# url =  'https://vnexpress.net'
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')

# new_feed = soup.find('section', class_='section section_topstory').find('a')
# title = new_feed.get('title')
# link = new_feed.get('href')
# print('Title: {}\nLink: {}'.format(title, link))