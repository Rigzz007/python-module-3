'''
1)write a python function to get the largest number,smallest num and sum of all from a list.
2)how will you compare two list?
'''
#1)

l=[1,5,48,2,6,50,14,28,35,21,19,14]
print("largest number of the list is:",max(l))
print("largest number of the list is:",min(l))
print("largest number of the list is:",sum(l))



#2)
'''
#using equal operator we compare two list but both list have same values in same order
l=[1,2,3,4]
l1=[1,2,3,4]
if l==l1:
    print(True)
else:
    print(False)
'''

'''
#The list.sort() method sorts the two lists and the == operator compares the two lists item by item
#which means they have equal data items at equal positions.
#This checks if the list contains equal data item values but it does not take into account the order of elements in the list.
#This means that the list [1,2,3,4] will be equal to the list [2,3,1,4] according to this method of comparison.

l=[1,2,3,4]
l1=[2,3,1,4]
l.sort()
l1.sort()
if l==l1:
    print(True)
else:
    print(False)
'''
'''
#Using collections.Counter()
#This method tests for the equality of the lists by comparing frequency of each element in first list with the second list.
#This method also does not take into account the order of the elements of the list.

import collections
def compareList(l1,l2):
   if(collections.Counter(l1)==collections.Counter(l2)):
      return "Equal"
   else:
      return "Non equal"
l1=[1,2,3]
l2=[2,1,3]
print("First comparison",compareList(l1,l2))
l3=[1,2,3]
l4=[1,2,4]
print("Second comparison",compareList(l3,l4))
'''
'''
#Using sum() ,zip() and len()
#This method first compares each element of the two lists and store those as summation of 1,
#which is then compared with the length of the other list.
#For this method, we have to first check if the lengths of both the lists are equal before performing this computation.
#This method also checks for the order of the elements. This means that the list [1,2,3] is not equal to the list [2,1,3].

def compareList(l1,l2):
   if(len(l1)==len(l2) and len(l1)==sum([1 for i,j in zip(l1,l2) if i==j])):
      return "Equal"
   else:
      return "Non equal"
l1=[1,2,3]
l2=[2,1,3]
print("First comparison",compareList(l1,l2))
l3=[1,2,3]
l4=[1,2,3]
print("Second comparison",compareList(l3,l4))
'''