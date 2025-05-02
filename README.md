
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


▎2. items()

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


▎3. keys()

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

