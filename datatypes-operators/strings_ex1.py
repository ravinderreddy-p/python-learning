amount = 500
split_with = 'Ravi, Dwaip'
paid_by = 'Ravi'
split_amt = amount/len(split_with.split(','))
print(len(split_with.split(',')))
print(split_amt)

for user in split_with.split(','):
    user2 = user.lstrip()
    print(user2)
    user_balance = User(user1=paid_by, user2=user2, balance=split_amt)



# insert/update a record
# Ravi, Dwaip + 250


