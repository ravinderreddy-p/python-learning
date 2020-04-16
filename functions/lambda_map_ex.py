# map() is a higher-order built-in function that takes a function and iterable as inputs,
# and returns an iterator that applies the function to each element of the iterable.

numbers = [
    [34, 63, 88, 71, 91],
    [1, 45, 432, 46],
    [7, 14, 21, 42, 84]
]


def get_average(num_list):
    return sum(num_list) / len(num_list)


num_avg_list = list(map(get_average, numbers))

print(num_avg_list)


# lambda expression for above get_average()
num_avg_list_lambda = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(num_avg_list_lambda)



