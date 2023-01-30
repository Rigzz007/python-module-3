'''
write a python program to convert a tuple to a string.
'''
#complete

#*using str.join()
#->The join() method is a string method and returns a string in which the elements of the sequence have been joined by a str separator.
#->Using join() we add the characters of the tuple and convert it into a string.


t=("rignesh","mukeshbhai","patel")
s=" ".join(t)
print(s)

'''
#*using  str.join() function and map() function
#->The str.join() function works well when we have only string objects as the tuple elements but
#->if the tuple contains at least one non-string object then the str.join() function will fail
#->and show a TypeError as a string object cannot be added to a non-string object.
#->Hence to avoid this TypeError we will make use of map() function inside the join().
#->This map() function will take the iterator of the tuple and str() function as its parameters and convert each element of the tuple into a string.

#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

#Syntax
#map(function, iterables)
#Parameter Values
#->Parameter    Description
#->function    Required. The function to execute for each item
#->iterable    Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

#code to convert a tuple  into a string using str.join() & map() functions

def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st

# Driver code
tuple = ('g', 'e', 'e', 'k', 's', 101)
str = convertTuple(tuple)
print(str)
'''

'''
#*using simple for loop
#->Create an empty string and using a for loop iterate through the elements of the tuple and keep on adding each element to the empty string.
#->In this way, the tuple is converted to a string. It is one of the simplest and the easiest approaches to convert a tuple to a string in Python.
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

tuple = ('g', 'e', 'e', 'k', 's')
str = convertTuple(tuple)
print(str)
'''
