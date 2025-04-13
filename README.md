#First Commit
1. append():

   • This method adds an element to the end of the list.

   • Syntax: list.append(element)

   • Example:
          my_list = [1, 2, 3]
     my_list.append(4)
     print(my_list)  # Output: [1, 2, 3, 4]
     

2. remove():

   • This method removes the first occurrence of a specified value from the list.

   • Syntax: list.remove(value)

   • Example:
          my_list = [1, 2, 3, 2]
     my_list.remove(2)
     print(my_list)  # Output: [1, 3, 2]
     

3. sort():

   • This method sorts the elements of the list in ascending order by default. You can also sort in descending order by passing the reverse=True argument.

   • Syntax: list.sort(reverse=False)

   • Example:
          my_list = [3, 1, 4, 2]
     my_list.sort()
     print(my_list)  # Output: [1, 2, 3, 4]
# Second commit

1. list.index(element, start=0, end=None)

•  Explanation: The index() method returns the index (position) of the first occurrence of a specified element in the list. You can optionally specify a start and end index to limit the search to a specific portion of the list. If the element is not found, it raises a ValueError.

•  Purpose: To efficiently locate the position of a specific item in a list, with the option to restrict the search to a subset of the list.

•  How it Works:

  1. The method searches the list (or the specified slice of the list) from left to right for the element.
  2. If the element is found, the index of its first occurrence is returned.
  3. If the element is not found within the specified range (or the entire list), a ValueError is raised.

•  Arguments:

  •  element: The element to search for.
  •  start (optional): The index to start the search from (default is 0).
  •  end (optional): The index to end the search at (default is the end of the list). Note that the search will not include the element at the end index.

•  Example (Python):

    my_list = ["apple", "banana", "cherry", "apple"]
    index1 = my_list.index("banana")  # index1 will be 1

    index2 = my_list.index("apple", 1) # index2 will be 3 (starts search at index 1)

    try:
        index3 = my_list.index("grape") # Raises ValueError
    except ValueError:
        print("Element not found")

    try:
       index4 = my_list.index("apple", 1, 3) #Raises ValueError
    except ValueError:
      print("Element apple not found between index 1 and 3")

2. list.count(element)

•  Explanation: The count() method returns the number of times a specified element appears in the list.

•  Purpose: To determine how many times a particular value occurs in a list.

•  How it Works:

  1. The method iterates through the list.
  2. For each element in the list, it checks if it's equal to the element being searched for.
  3. It increments a counter for each match.
  4. The final count is returned.

•  Example (Python):

```

▌Important Considerations

•  The method returns the index of the first occurrence only.
•  A ValueError is raised if the element is not found.
•  The start and end arguments allow you to restrict the search to a specific portion of the list. Note that the end index isn't inclusive in search.

```

    my_list = [1, 2, 2, 3, 2, 4]
    count = my_list.count(2)  # count will be 3

    my_list = ["apple", "banana", "apple", "apple"]
    count2 = my_list.count("apple") # count2 will be 3

    count3 = my_list.count("grape") # count3 will be 0

3. list.clear()

•  Explanation: The clear() method removes all elements from a list, effectively making it an empty list. It modifies the original list directly. While we covered this before, it's a fundamental method and worth reiterating for completeness.

•  Purpose: To efficiently empty a list, removing all of its contents.

•  How it Works:

  1. The method iterates through the list.
  2. It removes each element from the list.
  3. The list becomes an empty list: [].
  4. The list is modified in-place.

•  Example (Python):

    my_list = [1, 2, 3]
    my_list.clear()  # my_list will be []