# Assigning variables, lists, and dictionaries

# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

# On the next line, create a new dictionary by entering: 
 
pKR = {}

# To fill the dictionary with key-value pairs, insert the first key of y with a value of 10.07. Place the cursor inside the braces, and enter: 
# 'y': 10.07,
# 'c': 8.18
# 'k': 10.53
# 'h': 6.00
# 'r': 12.48
# 'd': 3.65
# 'e': 4.25
pKR = {
    'y':10.07,
    'c': 8.18,
    'k':10.53,
    'h':6.00,
    'r':12.48,
    'd':3.65,
    'e':4.25
}


# Using count() to count the numbers of each amino acid
# In this exercise, you will use the count() method and list comprehension to count the number of Y, C, K, H, R, D, 
# and E amino acids. 
# These amino acids contribute to the net charge.

# To identify a count of an item within a list, you can use the count() method. 
# To see how many amino acids in insulin are Y, 
# use the count() method by entering: 
insulin.count("Y")

# Next, update the insulin.count() line by casting the variable returned by the count() method as a float: 
float(insulin.count("Y"))

# Now that you have the basis for identifying a single entity, you can use this method to find all entities from a list.
#  This process can be done by using list comprehension. 
# For the entire line, enter: 
# explaining the code :
# This line of code is creating a dictionary in Python using a dictionary comprehension. Let's break it down step by step:

# 1. `seqCount =` : This is an assignment statement. It means that the result of the expression on the right side of the equals sign will be stored in the variable `seqCount`.

# 2. `{x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']}` : This is a dictionary comprehension. 
# It's a compact way of creating a new dictionary.

# 3. `for x in ['y','c','k','h','r','d','e']` : This is a for loop that iterates over the list 
# `['y','c','k','h','r','d','e']`. For each iteration, the variable `x` takes on the value of the next item in the list.

# 4. `x: float(insulin.count(x))` : This is the expression that generates the keys and values for the new dictionary. 
# For each iteration of the for loop, a new key-value pair is added to the dictionary. 
# The key is the current value of `x`, and the value is the result of the expression `float(insulin.count(x))`.

# 5. `float(insulin.count(x))` : This expression is calling the `count` method on the `insulin` object 
# (which is presumably a list or some other iterable), passing it the current value of `x`. 
# The `count` method returns the number of times `x` appears in `insulin`. 
# This number is then converted to a float by the `float` function.

# So, in summary, this line of code is creating a new dictionary where the keys are the characters 
# 'y', 'c', 'k', 'h', 'r', 'd', 'e', and the values are the number of times each character appears in `insulin`, 
# converted to a float.

seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})


# Note: The first two steps in this exercise are predecessors to the third step.

# Writing the net charge formula

# In this exercise, you will construct the net charge formula. 
# You will use the provided netCharge variable in a Python-based net charge formula.
# The function for the formula includes a while loop that will print the net charge 
# while the pH variable is equal to or below 14.

# Create a variable called pH and initialize it to zero by entering 
pH = 0 
# and pressing ENTER.

# Create the while loop by entering 
while (pH <= 14): 
# and pressing ENTER.

# Copy the following netCharge variable and paste it at the beginning of the while loop.
    #This code is calculating the net charge of a protein sequence at a specific pH. Here's a breakdown of the code with comments:


# The netCharge variable is calculated as the sum of the positive charges minus the sum of the negative charges
    netCharge = (
        # The positive charges are calculated for the amino acids 'k', 'h', 'r'
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))  # For each of these amino acids, 
        # the charge is calculated using the Henderson-Hasselbalch equation 
        # for basic amino acids, then all the charges are summed up
        # The negative charges are calculated for the amino acids 'y', 'c', 'd', 'e'
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values()))  # For each of these amino acids, 
        # the charge is calculated using the Henderson-Hasselbalch equation for acidic amino acids,
        # then all the charges are summed up
    )


#  In the Henderson-Hasselbalch equation, `pH` is the pH of the solution, 
# `pKR[x]` is the pKa of the amino acid (a measure of its acidity), 
# and `seqCount[x]` is the number of times the amino acid appears in the sequence. 
# The `10**` part is calculating 10 raised to the power of the value in the brackets, 
# which is part of the equation. The `.values()` method is used to get the values from 
# the dictionary created by the dictionary comprehension, 
# and `sum()` is used to add up these values.


# To print the netCharge variable with the pH, use a format string for better readability. 
# Enter :
print('{0:.2f}'.format(pH), netCharge) # and press ENTER.

# Finally, increment the pH variable by entering 
pH +=1 # and pressing ENTER.

# Be careful about indentation and spacing in Python

# Subsets of Python code are organized by indentation and spaces. In Python, even one misplaced indentation or space can throw an exception or other error. For example, be sure that every item within your while loop is properly indented so the code will work.

# Congratulations! You have worked with lists and loops in a Python function.

