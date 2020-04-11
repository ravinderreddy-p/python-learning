# A list is data structure in Python that is mutable ordered sequence of elements.

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

# we can look up individual elements in the list by it's index.
# months[index]
print(months[0])
print(months[1])
print(months[7])

# we can also index from the end of the list by specifying '-ve'.
print(months[len(months) - 1])
print(months[-1])
print(months[-2])

# Lists can contain any mix and match of the data types.
list_of_random_things = [1, 3.4, 'a string', True]

print(list_of_random_things[0])
print(list_of_random_things[1])
print(list_of_random_things[-1])

# Slicing of the list
# months[start_index:end_index] - inclusive start_index and exclusive end_index
q3 = months[6:9]
print(q3)

# To get the 1st few of the list elements
# months[:end_index] - start index considered as 0.
first_half = months[:6]
print(first_half)

# To get the last few list elements
# months[start_index:] - end_index considered as 'length of list - 1'
second_half = months[6:]
print(second_half)

# Membership operators in List
print('Sunday' in months)
print('Sunday' not in months)

# Lists are mutable - you can change the items in list.
months[0] = 'Jan'  # January has replaced by Jan.
print(months)

# Strings are Immutable - you can't change them.
greetings = "Hello there"
# greetings[0] = 'M' # we will get this error - TypeError: 'str' object does not support item assignment

# Both strings and Lists are ordered but list is mutable and strings are immutable.





