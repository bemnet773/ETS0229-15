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
     