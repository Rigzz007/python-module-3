'''
1)what is tuple? difference between list and tuple.
2)write a python program to create a tuple with different data types.

'''
'''
#1)
->Tuples are used to store multiple items in a single variable.

->Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

->A tuple is a collection which is ordered and unchangeable.

->Tuples are written with round brackets.

->Tuple items are ordered, unchangeable, and allow duplicate values.

->Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

*Ordered
 -> When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

*Unchangeable
 ->Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

*Allow Duplicates
 ->Since tuples are indexed, they can have items with the same value:



#difference of tuple and list.
->The primary difference between tuples and lists is that tuples are immutable as opposed to lists which are mutable.
->Therefore, it is possible to change a list but not a tuple.
->The contents of a tuple cannot change once they have been created in Python due to the immutability of tuples
'''


l=("rignesh","patel",11,8,1997,True,False)
print(l)