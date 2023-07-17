import csv
import copy
import random

template = {"date": "", "new_cases": 0, "deaths": 0, "recovered": 0}

data = []
with open('project1/covid_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        day_data = copy.deepcopy(template)
        day_data["date"] = row[0]
        day_data["new_cases"] = int(row[1])
        day_data["deaths"] = int(row[2])
        day_data["recovered"] = int(row[3])
        data.append(day_data)

total_cases = sum(day["new_cases"] for day in data)
total_deaths = sum(day["deaths"] for day in data)
total_recoveries = sum(day["recovered"] for day in data)


print(f"Total cases: {total_cases}")
print(f"Total deaths: {total_deaths}")
print(f"Total recoveries: {total_recoveries}")

average_cases = total_cases / len(data)
print(f"Average new cases per day: {average_cases}")


random_day = random.choice(data)
print(f"Data for {random_day['date']}:")
print(f"New cases: {random_day['new_cases']}")
print(f"Deaths: {random_day['deaths']}")
print(f"Recovered: {random_day['recovered']}")