

my_num = 600851475143

def max_prime_factor(num):
  optimus_prime = []
  divisor = 2
  while d < num:
    if num % divisor == 0:
      num /= divisor
    else:
      divisor += 1



# def prime_numbers():
#   primes = [2]
#   for i in xrange(9999):
#     for ii in xrange(2,i):
#       small_list = []
#       if i % ii != 0:
#         small_list.append(i)
#       if len(small_list) == len(xrange(2,i)):
#         primes.append(i)
#         print i
#   return primes

# print prime_numbers()