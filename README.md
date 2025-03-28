Upper and Lowwer case tring methods
In Python, strings are a sequence of characters, and sometimes you need to manipulate these characters' cases. The two primary methods for changing the case of strings are:

• str.lower(): Converts all characters in the string to lower case.

• str.upper(): Converts all characters in the string to upper case.

▎Methods

▎1. str.lower()

The lower() method returns a new string with all the characters converted to lower case. It does not modify the original string.

▎Syntax

string.lower()


▎Parameters

• None: This method does not take any parameters.

▎Returns

• A new string with all characters converted to lower case.

▎Example

original_string = "Hello World!"
lowercase_string = original_string.lower()
print(lowercase_string)  # Output: "hello world!"


▎2. str.upper()

The upper() method returns a new string with all the characters converted to upper case. Similar to lower(), it does not alter the original string.

▎Syntax

string.upper()


▎Parameters

• None: This method does not take any parameters.

▎Returns

• A new string with all characters converted to upper case.

▎Example

original_string = "Hello World!"
uppercase_string = original_string.upper()
print(uppercase_string)  # Output: "HELLO WORLD!"


▎Use Cases

1. Normalization: When comparing strings, it’s often useful to convert them to the same case to avoid discrepancies due to casing (e.g., "hello" vs "Hello").

   
2. Formatting: When displaying text, you might want to ensure that certain parts of your output are consistently formatted in either upper or lower case.

3. Data Processing: When processing user input or data from external sources, converting strings to a standard case can help in maintaining consistency.

▎Conclusion

The lower() and upper() methods are simple yet powerful tools for string manipulation in Python. By using these methods, you can easily manage the case of your strings for various applications, including data normalization and formatting. Remember that these methods do not change the original string; instead, they return a new one with the desired case transformation.



second commit

▎Python String Method: str.capitalize()

▎Overview

The str.capitalize() method in Python is a built-in string method that returns a copy of the original string with the first character capitalized (converted to uppercase) and all other characters converted to lowercase. This is useful for formatting strings where you want to ensure that only the first letter is uppercase, such as in titles or names.

▎Syntax

str.capitalize()


▎Parameters

The str.capitalize() method does not take any parameters.

▎Return Value

• Returns a new string with the first character capitalized and all other characters in lowercase.

• If the string is empty, it returns an empty string.

▎Usage

The str.capitalize() method can be called on any string object. It does not modify the original string, as strings in Python are immutable. Instead, it returns a new string.

▎Examples

▎Example 1: Basic Usage

original_string = "hello, world!"
capitalized_string = original_string.capitalize()

print(capitalized_string)  # Output: "Hello, world!"

third commit 

The str.swapcase() method in Python is a built-in string method that returns a new string with all the uppercase letters converted to lowercase and all the lowercase letters converted to uppercase. This method is useful for toggling the case of characters in a string.

▎Description

• Method Signature: str.swapcase()

• Return Type: str

• Returns: A new string with the case of each character swapped.

▎Usage

The swapcase() method does not modify the original string; instead, it creates and returns a new string with the case swapped.

▎Syntax

new_string = original_string.swapcase()


▎Parameters

The swapcase() method does not take any parameters.

▎Examples

Here are some examples demonstrating how to use the swapcase() method:

# Example 1: Basic usage
original_string = "Hello, World!"
swapped_string = original_string.swapcase()
print(swapped_string)  # Output: "hELLO, wORLD!"

# Example 2: All uppercase
original_string = "PYTHON PROGRAMMING"
swapped_string = original_string.swapcase()
print(swapped_string)  # Output: "python programming"

# Example 3: All lowercase
original_string = "python programming"
swapped_string = original_string.swapcase()
print(swapped_string)  # Output: "PYTHON PROGRAMMING"

# Example 4: Mixed case
original_string = "PyThOn Is AwEsOmE"
swapped_string = original_string.swapcase()
print(swapped_string)  # Output: "pYtHoN iS aWesOmE"

forth commit 
▎str.strip() Method in Python

▎Overview

The str.strip() method in Python is used to remove leading and trailing whitespace characters from a string. This includes spaces, tabs, newlines, and other whitespace characters. It can also take an optional argument to specify a set of characters to be removed from both ends of the string.

▎Syntax

string.strip([chars])


▎Parameters

• chars (optional): A string specifying the set of characters to be removed. If omitted, the method removes all leading and trailing whitespace.

▎Return Value

The method returns a new string with the specified characters removed from both ends. If no characters are specified, it removes whitespace by default.

▎Examples

▎Basic Usage

text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

fifth commit

▎str.isupper() Method in Python

▎Overview

The str.isupper() method in Python is used to determine if all the characters in a string are uppercase letters. It returns True if all characters in the string are uppercase and there is at least one character; otherwise, it returns False.

▎Syntax

string.isupper()


▎Return Value

• True: If all cased characters in the string are uppercase and there is at least one cased character.

• False: If there are no cased characters or if any cased character is not uppercase.

▎Examples

▎Basic Usage

text = "HELLO"
result = text.isupper()
print(result)  # Output: True


sixth commit

▎str.islower() Method in Python

▎Overview

The str.islower() method in Python is used to check if all the cased characters in a string are lowercase. It returns True if all cased characters in the string are lowercase and there is at least one cased character; otherwise, it returns False.

▎Syntax

string.islower()


▎Return Value

• True: If all cased characters in the string are lowercase and there is at least one cased character.

• False: If there are no cased characters or if any cased character is not lowercase.

▎Examples

▎Basic Usage

text = "hello"
result = text.islower()
print(result)  # Output: True

seventh commit
▎Overview

