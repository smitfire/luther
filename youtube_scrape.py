import time
from pprint import pprint as pp
import inspect
import csv
import urllib2
from bs4 import BeautifulSoup as BS
import re
import json
import requests
import random

tube_class = "yt-uix-tile-link"
queryrl1 = "https://gdata.youtube.com/feeds/api/videos/"
queryrl2 = "?v=2"
utube_srch_url = "https://www.youtube.com/results?search_query="


def add_youtube_vid_ids(mycsv):
  ultimate_list = []
  with open(mycsv, "r") as movies:
    reader = csv.reader(movies)
    reader.next()
    for index, row in enumerate(reader):
      if index == 10:
        break
      full_url = utube_srch_url + row[0].replace(' ', '+')
      print full_url
      rand_t = random.randint(4,10`)
      time.sleep(rand_t)
      page = urllib2.urlopen(full_url)
      soup = BS(page)
      vid_id = soup.find(class_=tube_class).attrs.get("href").replace('/watch?v=', '')
      query_full = queryrl1 + vid_id + queryrl2
      vid_data = urllib2.urlopen(query_full)
      souptube = BS(vid_data)
      view_count = souptube.find("yt:statistics").attrs.get("viewcount")
      num_likes = souptube.find("yt:rating").attrs.get("numlikes")
      new_row = row + [ view_count, num_likes ]
      ultimate_list.append(new_row)

  return ultimate_list

add_youtube_vid_ids("complete.csv")