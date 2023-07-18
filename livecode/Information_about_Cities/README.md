# Exercise: Creating a JSON File Handler for Retrieving Information about Cities

## Lab Overview
In this lab, you will:

1. Create a JSON file that contains information about different cities, their locations, and distances from a reference point.
2. Create a Python module to read the JSON file and retrieve the city data.
3. Calculate the distance between two cities using the given data.

## Estimated Completion Time
15 minutes

## Exercise 1: Creating the JSON Cities Data File
This JSON document stores information about different cities, their coordinates (latitude and longitude), and their distances from a reference point (in this case, New York City).

Create a new file and name it `cities.json`. Copy and paste the following code into this newly created file:

```json
{
   "cities":{
      "New York":{
         "coordinates": [40.7128, -74.0060],
         "distance_from_NYC": 0
      },
      "Los Angeles":{
         "coordinates": [34.0522, -118.2437],
         "distance_from_NYC": 2445
      },
      "Chicago":{
         "coordinates": [41.8781, -87.6298],
         "distance_from_NYC": 713
      },
      "Houston":{
         "coordinates": [29.7604, -95.3698],
         "distance_from_NYC": 1420
      },
      "Phoenix":{
         "coordinates": [33.4484, -112.0740],
         "distance_from_NYC": 2145
      }
   }
}
```

## Exercise 2: Creating the JSON File Handler Module
In this task, you create a module that reads the JSON file and returns the JSON document.

Create a new Python file and name it `jsonFileHandler.py`. Copy and paste the following code into this file:

```python
import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
```

## Exercise 3: Creating the Main Program
You create the main program that parses the JSON data and calculates the distance between two cities.

Create a new Python file and name it `calc_distance.py`. Copy and paste the following code into this file:

```python
import jsonFileHandler

data = jsonFileHandler.readJsonFile('cities.json')

if data != "" :
    city1 = data['cities']['New York']
    city2 = data['cities']['Los Angeles']
    distance = abs(city1['distance_from_NYC'] - city2['distance_from_NYC'])
    print('Distance between New York and Los Angeles: ' + str(distance) + ' miles')
else:
    print("Error. Exiting program")
```

You can run the program to see if the data is well retrieved. The result should be as follows:

```
Distance between New York and Los Angeles: 2445 miles
```

## End Lab

This lab demonstrated how to create a JSON file, a Python module to read the JSON file, and a main program to use the module and calculate the distance between two cities. You can modify the JSON file to add more cities and their data, and modify the main program to calculate distances between different cities.