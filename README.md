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

