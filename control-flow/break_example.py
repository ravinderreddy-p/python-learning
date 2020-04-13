# BREAK terminates a for() or while loop.
# a loop will terminate if it encounters a break statement.

# example - 1
manifest = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42),
            ("machine", 120), ("cheese", 5)]
weight = 0
items = []

for cargo in manifest:  # for cargo_name, cargo_weight in manifest
    if weight >= 100:
        print("breaking loop now!")
        break
    else:
        print(" adding {} ({})".format(cargo[0], cargo[1]))  # cargo_name, cargo_weight
        items.append(cargo[0])
        weight += cargo[1]

print(weight)
print(items)
