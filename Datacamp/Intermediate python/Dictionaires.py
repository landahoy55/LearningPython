#This is the non-dictionary approach

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

#Basic dictionary
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Dictionairies need to have unique keys
# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france': 'paris', 'germany': 'berlin', 'norway':'oslo'}

# Print europe
print(europe)

#print the keys
print(europe.keys())

#Loop over the cities
# [print(capital) for capital in europe]

#print an element
print(europe['norway'])


#Updating a dictionary
europe['uk'] = 'london'
print(europe['uk'])


#remove an item
europe.pop('uk')

print(europe)


#A dictionary of dictionaries!!
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population': '59.83'}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)