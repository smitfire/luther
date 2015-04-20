import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint as pp
import csv
import datetime
from dateutil.parser import parse
import matplotlib.dates as mdates

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20130101',periods=6)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })



#CHALLENGE ONE

t2015_df                   = pd.read_csv("2015.csv")
t2015_df["release date"]   = t2015_df["release date"].apply(lambda x: parse(x).date())
t2015_df["domestic gross"] = t2015_df["domestic gross"].apply(lambda x: int(x.strip("$")))

t2015_df.sort("release date")


t2015_df.plot(x="release date", y="domestic gross", style="o")
t2015_df.plot(x="release date", y="domestic gross", kind="bar")


#CHALLENGE TWO