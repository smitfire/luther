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

  if soup.find(text=re.compile("Release Date:")):
    release_date = soup.select("a[href^=/schedule/?view=bydate]")[0].attrs.get("href").split("&")[-2].replace('date=', '')
  else:
    release_date = None

  return title, opening_weekend, foreign_gross, release_date


def remove_noise_chars(string):
  return re.sub("[^0-9]", "", string)


def open_pkl_pages(my_file):
  ultimate_list=[]
  with open(my_file, "r") as movie_pages:
    parsed_movie_pages = pkl.load(movie_pages)
    for index, (url, contents) in enumerate(parsed_movie_pages.items()):
      soup      = BS(contents)
      release_date = soup.find("title").text.split("(")[-1].split('-')[0].replace(')','')
      if soup.find(text=re.compile("Opening Weekend")) and soup.find(text=re.compile("Foreign:")) and int(release_date) and int(release_date) > 2007:

        ultimate_list.append(movie_info(soup))
  return ultimate_list

def export_to_csv(my_file):
  with open("2007+_my_movie_shit_pre_reddit.csv", "wb") as movies:
    data      = ["title", "opening_weekend", "foreign_gross", "release_date"]
    writer    = csv.writer(movies)
    writer.writerow(data)
    ultimatum = open_pkl_pages(my_file)
    for row in ultimatum:
      print "Row has been written to CSV"
      writer.writerow(row)


export_to_csv("../page_data.pkl")
# pprint(open_pkl_pages("../page_data.pkl"))
# pprint(len(open_pkl_pages("../page_data.pkl")))

# with open("page_data.pkl", "r") as movie_pages:
#   parsed_movie_pages = pkl.load(movie_pages)


