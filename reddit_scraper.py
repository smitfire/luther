import praw
import time
from pprint import pprint as pp
import inspect
# search(query, subreddit=None, sort=None, syntax=None, period=None, *args, **kwargs

USERAGENT = "Script to search posts of certain movie titles activity by u/danger_ph0ne"
r = praw.Reddit(user_agent=USERAGENT)

try:
  fast7 = r.search("fast7")
except:
  print "couldnt't find a movie by that title :("
  raise

hot_movies = r.get_subreddit("movies").get_top(limit=5)
fast7_top = r.search("Fast7", subreddit="movies", limit=1)
print "fetching movie info..."


fast7_top

for movie_post in fast6_top:
  comments = praw.helpers.flatten_tree(movie_post.comments)
  for index, comment in enumerate(comments):
    print comment.score