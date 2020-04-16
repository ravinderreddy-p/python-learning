# Generators are simple way to create iterators using functions.
# for generators, we will use 'yield' keyword instead of 'return'.
# yield allows the function to return values one at a time and
# start where it left off each time it's called.


# define a generator function that produces iterators (stream of numbers)
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1


# my_range() generator, produces a iterator, so we need to loop the iterator.
for n in my_range(4):
    print(n)
