'''
write a python program to get a unique values from a list.
'''
#complete

l1=[1,2,3,2,5,4,6,"python",5,4,6,9]
print(set(l1))


'''
#l1.sort()   sort is not working because list contain mix of data sort
#print(l1)
l2=['a','x','d','s','b']
l2.sort()    #sort work only on same data type
print(l2)
'''
'''
#error because of mix of data
l3=[1,2,58,65,'a','sde']
l3.sort()
print(l3)
'''