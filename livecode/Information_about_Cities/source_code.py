# Import the json module to work with JSON data
import json

# Define a function to read a JSON file
def readJsonFile(fileName):
    # Initialize an empty string to store the data
    data = ""
    # Try to open the file and read its contents
    try:
        with open(fileName) as json_file:
            # Use the json module's load function to convert the JSON data into a Python dictionary
            data = json.load(json_file)
    # If the file cannot be opened, print an error message
    except IOError:
        print("Could not read file")
    # Return the data
    return data

# Use the function to read the cities.json file
data = readJsonFile('cities.json')

# If data was successfully read from the file
if data != "" :
    # Retrieve the data for New York and Los Angeles
    city1 = data['cities']['New York']
    city2 = data['cities']['Los Angeles']
    # Calculate the distance between the two cities
    distance = abs(city1['distance_from_NYC'] - city2['distance_from_NYC'])
    # Print the distance
    print('Distance between New York and Los Angeles: ' + str(distance) + ' miles')
# If no data was read from the file, print an error message
else:
    print("Error. Exiting program")