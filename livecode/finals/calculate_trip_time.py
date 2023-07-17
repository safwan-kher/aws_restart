# Exerise Instructions:
# 1. Store the avarage dpeed between each city in a dictionary.
# e.g. 
#  speeds =  {
#     "CityA_CityB":60,
#     "CityB_CityC":70,
#     "CityC_CityD":80,
#     "CityD_CityE":90,
# }
# 2. Write a function to calcualte the 
# total time of a trip between a start_citya and end_city
# 3. print the total time to the console

# Step 1: Store the avarage dpeed between each city in a dictionary.

speeds =  {
    "CityA_CityB":60,
    "CityB_CityC":70,
    "CityC_CityD":80,
    "CityD_CityE":90,
}

# Step 2: define cities :
cities = ["CityA", "CityB", "CityC", "CityD", "CityE"]

# Step 3: define the distances
distance = {
    "CityA_CityB":100,
    "CityB_CityC":200,
    "CityC_CityD":300,
    "CityD_CityE":400,
}

# also we assume that you have created a functionm to valculate the distance :
# from last phase : 
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


# Step 4: write a function to calculate 
# the time to drive between start_city and end_city:
def calculate_time(start_city, end_city, cities, distance, speeds):
    # define the result to be returned 
    total_time = 0

    # bring the indexes of start and end cities:
    start_index = cities.index(start_city)
    end_index = cities.index(end_city)

    # loop through the cities rang from start to the end city index
    for i in range(start_index, end_index):
        key=cities[i] + "_" + cities[i+1]
        total_time += distance[key] / speeds[key]
    # convert the totzal time into minutes
    total_time = round(total_time, 2)
    total_time = round(total_time * 60 , 2)

    # return the time
    return total_time

# try the function
time = calculate_time("CityA", "CityE", cities, distance, speeds)
print("The time between CityA and CityE is", time , "minutes")




