class Object(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		template = '{0.name} {0.age}'
		return template.format (self)

# Function to return age 
def byAge_key(object): 
    return object.age

# Arrays to be sorted 
name = ['Adam', 'Bob', 'Mark']
age = [34, 41, 21]


i = 0
elements = []
# Assigning elements of class Object: name and age 
for el in name:
	people = Object(name [i], age [i])
	elements.append (people)
	i += 1

# Sort items by byAge_key function, which returns object.age 
sorting = sorted (elements, key = byAge_key, reverse = False)
