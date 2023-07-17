# 1. Create a list of mixed data types and categorize them
#  into two separate lists: one for integers and one for strings. (5 min)

# 2. Modify the above code to categorize the values into 
# three lists: one for integers, one for strings, and one for floats. (5 min)

myList = [10, "Safwan", 15, 7.0]
integer_list = []
string_list = []
# float_list = [i for i in myList if type(i) == float]
# float_list = []

# for item in myList:
#     if type(item) == str:
#         string_list.append(item)
#     elif type(item) == int:
#         integer_list.append(item)
#     elif type(item) == float:
#         float_list.append(item)

# print(string_list)
# print(integer_list)
# print(float_list)


#----------------------------#
# 1. Create a list of your favorite fruits. Use a for loop to print 
# each fruit in the list.
# favorite_fruits = ["apple", "banana", "mango", "orange"]
# for x in favorite_fruits:
#     print(x)

# 2. Create a dictionary where the keys are country names and 
# the values are the capital of each country. 
# Use the dictionary to print the capital of a country of your choice.
# use input function

# country_dist= {"India":"Delhi", "Germany":"Berlin", "Japan":"Tokyo"}
# country = input("The name of the country is ")

# print("The capital of", country,"is", country_dist[country])


# 3. Use an if-else statement to check if a number is positive or negative.
#  Print a message accordingly.

# num = int(input("Please enter a number...    "))

# if num > 0:
#     print("Your entered number", num, "is a positive number.")
# elif num < 0:
#     print("Your entered number", num, "is a negative number.")
# else: print("Your entered number is ZERO!")


#------------------------------------#
# 1. Write a function that takes a string as input and returns the string reversed.
def reversed(string):
    reversed = ''
    for char in string:
        reversed = char + reversed
    return reversed
# print(reversed("cat"))

def res_str(s):
    return s[::-1]
# print(res_str("cat"))

# 2. Write a function that takes two numbers as inputs and returns the larger number.
def larger_number(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
# print("The larger number is", larger_number(2, 10))

# 3. Write a function that takes a list as input and 
#       returns the sum of all numbers in the list.

def sumOfList(list_of_numbers):
    return sum(list_of_numbers)

numbers_list=[1,2,88,22]

print("the total of list numbers is: ", sumOfList(numbers_list))