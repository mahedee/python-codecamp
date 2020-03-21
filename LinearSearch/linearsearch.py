
"""
Muliline comment
This is a linear search algorithm.
Immplement some concept of python
"""

# Define a function with two parameter
def linear_search(theList, findItem):
   
    # intial index of array
    i = 0
   
   # Define a for loop
    for element in theList:
        if element == findItem:
            return i
        i = i + 1
    return -1



#Define a array
items  = [1, 5, 7, 20, 39, 4, 11, 25]

# Set value in a variable
searchItem = 20

# Call a function
index = linear_search(items, searchItem)

# Now print the index
if index != -1:
    print("Index is: " + str(index))
else:
    print("Item not found")
