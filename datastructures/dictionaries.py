# dictionary - A data type for mutable objects. That stores mapping of
# unique keys to values. Dictionaries stores pair of elements - keys & values.
elements = {'hydrogen': 1,
            'helium': 2,
            'carbon': 6}

# we can look up values in dictionary by key.
print(elements['carbon'])

# insert new values into dictionary
elements['lithium'] = 3

print(elements)

# verify whether the key exist IN dictionary or not
is_exist = 'mithril' in elements
print(is_exist)

# dictionaries have related methods like get to fetch the corresponding key value.
print(elements.get('hydrogen'))
print(elements.get('dilithium'))

x = elements.get('dilithium')
print(x)

# identity operators (is or is not)
is_null = x is None
print(is_null)
not_null = x is not None
print(not_null)




