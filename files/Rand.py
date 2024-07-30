from bs4 import *
from urllib.request import Request, urlopen
import random as rand
import enchant
from bing_image_urls import bing_image_urls
import applesmusic_abs
import Imdb_abs
import time

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d = enchant.Dict("en_US")

imdb = "https://www.imdb.com/title/"



def rand_word(num=-1, mean=-1):
    if num == -1:
        num=rand.randint(2,6)
    if mean == -1:
        mean=rand.randint(0,1)
    counter=0
    while True:
        result=""
        for i in range(num):
            result += rand.choice(alphabet)
        if d.check(result)==mean:
            break
        else:
            counter+=1
            if counter == 5000:
                return rand_word()
    return result



def rand_movie(keyword="randibabot"):
    
    if keyword == "randibabot":
        keyword=rand_word()
    
    movies = Imdb_abs.moviesearch(keyword)
    
    for i in movies:
        try:
            if Imdb_abs.getinfo_movie(imdb + i['id']+"/")['aggregateRating']['ratingCount'] >= 1000:
                    return i
        except:
            continue

    
    # while True:
    #     if userkeyword==False:
    #         keyword=rand_word()
    #     movies = Imdb_abs.moviesearch(keyword)
        
    #     try:
    #         random_index = rand.randint(0,len(movies)-1)
    #         if Imdb_abs.getinfo_movie(movies[random_index]['url'])['aggregateRating']['ratingCount'] >= 5000:
    #             e = time.time()
    #             print("try")
    #             print(e-s)
    #             return movies[random_index]
        
    #         else:
    #             for i in range(len(movies)):
    #                 if Imdb_abs.getinfo_movie(movies[i]['url'])['aggregateRating']['ratingCount'] >= 5000:
    #                     e = time.time()
    #                     print("exc")
    #                     print(e-s)
    #                     return movies[i]
    #     except:
    #         continue
            
            



def rand_game(keyword="randibabot"):
    if keyword == "randibabot":
        keyword=rand_word()
        
    games = Imdb_abs.gamessearch(keyword)
    random_index = rand.randint(0,len(games)-1)
    
    return games[random_index]



def rand_series(keyword="randibabot"):
    if keyword == "randibabot":
        keyword=rand_word()
        
    series = Imdb_abs.tvsearch(keyword)
    random_index = rand.randint(0,len(series)-1)
    
    return series[random_index]



def rand_pic(keyword="randibabot"):
    if keyword == "randibabot":
        keyword=rand_word()
    photos = bing_image_urls(keyword, limit=15)
    random_index = rand.randint(0,len(photos)-1)
    
    return photos[random_index]



def rand_music(keyword="randibabot"):
    if keyword == "randibabot":
        keyword=rand_word()
    songs = applesmusic_abs.search(keyword)['songs']
    random_index = rand.randint(0,len(songs)-1)
    
    return songs[random_index]



def rand_person(keyword):
    pass

