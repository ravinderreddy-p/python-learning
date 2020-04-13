# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit

manifest = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42),
            ("machine", 120), ("cheese", 5)]

weight = 0
items = []

for cargo_item, cargo_weight in manifest:
    if weight >= 100:
        break
    elif weight + cargo_weight > 100:
        continue
    else:
        weight += cargo_weight
        items.append(cargo_item)

print(items, weight)
