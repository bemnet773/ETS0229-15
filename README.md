
# second commit
1. get()

The get() method retrieves the value associated with a specified key. If the key does not exist, it returns None or a specified default value.

Syntax:
value = dictionary.get(key, default_value)


Example:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using get() to retrieve values
name = my_dict.get('name')  # Key exists
age = my_dict.get('age')    # Key exists
country = my_dict.get('country', 'Not Found')  # Key does not exist with a default value

print("Name:", name)          # Output: Name: Alice
print("Age:", age)            # Output: Age: 30
print("Country:", country)    # Output: Country: Not Found


2. items()

The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs. This is useful for iterating over both keys and values.

Syntax:
items_view = dictionary.items()


Example:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using items() to get key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 30
# city: New York


3. keys()

The keys() method returns a view object that displays a list of all the keys in the dictionary. This can be useful when you only need to work with the keys.

Syntax:
keys_view = dictionary.keys()


Example:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using keys() to get all keys
for key in my_dict.keys():
    print(key)

# Output:
# name
# age
# city

# thired commit

1. pop(key)

The pop() method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError unless a default value is provided.

Example:
# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using pop() to remove 'b'
value = my_dict.pop('b')
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

# Using pop() with a default value
value = my_dict.pop('d', 'Not Found')
print(value)  # Output: Not Found


2. popitem()

The popitem() method removes and returns the last inserted key-value pair as a tuple. If the dictionary is empty, it raises a KeyError.

Example:
# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using popitem() to remove the last item
item = my_dict.popitem()
print(item)  # Output: ('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2}


3. update(other)

The update() method updates the dictionary with elements from another dictionary or from an iterable of key-value pairs. If a key already exists, its value is updated; if it doesn’t exist, it is added.

Example:
# Creating two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using update() to merge dict2 into dict1
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}


4. values()

The values() method returns a view object that displays a list of all the values in the dictionary.

Example:
# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using values() to get all values
values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])

# Converting to a list
values_list = list(values)
print(values_list)  # Output: [1, 2, 3]
5. 