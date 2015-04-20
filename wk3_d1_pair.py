def variance(list):
  summation = sum(list)
  sum_of_square = sum([ num**2 for num in list ])
  mew = summation/len(list)
  var = (sum_of_square/float(len(list))) - mew**2
  return var

our_list = [3,4,4,5,6,8]

print variance(our_list)

def covariance(list1, list2):
  var1 = variance(list1)
  var2 = variance(list2)
  mew1 = sum(list1)/len(list1)
  mew2 = sum(list2)/len(list2)
  thing1 = [ num - mew1 for num in list1 ]
  thing2 = [ num - mew2 for num in list2 ]
  combined = [ a*b for a,b in zip(thing1, thing2) ]
  covar = sum(combined) / float((len(list1)-1))
  return covar


l1 = [2.1, 2.5, 4.0, 3.6]
l2 = [8, 12, 14.0, 10.0]

print covariance(l1,l2)