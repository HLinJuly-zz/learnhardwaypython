states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."


city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is : %s" % city

print cities[0]  # wrong

# What if I need a dictionary, but I need it to be in order?
# Take a look at the collections.OrderedDict data structure in Python. Search for it online to find the documentation.
