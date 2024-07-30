import requests, json
from bs4 import *
from urllib.request import Request, urlopen
import random as rand
import enchant
import time

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d = enchant.Dict("en_US")

def rand_music(keyword):
    results = []
    link = "https://www.deezer.com/search/"+keyword+"/track"
    
    req = Request(
        url=link, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    
    sup = BeautifulSoup(webpage, "html.parser")