The str.encode() method in Python is used to encode a string into bytes using a specified encoding scheme. This is particularly useful when you need to convert text data into a byte representation for storage or transmission.

▎Syntax

str.encode(encoding='utf-8', errors='strict')


▎Parameters

• encoding (optional): A string specifying the encoding to use. The default is 'utf-8'. Other common encodings include 'ascii', 'utf-16', and 'latin-1'.

  
• errors (optional): A string that specifies how to handle encoding errors. The default is 'strict', which raises a UnicodeEncodeError on failure. Other options include:

  • 'ignore': Ignore characters that cannot be encoded.

  • 'replace': Replace characters that cannot be encoded with a replacement character (usually ?).

  • 'backslashreplace': Replace characters that cannot be encoded with a backslash escape sequence.

  • 'xmlcharrefreplace': Replace characters that cannot be encoded with the corresponding XML character reference.

▎Return Value

The method returns a bytes object representing the encoded string.

▎Exceptions

• UnicodeEncodeError: Raised if a character cannot be encoded using the specified encoding and the error handling scheme is set to 'strict'.

▎Examples

▎Basic Usage

# Example of basic encoding
text = "Hello, World!"
encoded_text = text.encode()  # Default is 'utf-8'
print(encoded_text)  # Output: b'Hello, World!'

The str.encode() method in Python is used to encode a string into bytes using a specified encoding scheme. This is particularly useful when you need to convert text data into a byte representation for storage or transmission.

▎Syntax

str.encode(encoding='utf-8', errors='strict')


▎Parameters

• encoding (optional): A string specifying the encoding to use. The default is 'utf-8'. Other common encodings include 'ascii', 'utf-16', and 'latin-1'.

  
• errors (optional): A string that specifies how to handle encoding errors. The default is 'strict', which raises a UnicodeEncodeError on failure. Other options include:

  • 'ignore': Ignore characters that cannot be encoded.

  • 'replace': Replace characters that cannot be encoded with a replacement character (usually ?).

  • 'backslashreplace': Replace characters that cannot be encoded with a backslash escape sequence.

  • 'xmlcharrefreplace'


  eighth commit

  ▎README for len()

▎Overview

The len() function in Python is a built-in function used to determine the number of items in an object. It can be used with various data types, including strings, lists, tuples, dictionaries, and sets. The len() function returns an integer representing the count of elements in the given object.

▎Syntax

len(object)


▎Parameters

• object: The object whose length you want to determine. This can be a string, list, tuple, dictionary, set, or any other iterable.

▎Return Value

The function returns an integer representing the number of items in the specified object. If the object is empty, len() will return 0.

▎Exceptions

• TypeError: Raised if the argument passed to len() is not a valid object that supports length measurement (e.g., an integer).

▎Examples

▎Using len() with Strings

# Example of using len() with a string
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13


▎Using len() with Lists

# Example of using len() with a list
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)  # Output: 5


▎Using len() with Tuples

# Example of using len() with a tuple
my_tuple = (1, 2, 3)
length = len(my_tuple)
print(length)  # Output: 3


▎Using len() with Dictionaries

# Example of using len() with a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
length = len(my_dict)
print(length)  # Output: 3 (counts keys)


▎Using len() with Sets

# Example of using len() with a set
my_set = {1, 2, 3, 4}
length = len(my_set)
print(length)  # Output: 4

ninth commit

▎Overview

f-strings, or formatted string literals, are a feature introduced in Python 3.6 that allows for easier and more readable string formatting. They provide a way to embed expressions inside string literals, using curly braces {} to evaluate variables and expressions at runtime.

▎Syntax

To create an f-string, prefix the string literal with the letter f or F. Any expressions that need to be evaluated should be placed inside curly braces {}.

f"string {expression}"


▎Parameters

• expression: Any valid Python expression that you want to include in the string. This can be variables, mathematical operations, function calls, etc.

▎Features

• Readability: f-strings are generally more readable than other string formatting methods.

• Performance: f-strings are faster than both the % operator and the str.format() method.

• Inline Expressions: You can include any valid Python expression inside the curly braces.

▎Examples

▎Basic Usage

name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.


▎Expressions Inside f-Strings

a = 5
b = 10
result = f"The sum of {a} and {b} is {a + b}."
print(result)  # Output: The sum of 5 and 10 is 15.


▎Formatting Numbers

You can format numbers directly within f-strings:

pi = 3.141592653589793
formatted_pi = f"The value of pi is approximately {pi:.2f}."
print(formatted_pi)  # Output: The value of pi is approximately 3.14.


▎Calling Functions

You can also call functions within f-strings:

def greet(name):
    return f"Hello, {name}!"

message = f"{greet('Bob')}"
print(message)  # Output: Hello, Bob!


▎Escaping Braces

If you need to include literal braces in your string, double them:

value = 42
message = f"The set contains {{ {value} }}."
print(message)  # Output: The set contains { 42 }.





tenth commit


▎README: Using str.format() in Python

▎Overview

This README provides an overview of the str.format() method in Python, which is used for formatting strings. This method allows you to create complex string outputs in a clean and readable way.

▎Table of Contents

• Introduction

• Basic Usage

• Positional and Keyword Arguments

• Formatting Numbers

• Padding and Aligning Strings

• Using Format Specifiers

• Nested Fields

• Examples

• Conclusion

▎Introduction

The str.format() method was introduced in Python 2.7 and 3.0 as a way to format strings dynamically. It replaces the older % formatting and offers more powerful and flexible options.

▎Basic Usage

The basic syntax of the str.format() method is:

"string {}".format(value)


▎Example:

name = "Alice"
greeting = "Hello, {}".format(name)
print(greeting)  # Output: Hello, Alice









