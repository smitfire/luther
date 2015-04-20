import urllib2
from bs4 import BeautifulSoup as BS
import re
import pickle
import csv
from pprint import pprint



def movie_links(url):
  url       = url
  page      = urllib2.urlopen(url)
  soup      = BS(page)
  link_list = [ a.attrs.get('href') for a in soup.select('a[href^=/movies/?id=]') ]
  with open("movie_links.pkl", "w") as links:
    pickle.dump(link_list, links)
  return "succesfully dumped to movie_links.pkl"


def movie_data(url):
  dayrl        = "http://www.boxofficemojo.com/movies/?page=daily&view=chart&" + url.replace("/movies/?", '')
  print dayrl
  page         = urllib2.urlopen(dayrl)
  soup         = BS(page)
  daily_data   = soup.find(class_="chart-wide")
  return daily_data


#==============DRIVER CODE YOLO, WASSUP WASSUP!==================>

egpartrl   = "/movies/?id=fast7.htm"
egrl       = "http://www.boxofficemojo.com/movies/?id=fast7.htm"
egrl_daily = "http://www.boxofficemojo.com/movies/?page=daily&id=fast7.htm"
egrl_chart = "http://www.boxofficemojo.com/movies/?page=daily&view=chart&id=fast7.htm"
url        = "http://www.boxofficemojo.com/yearly/chart/?yr=2005&p=.htm"

# pprint(movie_data(egpartrl) == egrl_chart)
# print movie_links(url)

pprint(movie_data(egrl))