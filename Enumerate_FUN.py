def my_enumerator(iterable, start=0):
    """A custom enumerator function that mimics the behavior of Python's built-in enumerate.

    Args:
        iterable: An iterable object (like a list, tuple, dictionary or string).
        start: The starting index for enumeration (default is 0).

    Yields:
        A tuple containing the index and the corresponding item from the iterable.
    """
    index = start
    for item in iterable:
        yield (index, item)
        index += 1

# for i, val in my_enumerator(['apple', 'banana', 'cherry'], 1):
#     print(i, val)

sport = ["Circket", "Football", "Hockey", "Tennis"]
print(list(my_enumerator(sport, start=1)))  # <class 'enumerate'>
         

