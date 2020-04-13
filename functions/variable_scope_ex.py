# Variable scope refers to which parts of a program a variable can be referenced
# If variable is created inside a function, it can only be accessed within that function

word = "Goodbye"


# function definitions
def some_function():
    word = "hello!"
    print(word)


def another_function():
    print(word)


# function calls
some_function()  # o/p: hello!
another_function()  # o/p: Goodbye
