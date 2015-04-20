import numpy as np
import pandas as pd
import matplotlib as plt
import operator

our_list = [2, 7, 1, 5, 10]


solverlist={}
def solver():
  our_range = np.linspace(0.0, 10.0, num=100)
  for num in our_range:
    ourlist=[]
    for something in our_list:
      ourlist.append((something - float(num))**2)

    solverlist[sum(ourlist)] = num

solver()

sorted_x = sorted(solverlist.items(), key=operator.itemgetter(0))
print sorted_x[0]

df = pd.DataFrame(sorted_x)
df.plot()