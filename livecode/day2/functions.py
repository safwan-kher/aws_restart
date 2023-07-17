# A function in Pythin is defined by the "def" keyword

# Simple example
def add_numbers(num1, num2):
    result = num1 + num2
    #to return the result use the "return" keyword
    return result

# To call the new defiend function
#addition = add_numbers(3, 5)
#print(addition)


# reading numbers from terminal

number1 =int(input("Please enter the first number: ")) 
number2 =int(input("Please enter the second number: ")) 
sum_value = add_numbers(number1, number2)

print("The result of adding", number1, "to", number2, "is", sum_value)
