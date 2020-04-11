# Tuples are similar to lists in that they store an ordered collection
# of objects which can be accessed by their indices.
# Unlike lists, tuples are IMMUTABLE. You cannot add or remove items
# from tuples or sort them in place.
# Tuples are useful when you have two or more values that are so closely
# related that they will always be used together

AngkorWat = (13.4125, 103.866667)

print(type(AngkorWat))

print("Angkor Wat is at Latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at Longitude: {}".format(AngkorWat[1]))

# Tuples can also be used to assign multiple variables in a compact way.
dimensions = 52, 40, 100   # parentheses are optional - (52, 40, 100)
print(type(dimensions))

# tuple unpacking to assign the information from a tuple into multiple
# variables without having access them one by one.
length, width, height = dimensions  # tuple unpacking

# we can assign this way: length, width, height = 52, 40, 100

print("The dimensions are {} x {} x {}.".format(length, width, height))

