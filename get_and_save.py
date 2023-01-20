from requests import get
from bs4 import BeautifulSoup
from json import dumps, loads
from os.path import exists
from datetime import datetime
from page import page

with open('conf.json') as f:
    j = loads(f.read())
    SAVE_IMAGE_PATH = j['SAVE_IMAGE_PATH']
    SAVE_JSON_PATH = j['SAVE_JSON_PATH']
    BING_URL = j['BING_URL']

re = get(BING_URL, headers={
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'})
now = datetime.now()
year = now.year
month = now.month
day = now.day
file_name = '%s-%s-%s.png' % (year, month, day)
soup = BeautifulSoup(re.text, 'lxml')
tittle = soup.find('meta', property='og:title').attrs['content']
image_url = soup.find('meta', property='og:image').attrs['content']
description = soup.find('meta', property='og:description').attrs['content']
location = soup.find('a', class_='title').text
long_url = soup.find('a', class_='title').attrs['href']

image_re = get(image_url)
with open(SAVE_IMAGE_PATH + file_name, 'wb') as f:
    f.write(image_re.content)

long_re = get(BING_URL + long_url, headers={
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'})
long_soup = BeautifulSoup(long_re.text.replace('<br>', '\n'), 'lxml')
long_description = long_soup.find('div', id='ency_desc_Prom').text

zd = []
if exists(SAVE_JSON_PATH.replace('*', '')):
    with open(SAVE_JSON_PATH.replace('*', ''), 'r', encoding='UTF-8') as f:
        zd = loads(f.read())
zd.append({'tittle': tittle, 'location': location, 'description': description,
          'long_description': long_description, 'file_name': file_name})

with open(SAVE_JSON_PATH.replace('*', ''), 'w', encoding='UTF-8') as f:
    f.write(dumps(zd))
page()
