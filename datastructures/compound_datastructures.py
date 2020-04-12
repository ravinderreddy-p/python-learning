elements = {'hydrogen': {'number': 1,
                         'weight': 1.00794,
                         'symbol': 'H'},
            'helium': {'number': 2,
                       'weight': 4.002602,
                       'symbol': 'He'}
            }

print(elements['helium'])
print(elements.get('hydrogen'))
print(elements.get('unobtainium', 'There\'s no such element!'))
print(elements.get('helium', 'There\'s no such element!'))

print(elements['helium']['weight'])

# adding values to nested dictionary
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

print(elements)
