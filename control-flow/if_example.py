# if statement is conditional statement that runs or skips code based on
# whether a condition is true or false.
phone_balance = 4
bank_balance = 100

print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)

# Second example
number = 146
if number % 2 == 0:
    print("Number " + str(number) + "is even.")
else:
    print("Number " + str(number) + "is odd.")

# Third example
age = 19

# Here are the age limits for bus fare prices
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determines bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Sombody who is {} years old will pay {} to ride the bus."\
    .format(age, ticket_price)
print(message)

# fourth example
points = None

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)

