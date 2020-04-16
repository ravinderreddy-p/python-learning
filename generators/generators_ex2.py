# write a generator function that works like built-in function enumerate()

languages = ["python", "java", "javascript", "ruby", "html"]


def my_enumerate(iterable, start=1):
    # implement generator function here
    i = 0
    while i < len(iterable):
        yield start, iterable[start - 1]
        i += 1
        start += 1


for i, language in my_enumerate(languages, 1):
    print("lesson {}: {}".format(i, language))

