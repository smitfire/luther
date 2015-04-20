import urllib2
from bs4 import BeautifulSoup as BS
import re
import pickle as pkl
import csv
from pprint import pprint

def movie_info(soup):
  headers = ["title", "domestic gross", "foreign gross", "total gross", "release date", "runtime", "rating", "distributor", "youtube views"]
  title = soup.find("title").text.split("(")[0].strip()

  if soup.find(text=re.compile("Foreign:")):
    foreign_gross = remove_noise_chars(soup.find(text=re.compile("Foreign:")).parent.parent.parent.text.strip().split()[-2])
  else:
    foreign_gross = 0

  if soup.find(text=re.compile("Opening Weekend")):
    opening_weekend = remove_noise_chars(soup.select('a[href^=/weekend/chart/?yr=]')[0].parent.next_sibling.text)
  else:
    opening_weekend  = 0

  return title, opening_weekend, foreign_gross


def remove_noise_chars(string):
  return re.sub("[^0-9]", "", string)



def open_pkl_pages(file):
  with open(file, "r") as movie_pages:
    parsed_movie_pages = pkl.load(movie_pages)
    for index, movie_page in enumerate(parsed_movie_pages):
      soup_page = urllib2.urlopen(movie_page)
      soup      = BS(soup_page)
      if soup.find(text=re.compile("Opening Weekend")):
        print movie_info(soup)


open_pkl_pages("../page_data.pkl")

# with open("page_data.pkl", "r") as movie_pages:
#   parsed_movie_pages = pkl.load(movie_pages)
