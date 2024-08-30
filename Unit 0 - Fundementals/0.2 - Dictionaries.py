"""0.2 Dictionaries"""

from random import randint

"""
Remember that a dictionary is not ordered. 
That means we CANNOT access dictionary entries by its positon value (or index) unless we convert the dictionary to a 
list or another structure that is ordered.


Create an empty dictionary and create a key/value pair
"""
# rand_dict = {'a': 1, 'b' : 2} #Key/value pairs
# rand_dict['c'] = 3
#
# print(rand_dict)

my_numbers = {}
my_numbers[0] = randint(0,20)

# print(my_numbers)


"""Create multiple key/value pairs"""
for i in range(10):    #Use i+1 because we already have one entry in the dictionary
    my_numbers[i+1] = randint(0,20)

# print(my_numbers)


"""Print the keys and values of the dictionary"""
# Keys
# print(my_numbers.keys())

# Values
# print(my_numbers.values())

"""Print key/value pairs as tuples"""
# a = (1,2,3,4)
# print(a[0])
# a[0] = 5
# print(my_numbers.items())

"""
Print out the value of a dictionary by giving a key
Returns an error if the value does not exit
"""
# print(my_numbers[10])
# print(my_numbers[11])# KeyError



"""Return the value of the key in the argument or None if it does not exist
This is prefered if you are not sure whether a value exists"""
# print(my_numbers.get(10))
# print(my_numbers.get(11))



"""Remove and return the value at the key index specified
Similar to a list, except we NEED to specify a key(again since a dictionary is not ordered)"""

# another_entry = my_numbers.pop(11) # Key error
# print(another_entry)
my_key = 8
entry = my_numbers.pop(my_key)
# print(my_key, entry)
print(my_numbers)

#Replace what was removed
my_numbers[my_key] = entry
print(my_numbers)


"""
Sometimes we want both the key AND value at an index.

For this to work, we need to turn or dictionary to a list. 

Then we can remove and return the key/value pair at the index specified.
"""

# We first use 'list' to turn all the entries into a list of tuples, then take the last tuple with the -1 argument
index_entry = list(my_numbers.items()).pop(1)

a_list = sorted((list(my_numbers.values())))
print(a_list)

print(index_entry)


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
rand_dict = {}

