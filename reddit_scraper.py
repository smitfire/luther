import praw
import time
from pprint import pprint as pp
import inspect
import csv


def reddit_search():
  USERAGENT = "Script to search posts of certain movie titles activity by u/danger_ph0ne"
  r = praw.Reddit(user_agent=USERAGENT)
  ultimate_list = []
  with open("2007+_my_movie_shit_pre_reddit.csv", "r") as movies:
    reader    = csv.reader(movies)
    reader.next()
    for index, row in enumerate(reader):
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
        if post.score:
          posts_score.append(post.score)
        else:
          posts_score.append(0)
        comments = praw.helpers.flatten_tree(post.comments)
        for comment in comments:
          try:
            comments_score.append(comment.score)
          except Exception, e:
            print e
          else:
            comments_score.append(0)

      new_row = row + [sum(posts_score), sum(comments_score)]
      print row
      print new_row
      ultimate_list.append(new_row)

    return ultimate_list


def export_to_csv():
  with open("complete.csv", "wb") as movies:
    data   = ["title", "opening_weekend", "foreign_gross", "release_date", "posts_score", "comments_score"]
    writer = csv.writer(movies)
    writer.writerow(data)
    ultimatum = reddit_search()
    for row in ultimatum:
      print "Row has been written to CSV"
      writer.writerow(row)


export_to_csv()
