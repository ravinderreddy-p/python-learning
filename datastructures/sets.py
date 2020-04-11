countries = ['Angola', 'India', 'Maldives', 'India', 'United States', 'India',
             'China', 'United States', 'Russia', 'India', 'China']

print(len(countries))

countries_set = set(countries)
print(countries_set)
print(len(countries_set))

print('India' in countries_set)

# add elements to set by add() method
countries_set.add('Italy')
print(countries_set)

# remove the random element from list
countries_set.pop()
print(countries_set)
