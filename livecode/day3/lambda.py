# fiunctions in Python has a name:
# def myFunc(x, y):
#     return x+y 

# anonymous functions, using 'lambda' keyword :

# example: with one Parameter

x = lambda a: a+10

print(x(5)) # Output: 15

sum = lambda num1, num2, num3: num1 + num2 + num3

# def sum(num1, num2, num3):
#     return  num1 + num2 + num3

print(sum(5, 9))

# best usecase:

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x: x%2 != 0, numbers))
# even_numbers : this is a variable to be the list of even numbers
# list : is a constructor of list data type
# filter: is a predefines function it takes two arguments :
    # first argument is the ('lambda function') to apply the filter
    # second argument is the list to be filtered
# the proccess:
    # the filter will itrate over the list
    #  each element of the list will be 
    #  the argument of the function on its itration
    # what the function returns willm be added to the new created list 
    # out of the filter

print(odd_numbers)