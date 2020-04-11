scores = ["B", "C", "A", "D", "B", "A"]
grades = scores
print("scores: " + str(scores))
print("grades :" + str(grades))

scores[3] = "B"
print("scores: " + str(scores))  # updated 3rd index with 'B'
print("grades :" + str(grades))  # updated 3rd index with 'B'

# len() method returns how many elements in the list
print(len(scores))

# max() method returns the max value in the list.
batch_sizes = [15, 6, 89, 34, 65, 35]
print(max(batch_sizes))
print((min(batch_sizes)))

python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python',
                    'Reticulated Python', 'Angolan Python']
print(max(python_varieties))  # Prints largest letter alphabetically
print(min(python_varieties))  # Prints smallest letter alphabetically

mix_match = [1, 2, 'str']
# print(max(mix_match))  # TypeError: '>' not supported between instances of 'str' and 'int'

# sorted() method returns a copy of a list in order from smallest to largest
# leaving the original list unchanged.

print(sorted(batch_sizes))  # prints the list items in ascending order.

print(sorted(batch_sizes, reverse=True))  # prints the list items in descending order.

# join() - takes a list as an argument and returns a string consisting of the
# list elements joined by separator string.
print("join()  method:")
nautical_directions = "\n".join(["force", "aft", "starboard", "port"])
print(nautical_directions)

names = ["Gercia", "O'Kelly", "Davis"]
print("-".join(names))

# append() - adds an element to the end of the lists.
print("append() method: ")
python_varieties.append("Blood Python")
print(python_varieties)



