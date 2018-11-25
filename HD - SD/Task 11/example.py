# The location data which we obtain from Google is in a JSON format
# JSON stands for JavaScript Object Notation, and is used very commonly in the web
# Don't get put off by the long acronym, JSON is actually very simple
# JSON just stores data in key-value pairs which is really easy for humans to read and understand
# Furthermore, it is almost identical to a python dictionary
# Look at the file example.json, it is a simple example of what a JSON file looks like
# As you will see, the JSON file format is almost identical to a Python dictionary!
# This is how we read such a file

import json  # We will use the json library here
json_file = open('example.json')
json_string = json_file.read()  # Read the contents of the file into a string
json_data = json.loads(json_string)  # Load the data from the json file into a Python dictionary

print('His name is', json_data["name"], "and his age is", json_data["age"])

# How do we check if a particular key is in the json file?
if "age" in json_data:  # Returns true because this is a key in the file
    print("Age is a key in the json file")
    
if "school" in json_data:  # Returns false because this attribute is not in the file
    print("School is a key in the json file")
else:
    print("School is not a key in the json file")

# Now let us look at a more complicated JSON file.
# Example.py has an array of two people
# This is an example of how we can read an array of records

print("\nReading a more complicated JSON file \n")
json_file = open('example2.json')
json_string = json_file.read()  # Read the contents of the file into a string
json_data = json.loads(json_string)  # Load the data from the json file into a Python dictionary

people = json_data["people"]  # In the JSON file, the "people" key stores an array of objects. Here, we are reading
# all the data stored in the "people" key into a Python list.

for person in people:
    print(person["name"], person["surname"], person["age"])

# This is all you need to know about JSON to complete this task!
