# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:04:23 2022

@author: edgar
"""

import requests 
from bs4 import BeautifulSoup

res = requests.get("https://g1.globo.com/mundo/noticia/2022/05/08/u2-faz-show-improvisado-no-metro-de-kiev-em-solidariedade-a-ucrania.ghtml")
res.encoding = "utf-8"
print(res)

soup = BeautifulSoup(res.text, 'html.parser')

all_posts = soup.find_all(class_="content-text")
#print(res.text)
print(all_posts)