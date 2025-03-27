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







