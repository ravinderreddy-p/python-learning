# loop is used to iterate, or do something repeatedly over an iterable.
# An iterable is an object that can return one of it's elements at a time.

# example - 1
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

# example - 2
# using the range() function with for loops.
for i in range(3):
    print(i)
    print("hello")

# example - 3
# range(start=0, stop, step=1) - here 1st & 3rd args are optional
for i in range(1, 10, 2):
    print(i)

# example - 4
# range(start=0, stop)
for i in range(2, 6):
    print(i)

# Creating and modifying the lists
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

# modify the list by using range() function.
for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)

# build a dictionary from list
book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlok',
              'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of',
              'huckleberry', 'fin']
# create an empty dictionary
word_counter = {}

# iterate through each element in the list to count words.
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# iterate the list using get() method same as above
word_counter_get = {}
for word in book_title:
    word_counter_get[word] = word_counter_get.get(word, 0) + 1
print(word_counter_get)

# Iterating through dictionaries with for() loops
cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

# Iterating through dictionary gives you keys.
for key in cast:
    print(key)

# to iterate through both keys and values, we can use built-in method items().
# items() returns tuple of key, value pairs.
for key, value in cast.items():
    print("Actor: {} Role: {} ".format(key, value))
