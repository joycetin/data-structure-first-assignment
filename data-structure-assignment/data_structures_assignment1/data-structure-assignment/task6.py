#A dictionary that maps the names of countries to their respective capital cities with a prompt.
# Define the dictionary of countries and their capitals
countries = {
    
    "France": "Paris",
    "Brazil": "Brasilia",
    "India": "New Delhi",
    "Uganda":"Kampala",
    "Chad":"Indjimena",
    "Tunisia":"Tunis",
    "USA": "Washington ",
    "Japan": "Tokyo"
}

# Ask user to input a country name
country = input("Enter a country name: ")

# Check if the country is in the dictionary
if country in countries:

# If it is, print the capital
    print(f"The capital of {country} is {countries[country]}.")

else:
# If not, print an error message
    print("Sorry, we don't have information about that country.")
