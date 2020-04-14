# filter() is a higher-order built-in function that takes a function and iterable as inputs and
# returns an iterator with the elements from the iterable for which the function returns True.

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]


def is_short(name):
    return len(name) < 10


for city in cities:
    print(city)
    print(is_short(city))

filter_city = list(filter(is_short, cities))

# lambda expression for above code as below:
filter_cities = list(filter(lambda city: len(city) < 10, cities))

print("short cities:")
print(type(filter_city))
print(filter_city)
print(filter_cities)


# example - 2:
# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# function that filters vowels
def filter_vowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if alphabet in vowels:
        return True
    else:
        return False


filteredVowels = filter(filter_vowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

# lambda expression for above code:
filtered_vowels_lambda = list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], alphabets))
print(filtered_vowels_lambda)
