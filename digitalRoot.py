# Below is a function that takes in a number, and it's behavior
# is to take that number and add each digit together, until the
# final result is a single digit answer. For example:
# An entry of 756 would be handled as 7 + 5 + 6 = 18. From there, 1 + 8 = 9.
# An entry of 756 would grand an answer of 9.

def digital_root(number):

  number_string = len(str(number))
  length = number_string
  new_number = number

  while length > 1:
    number_array = [int(i) for i in str(new_number)]
    length -= 1
    new_number = sum(number_array)

  return new_number