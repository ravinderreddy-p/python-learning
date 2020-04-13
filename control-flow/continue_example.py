# CONTINUE terminates one iteration of a for() or while loop

# example - 1
fruit = ["oranges", "strawberry", "apple"]
foods = ["apple", "apple", "hummus", "toast"]

fruit_count = 0
for food in foods:
    if food not in fruit:
        print("not a fruit")
        continue
    fruit_count += 1
    print("Found a fruit!")

print("total fruit count: ", fruit_count)
