import requests, json
from bs4 import *
from urllib.request import Request, urlopen
import random as rand


def moviesearch(keyword):
    movies = []
    movieslink = "https://www.imdb.com/find/?q="+keyword+"&s=tt&ttype=ft"
    imdb = "https://www.imdb.com/title/"

    moviesreq = Request(
            url=movieslink, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
    movieswebpage = urlopen(moviesreq).read()
    
    moviessup = BeautifulSoup(movieswebpage, "html.parser")
    items = moviessup.find('script',{"id":"__NEXT_DATA__"})

    our_json = json.loads(items.text)
    
    return our_json['props']['pageProps']['titleResults']['results']

    for i in our_json['props']['pageProps']['titleResults']['results']:
        result = {}
        result['name'] = i['titleNameText']
        try:
            result['year'] = i['titleReleaseText']
        except:
            result['year'] = "0000"
        result['type'] = i['titleTypeText']
        try:
            result['img'] = i['titlePosterImageModel']['url']
        except:
            result['img'] = "https://lightwidget.com/wp-content/uploads/localhost-file-not-found.jpg"
        result['url'] = imdb+i['id']+"/"
        movies.append(result)
    return movies

def tvsearch(keyword):
    tv = []
    tvlink = "https://www.imdb.com/find/?q="+keyword+"&s=tt&ttype=tv&ref_=fn_tv"
    imdb = "https://www.imdb.com/title/"


    tvreq = Request(
            url=tvlink, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
    tvwebpage = urlopen(tvreq).read()
    
    tvsup = BeautifulSoup(tvwebpage, "html.parser")
    items = tvsup.find('script',{"id":"__NEXT_DATA__"})

    our_json = json.loads(items.text)

    for i in our_json['props']['pageProps']['titleResults']['results']:
        result = {}
        result['name'] = i['titleNameText']
        try:
            result['year'] = i['titleReleaseText']
        except:
            result['year'] = "0000"
        result['type'] = i['titleTypeText']
        try:
            result['img'] = i['titlePosterImageModel']['url']
        except:
            result['img'] = "https://lightwidget.com/wp-content/uploads/localhost-file-not-found.jpg"
        result['url'] = imdb+i['id']
        tv.append(result)
    return tv

def gamessearch(keyword):
    games = []
    gameslink = "https://www.imdb.com/find/?q="+keyword+"&s=tt&ttype=vg&ref_=fn_vg"
    imdb = "https://www.imdb.com/title/"

    gamesreq = Request(
            url=gameslink, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
    gameswebpage = urlopen(gamesreq).read()
    
    
    tvsup = BeautifulSoup(gameswebpage, "html.parser")
    items = tvsup.find('script',{"id":"__NEXT_DATA__"})

    our_json = json.loads(items.text)

    for i in our_json['props']['pageProps']['titleResults']['results']:
        result = {}
        result['name'] = i['titleNameText']
        try:
            result['year'] = i['titleReleaseText']
        except:
            result['year'] = "0000"
        result['type'] = i['titleTypeText']
        try:
            result['img'] = i['titlePosterImageModel']['url']
        except:
            result['img'] = "https://lightwidget.com/wp-content/uploads/localhost-file-not-found.jpg"
        result['url'] = imdb+i['id']
        games.append(result)
    return games
    
def peoplesearch(keyword):
    people = []
    peoplelink = "https://www.imdb.com/find/?q="+keyword+"&s=nm&ref_=fn_nm"
    imdb = "https://www.imdb.com/name/"

    peoplereq = Request(
            url=peoplelink, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
    peoplewebpage = urlopen(peoplereq).read()
    
    peoplesup = BeautifulSoup(peoplewebpage, "html.parser")
    items = peoplesup.find('script',{"id":"__NEXT_DATA__"})

    our_json = json.loads(items.text)

    for i in our_json['props']['pageProps']['nameResults']['results']:
        result = {}
        result['name'] = i['displayNameText']
        result['job'] = i['knownForJobCategory']
        try:
            result['aka'] = i['akaName']
        except:
            result['aka'] = ""
        try:
            result['img'] = i['avatarImageModel']['url']
        except:
            result['img'] = "https://lightwidget.com/wp-content/uploads/localhost-file-not-found.jpg"
        result['url'] = imdb+i['id']
        people.append(result)
    return people



def getinfo_movie(link):
    
    req = Request(
            url=link, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
    webpage = urlopen(req).read()
    
    sup = BeautifulSoup(webpage, "html.parser")
    
    items = sup.find('script', {'type':"application/ld+json"})
    our_json = json.loads(items.text)
    
    return our_json
