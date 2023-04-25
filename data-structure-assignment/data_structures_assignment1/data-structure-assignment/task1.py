# A program to store a given dictionary in a json file.
import json
# Define the dictionary with a variable name
myClass = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName':'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}],

    'teachers': [
        {'firstName': 'Amberly','lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}]
}

# Open a new file for writing
with open('myData', 'w') as classFile:
    # Write the dictionary to the classFile in JSON format
    json.dump(myClass, classFile)

# Open the file and load the JSON data back into a dictionary
with open('myData', 'r') as classFile:
    myClass_json = json.load(classFile)

# Print the resulting dictionary
print(myClass_json)
