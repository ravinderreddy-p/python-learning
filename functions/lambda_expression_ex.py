# Lambda expression used to create an anonymous functions.
# They are not needed later in the code.
# lambda <args>: <evaluate expression & return>
# ex: lambda x: x*2 (double the given number)


def double_fun(x):
    return x * 2


# equivalent lambda expression for above function
double = lambda x: x * 2  # lambda keyword used to indicate lambda expression.

# lambda expression call
double(3)
print(double(3))


# example - 2:
def multiply(x, y):
    return x * y


# above function can be reduced by lambda expression
multiply = lambda x, y: x * y


# lambda expression call
multiply(4, 5)


# example - 3: lambda with Map
# map() is a higher-order built-in function that takes a function and iterable as inputs,
# and returns an iterator that applies the function to each element of the iterable
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]
averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)


# example - 4: lambda with Filter
# filter() is a higher-order built-in function that takes a function and iterable as inputs and
# returns an iterator with the elements from the iterable for which the function returns True.
cities = ["New York", "LA", "Chicago", "MV", "Denver", "Boston"]
short_cities = list(filter(lambda x: len(x) < 3, cities))
print(short_cities)
