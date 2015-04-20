import urllib2
from bs4 import BeautifulSoup as BS
import re
import pickle
import csv
from pprint import pprint

# YEAR, TOTAL GROSS, DOMESTIC GROSS, FOREIGN GROSS, LIMTED WEEKEND OPENING, WIDE WEEKEND OPENING, DISTRIBUTOR,
# Production Budget, Genre, Rating, Release Date
url1 = "http://www.boxofficemojo.com/yearly/chart/?yr="
url2 = "&p=.htm"

"http://www.boxofficemojo.com/yearly/chart/?yr=2005&p=.htm"
# dg_str = soup.find(text=re.compile("Domestic Total"))
# print dg_str.findNextSibling().text
# title_str = soup.find("title").text
# print title_str.split("(")[0].strip()


def movie_links(year):
  url  = url1 + year + url2
  page = urllib2.urlopen(url)
  soup = BS(page)
  return [ a.attrs.get('href') for a in soup.select('a[href^=/movies/?id=]') ]


def movie_info(url):
  full_url              = "http://www.boxofficemojo.com" + url
  page                  = urllib2.urlopen(full_url)
  soup                  = BS(page)
  headers               = ["title", "domestic gross", "foreign gross", "total gross", "release date", "runtime", "rating", "distributor", "youtube views"]
  title                 = soup.find("title").text.split("(")[0].strip()
  domestic_gross        = soup.find(text=re.compile("Domestic Total")).parent.parent.text.split(": ")[-1].replace(',','').split(' ')[0]
  if soup.find(text=re.compile("Worldwide")):
    total_gross = soup.find(text=re.compile("Worldwide")).parent.parent.parent.find(align="right").text.strip().replace(',','')
  else:
    total_gross = "0"
  foreign_gross         = "$" + str(int(total_gross.lstrip('$')) - int(domestic_gross.lstrip('$')))
  rating                = soup.find(text=re.compile("MPAA Rating")).parent.text.split(' ')[-1].strip()
  production_budget     = soup.find(text=re.compile("Production Budget")).parent()[0].text
  return [title, domestic_gross, foreign_gross, total_gross, release]



def export_to_csv():
  with open(year + ".csv", "w") as movies:
    data      = ["title","domestic gross","foreign gross","total gross","release date","runtime","rating","distributor"]
    writer    = csv.writer(movies)
    writer.writerow(data)
    ultimatum = ultimate_dic(year)
    for row in ultimatum:
      writer.writerow(row)


testrl  ="/movies/?page=main&id=americansniper.htm"
testrl2 ="/movies/?id=mi4.htm"
testrl3 ="/movies/?id=worldwarz.htm"
testrl4 ="/movies/?id=spongebob2.htm"

pprint(movie_info(testrl))
pprint(movie_info(testrl2))
pprint(movie_info(testrl3))
pprint(movie_info(testrl4))

# pprint(movie_links("2014"))

# pprint(ultimate_dic("2014"))

# export_to_csv("2014")
