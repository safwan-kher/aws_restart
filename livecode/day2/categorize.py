# define a list of mixed data types
mixed_list = [9, "maher", 6.3, True, "hristomir", {"key":"value"}]

# define an empty list

empty_list = []
string_list = []
numeric_list = []
boolean_list = []

# Use for loop to categorize value
for item in mixed_list:
    # Check for strings and append it to string_list
    if type(item) == str:
        string_list.append(item)
    # Check if the type of the item is integer or float then add it to the 
    # numeric list
    elif type(item) == int or type(item) == float:
        numeric_list.append(item)
    # if the type of the item is boolean 
    # Add the item to the boolean list
    elif type(item) == bool:
        boolean_list.append(item)
    # if item has other data type then add it to the empty list
    else:
        empty_list.append(item)


# examin the lists:
print(empty_list)