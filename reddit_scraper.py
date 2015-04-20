import praw
import time
from pprint import pprint as pp
import inspect
import csv

# search(query, subreddit=None, sort=None, syntax=None, period=None, *args, **kwargs

date_time = '29.08.2011 11:05:02'
pattern = '%d.%m.%Y %H:%M:%S'
epoch = int(time.mktime(time.strptime(date_time, pattern)))
# print epoch




def reddit_search():
  USERAGENT = "Script to search posts of certain movie titles activity by u/danger_ph0ne"
  r = praw.Reddit(user_agent=USERAGENT)
  ultimate_list = []
  with open("2007+_my_movie_shit_pre_reddit.csv", "r") as movies:
    reader    = csv.reader(movies)
    reader.next()
    for index, row in enumerate(reader):
      if index==1:
        break
      date_time = row[-1] + " 00:00:00"
      pattern = '%Y-%m-%d %H:%M:%S'
      epoch_start = int(time.mktime(time.strptime(date_time, pattern)))
      epoch_end = epoch_start + 604761
      time_range = 'timestamp:'+ str(epoch_start) + '..' + str(epoch_end)
      print "searching reddit/r/movies for " + row[0] + " between " + time_range
      ressy_res_res = r.search(query=row[0], subreddit="movies", period=time_range, limit=10)
      posts_score = []
      comments_score = []
      for post in ressy_res_res:
        posts_score.append(post.score)
        comments = praw.helpers.flatten_tree(post.comments)
        for comment in comments:
          comments_score.append(comment.score)

      print "sum of posts = " + str(sum(posts_score))
      print "sum of comments = " + str(sum(comments_score))


reddit_search()

# hot_movies = r.get_subreddit("movies").get_top(limit=5)
# fast7_top = r.search("Fast7", limit=10, )
# print "fetching movie info..."


# fast7_top

# for movie_post in fast7_top:
#   comments = praw.helpers.flatten_tree(movie_post.comments)
#   for index, comment in enumerate(comments):
#     print comment.score