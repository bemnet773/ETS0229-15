my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

# Attempting to discard an element that does not exist
my_set.discard(5)  # No error raised
print(my_set)  # Output: {1, 3}
