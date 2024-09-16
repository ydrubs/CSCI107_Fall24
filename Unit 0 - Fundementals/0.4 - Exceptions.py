##Get two integer values from the user - Suppose they enter something else though
# a = int(input("Please enter the first number: "))
# b = int(input("Please enter the second number: "))
##Try entering a character when the code is run



##Using a try/except block to correct for any non-integer data without explicitly writing code for it
# while True:
#     pass
#         a = int(input("Please enter the first number: "))
#         b = int(input("Please enter the second number: "))
#         pass
#     pass
#         pass


##Preventing a division by zero error



##You can catch both errors by specifying which to correct
# while True:
#     pass

#         a = int(input("Please enter the first number: "))
#         b = int(input("Please enter the second number: "))
#         c = a/b
#         break
#     pass
#         print("bad data, can only accept an integer")
#     pass
#         print("You divided by zero")
#     #If an error does not match the above two you can run a general exception
#     pass
#         print("No Math Today!")
# print(c)

##Tryng to change a tuple
# my_card = ('Ace', 'Spades')
# my_card[0] = 'Ace'

##You can raise your own errors with descriptions as well
# pass
#     my_card[0] = 'Ace'
# pass
#     pass

##Errors can also be raised without needing a try/except
# feedback = input("How Awesome is your programming teacher? ")
# pass
#     pass
# print('Thank you for your valuable feedback')

##Exercise 1.1 - Banking Exceptions
##  1) Ask the user for an amount they want to deposit into a bank account
##  2) If the amount is not an integer (a float or string), write a (named) exception
##  3) If the amount is a negative integer raise an ArithmeticError with a message of your choice
##  4) If the amount is accepted, call a function named accepted_deposit that prints the amount deposited



