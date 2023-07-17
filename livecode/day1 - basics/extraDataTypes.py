# 1. List Data Type

# Creating a list 

fruits = ["apple", "banana", "cherry"]

# Accessing list items
#print(fruits[1]) # Output banana
#print(fruits[0]) # Output apple
#print(fruits[2]) # Output cherry

# Modifying a list

fruits[1] = "blueberry"

#print(fruits)

# Using list methods

fruits.append("dragonfruit")
#print(fruits)


# Exercise:
# Create a list of your favorite movies. 
movies = ["Inception", "Matrix", "The Dark Knight"]
# Add a movie to the list, 
movies.append("Memento")
# print(movies)
# remove a movie from the list 
movies.remove("The Dark Knight")

movies = ["Inception", "Matrix", "The Dark Knight", "Apple"]
#print(movies)
# and sort the list in alphabetical order.
#print(sorted(movies))
#print(movies)
movies.sort()
#print(movies)


# 1. Tuple Data Type

# Creating  tuple
colors = ("red","green","blue")

# Accessing a tuple item

# print(colors[1]) # Output green 

# Exercise: 
# Create a tuple of the days of the week. 
daysOfWeek = ("Mon","Tue", "Wed", "Thu", "Fri", "Su", "Sa", "Su")
# print(daysOfWeek)
# Try to change one of the days. 
# daysOfWeek[5] = "Tue" # immuatble
# What happens? 
# Tuples are immuatble therefore can't be changed
# Use a method to count the number of times 
# 'Sunday' appears in the tuple.

count = daysOfWeek.count("Su")
#print(count)

length = len(daysOfWeek)

#print(length)

# 3. Dictionary Data Type

# Create a dictionary

student = {"name":"Maher","age":23, "grade":"10th"}

# Accessing dictionary items

# print(student["age"]) # Output 23 

# print(student.keys()) # Output ['name', 'age', 'grade']

# print(student.values()) # Output  ['Maher', 23, '10th']

# Exercise: 
# Create a dictionary that represents a book, 
# with keys for 'title', 'author', and 'year_published'. 
book = {"title":"Python", "author":"Safwan", "year_published":2024}
print(book)
# Change the 'year_published' to a different year. 
book["year_published"] = 2023
#print(book["year_published"])
print(book)
# Use a method to print out all the keys in the dictionary.
# print(book.keys())

