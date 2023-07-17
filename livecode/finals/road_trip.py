 # Exercise Instructions:
 # 1. Store the sequence of cities in a list.
 #  e.g. cizies = ["CityA", "CityB", ..etc]
 # 2. Store the distnace of the cities in a dictionary.
 # e.g. distance = {
 # "CityA_CityB":100, 
 # "CityB_CityC":200,
 # ...etc
 # }
 # 3. Write a function to calculate the total distance of the trip from a start_city and end_city.
 # 4. Print the total ditsance to the console.
 
 # Step 1: store the sequence in a list



cities = ["CityA", "CityB", "CityC", "CityD", "CityE"]

# Step 2: store the distance between cities in a dictionary
distance = {
    "CityA_CityB":100,
    "CityB_CityC":200,
    "CityC_CityD":300,
    "CityD_CityE":400,
}

# Step 3: create a function to calculate th total distance of a trip


def calculate_total_distance(start_city, end_city,cities, distance):
    # define a result to be returned
    total_distance = 0

    # make sure start_city, end_city are in our system
    # example : start_city: "cityA", end_city:"city_D"
    start_index = cities.index(start_city) # 1
    end_index = cities.index(end_city) # 3
    # find the  start_city as a start in a properpty in distance
    # find end_city as an end in a properpty in distance
    for i in range(start_index, end_index):
        key=cities[i]+"_"+cities[i+1] # i:2 (key:"CityC_CityD")
        total_distance += distance[key] # i:2 distance["CityC_CityD"] = 300
    
    return total_distance

# try your function
print("The distance between CityB and CityD is: ")
print(calculate_total_distance("CityB","CityD",cities, distance))