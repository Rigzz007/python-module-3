'''
write a python program to check whether a list contains a sub list
'''
#complete

l=[1,2,3,4,5,["a","b","c","d"],6,7,8]
l2=["a","b","c","d"]
for i in l:
    if i==l2:
        print("true")
        break
else:
    print("false")

#using length
'''
l1=['a','b','c',[4,5,6,"python"]]
for i in l1:
    if len(i)>1:
        print("sublist in list")
        break
else:
    print("sublist is not in list")
'''