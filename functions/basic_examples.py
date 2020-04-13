# example : function definition without argument & return statement
def print_greetings():
    print("Hello world!")


# example : function definition with arguments & return
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


# function call
cylinder_volume(10, 3)


# example : function definition with default arguments
# radius is set to 5, if this parameter is omitted in a function call.
def cylinder_vol(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2


# function call of cylinder_vol(arg1, arg2(optional))
cylinder_vol(10)  # cylinder_vol(10,5)

# function call - pass arguments by position
cylinder_vol(10, 7)  # radius = 7 will overwrite default value 5.

# function call - pass arguments by argument names
cylinder_vol(height=10, radius=7)
