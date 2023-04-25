# A program that converts more than one list a to nested dictionary.
Ids = ['S001', 'S002', 'S003', 'S004']
Names = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
Scores = [85, 98, 89, 92]

# Combine the lists into a list of tuples
myInfo = list(zip(Ids, zip(Names, Scores)))

# Create a list of nested dictionaries
Output = []
for item in myInfo:
    key, value = item
    name, score = value
    Output.append({key: {name: score}})

# Print the Output
print(Output)
