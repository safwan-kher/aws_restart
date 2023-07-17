# Step 1: Import Necessary Libraries
import csv
import random

# Step 2: Read the CSV File
with open('project3/movie_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    movies = list(reader)

# Step 3: Create a List of Dictionaries
movies_dict = [{ 'title': movie[0], 'year': movie[1], 'genre': movie[2], 'rating': float(movie[3]) } for movie in movies]

# Step 4: Calculate and Print the Number of Movies in Each Genre
genre_counts = {}
for movie in movies_dict:
    if movie['genre'] in genre_counts:
        genre_counts[movie['genre']] += 1
    else:
        genre_counts[movie['genre']] = 1
print('Number of movies in each genre:', genre_counts)

# Step 5: Calculate and Print the Average Rating for Each Genre
genre_ratings = {}
for movie in movies_dict:
    if movie['genre'] in genre_ratings:
        genre_ratings[movie['genre']].append(movie['rating'])
    else:
        genre_ratings[movie['genre']] = [movie['rating']]
average_ratings = { genre: sum(ratings) / len(ratings) for genre, ratings in genre_ratings.items() }
print('Average rating for each genre:', average_ratings)

# Step 6: Calculate and Print the Number of Movies Released Each Year
year_counts = {}
for movie in movies_dict:
    if movie['year'] in year_counts:
        year_counts[movie['year']] += 1
    else:
        year_counts[movie['year']] = 1
print('Number of movies released each year:', year_counts)

# Step 7: Select and Print a Random Movie
random_movie = random.choice(movies_dict)
print('Random movie:', random_movie)