# The challenge given, was to build a function that takes in a number, and checks each number that numerically comes before the entered number.
# The first step is to create a list. The list is created by taking in the number passed in, and creating a range from the number 1, up TO the number passed in.
# So if 10 is passed in, the Range created is from 1 through 9, as the range goes up TO the number passed in, not INCLUDING the number passed in.
# The check iterates over each of these numbers, and IF a number can be divided down to '0' by 3 AND by 5, it is added to the multiples_list within this function.
# If the number can be divided down to '0' by only 3 OR 5, AND that number hasn't been added to the new list already, then it is added into the multiples_list.

# The multiples list will now contain only one of each possible value that matches one or more of the if/elif conditions within the function.
# The result variable takes in the multiples list as a whole at this point, and sums it up. 
# Then, the result variable is returned at the end of this functions process.

def solution(number):
    local_var = number
    number_list = list(range(1, local_var))
    multiples_list = []
    
    for num in number_list:
        if num % 3 == 0 and num % 5 == 0:
            multiples_list.append(num)
        elif num % 3 == 0 and num not in multiples_list:
            multiples_list.append(num)
        elif num % 5 == 0 and num not in multiples_list:
            multiples_list.append(num)

    result = sum(multiples_list)
    return result