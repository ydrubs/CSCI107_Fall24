"""0.2 Dictionaries"""

from random import randint

"""
Remember that a dictionary is not ordered. 
That means we CANNOT access dictionary entries by its positon value (or index) unless we convert the dictionary to a 
list or another structure that is ordered.


Create an empty dictionary and create a key/value pair
"""


"""Create multiple key/value pairs"""
    #Use i+1 because we already have one entry in the dictionary



"""Print the keys and values of the dictionary"""
# Keys

# Values


"""Print key/value pairs as tuples"""


"""
Print out the value of a dictionary by giving a key
Returns an error if the value does not exit
"""
# KeyError



"""Return the value of the key in the argument or None if it does not exist
This is prefered if you are not sure whether a value exists"""




"""Remove and return the value at the key index specified
Similar to a list, except we NEED to specify a key(again since a dictionary is not ordered)"""

# another_entry = rand_dict.pop(11) # Key error
# print(another_entry)


#Replace what was removed


"""
Sometimes we want both the key AND value at an index.

For this to work, we need to turn or dictionary to a list. 

Then we can remove and return the key/value pair at the index specified.
"""

# We first use 'list' to turn all the entries into a list of tuples, then take the last tuple with the -1 argument



#Replace it


"""
Practice:
Given the rand_digits dictionary you made previously,

1) Ask the user for a lower bound integer and upper bound integer.

2) Check to make sure the lower and upper bounds are within the range of the dictionary entries. If they are proceed to 
step 3, if either is not, give an appropriate message and ask again.

    Assume the smallest valid lower bound should be 0 and the highest would be the number of entries minus 1
    
3) Return all key/value pairs from the rand_dict dictionary between that range
"""











