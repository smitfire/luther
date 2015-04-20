import sys

def reverse_it(strings):
  # new_one = [ string[::-1] for string in strings.splitlines() ]
  # return '\n'.join(new_one)
  return strings[::-1].strip()




for line in sys.stdin:
  print reverse_it(line)

# input_string = raw_input()
# # print input_string
# test_string = "nick\nbrian"
# print reverse_it(input_string)
# print reverse_it(test_string)