# write a  generator function - chunker, that takes iterable and yields
# a chunk of a specified size at a time. (to deal with large files)


def chunker(iterable, size):
    chunk = []
    k = 0
    for i in range(len(iterable)):
        chunk.append(i)
        k += 1
        if k == size:
            yield chunk
            chunk.clear()
            k = 0
    if len(chunk) != 0:
        yield chunk


for chunk in chunker(range(25), 5):
    print(list(chunk))


# above logic can be written as below:
def chunker(iterable, size):
    """yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i: i+size]


for chunk in chunker(range(25), 4):
    print(list(chunk))
