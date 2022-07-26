from requests import get
from bs4 import BeautifulSoup
from json import dumps, loads
from os.path import exists
from datetime import datetime

with open('conf.json') as f:
    j = loads(f.read())
    SAVE_IMAGE_PATH = j['SAVE_IMAGE_PATH']
    SAVE_JSON_PATH = j['SAVE_JSON_PATH']
    BING_URL = j['BING_URL']

re = get(BING_URL)
now = datetime.now()
year = now.year
month = now.month
day = now.day
file_name = SAVE_IMAGE_PATH + '%s-%s-%s.png' % (year, month, day)
soup = BeautifulSoup(re.text, 'lxml')
tittle = soup.find('meta', property='og:title').attrs['content']
image_url = soup.find('meta', property='og:image').attrs['content']
description = soup.find('meta', property='og:description').attrs['content']
image_re = get(image_url)
with open(file_name, 'wb') as f:
    f.write(image_re.content)
zd = []
if exists(SAVE_JSON_PATH):
    with open(SAVE_JSON_PATH, 'r', encoding='UTF-8') as f:
        zd = loads(f.read())

zd.append({'tittle': tittle, 'description': description, 'file_name': file_name})
with open(SAVE_JSON_PATH, 'w', encoding='UTF-8') as f:
    f.write(dumps(zd))
