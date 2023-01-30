'''
write a python program to remove duplicate from a list.
'''
#complete
'''
l=[1,5,4,79,53,5,4,6]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
        print(l1)
'''
'''
l=[2,3,4,2,5,6,4,7,9,5,6]
print(set(l))
'''

#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary,
#all with different qualities and usage.



#* Note: Set items are unchangeable, but you can remove items and add new items.Sets are used to store multiple items in a single variable.

#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary,
#all with different qualities and usage.

#A set is a collection which is unordered, unchangeable*, and unindexed.

#Sets are written with curly brackets.

#Note: Sets are unordered, so you cannot be sure in which order the items will appear.

#NOTE:-Set Items
#Set items are unordered, unchangeable, and do not allow duplicate values.

# NOTE:-Unordered
#Unordered means that the items in a set do not have a defined order.

#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# NOTE:-Unchangeable
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

#Once a set is created, you cannot change its items, but you can remove items and add new items.

# NOTE:-Duplicates Not Allowed
#Sets cannot have two items with the same value.

#Example
# NOTE:-Duplicate values will be ignored:
'''
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
'''
'''
n=int(input("Enter the  total no of element you want inside your list:"))
l=[]
for i in range (n):
      ele=input("Enter the element")
      l.append(ele)
print("my list",l)
duplicate=(set(l))
print(duplicate)
'''