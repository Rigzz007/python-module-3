'''
write a python function that takes a list and return a new list with unique element of the first list.
'''
#complete
def uniquelist(l1,l2):
    for i in a:
        if i not in b:
            b.append(i)
            b.sort()
    print(b)

a=[1,5,4,8,9,6,1,5,7,3,2,5,4,8,9,2]
b=[]
print(uniquelist(a,b))