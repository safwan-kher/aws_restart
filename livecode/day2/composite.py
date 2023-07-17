# Import the random module

import random

# Define a list of numbers

numbers = [1,2,3,4,5]

# Define a dictionary with string keys , and number values

dictionary = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}

# Use a for loop to iterate over the numbers

#for number in numbers:
    # check if the number is even
  #  if number % 2 == 0:
        # print the even number
       # print("The number ", number, " is even.")
    # Use else statment for odd number
    #else:
      #  print("The number ", number, " is odd.")

# Use the dictionary to print the string reprentation 
# of a random number in numbers

random_number = random.choice(numbers)
print(
    "The string representation of", random_number, "is", dictionary[random_number] 
)