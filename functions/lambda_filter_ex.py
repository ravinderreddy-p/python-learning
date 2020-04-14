cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]


def is_short(name):
    return len(name) < 10


for city in cities:
    print(city)
    print(is_short(city))

filter_city = list(filter(is_short, cities))

print("short cities:")
print(type(filter_city))
print(filter_city)


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
