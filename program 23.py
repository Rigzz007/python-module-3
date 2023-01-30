'''
write a python program to find the repeated items of a tuple.
'''
t=(1,5,98,75,5,98,10)
a=list(t)
j=0
count=0
for i in range(len(a)):
    if i==a[i]:
        count=count+1
        print("repeated",i,count)
    j=j+1


'''
var=int(input())
tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
a=list(tup)
for i in range(len(a)):
  a[i]=int(a[i])
count=a.count(var)
print(var,'appears',count,'times in the tuple')
'''
'''
tuple1=(1,2,3,4,1,5,6,1,1,0,9,2,2)
print(tuple1)
count=tuple1.count(1)
print(count)
'''