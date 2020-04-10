# integer and float
x = int(4.7)  # x = 4
y = float(4)  # y = 4.0

print(x)
print(y)

# boolean data type with comparison operators
age = 14
is_teen = age > 12 and age < 20
not_teen = not (age > 12 and age < 20)
print(is_teen)
print(not_teen)

# strings - which are immutable order series of characters
welcome_msg = "Hello, welcome to Python world!"
print(welcome_msg)

pet_halibut = 'why should I be tarred with the epithet "lonely" merely' \
              'because I have a pet halibut?'

print(pet_halibut)

salesman = '"I think you\'re an encyclopedia salesman"'

print(salesman)

# Concatenate two strings
first_word = "Hello"
second_word = "There"
print(first_word + " " + second_word)

# Multiply the string
word = "Hello"
print(word * 5)  # Repeat the string 5 times

print(len(word))

# type conversion
house_number = 13
street_name = "Altmore Avenue"
city = "London"
print(type(house_number))

address = str(house_number) + " " + street_name + " " + city

print(address)

grams = "35.0"
print(type(grams))
print(grams)
grams = float(grams)
print(type(grams))
print(grams)

