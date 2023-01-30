'''
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
write python program to find the highest 3 values in a dictionary
'''
'''
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
l=list(d.values())
print(l)
l.sort(reverse=True)
l=l[:3]
for i in l:
    for j in d.keys():
        if(d[j]==i):
            print(str(j)+":"+str(d[j]))

'''
'''
from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)

'''
'''
d= {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
c=[]
m=[]
a=sorted(d.values(),reverse=True)
a=a[0:3]
for i in a:
    for k, v in d.items():
        if i==v:
            c.append(k)
for i in c:
    if i not in m:
        m.append(i)
    else:
        del i
print(m)
'''
'''
d = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
z = sorted(d.values())
print(sorted(z[-3:],reverse=True))
'''
'''
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

res = dict()
highest_keys = []
for key,value in my_dict.items():
    d1=sorted(my_dict.values())
    for i in d1[-3:]:
        if i==value:
            res[key] = value
for key,value in res.items():
    highest_keys.append(key)
print(highest_keys)
'''

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
my_list = sorted(my_dict.values())
print(my_list[-3:])
for i in my_list[-3:]:
    print(i)

'''
d = {'a':500, 'b':874, 'c': 560,'d':400, 'e':5874, 'f': 20}
a=list(d.values())
a.sort()
print(a[:-4:-1])
'''
'''
dic = {'a':44,'b':100,'c':37,'d':50,'e':76,'f':65}
a = []

for values in dic.values():
a.append(values)
a.sort()
for k in dic:
if dic[k] in a:
index_new = a.index(dic[k])
a.insert(index_new,k)

print(a[-6::])
'''
'''
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
j=sorted(my_dict.values(),reverse=True)[:3]
k=[]
for i in my_dict:
if my_dict[i] in j:
k.append(i)
print(k)
'''
'''
e={'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
b=[]
for k,v in e.items():
for i in range(0,3):
if v==(sorted(e.values(),reverse=True).pop(i)):
if k not in b:
b.append(k);
else:
continue;
print(b)

'''
'''
my= {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
j=sorted(my.values(),reverse=True)[:3]
l=[i for i in my if my[i] in j]
print(l)
'''
'''
D = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
V=[]
B=[]
for i in D.values():
V.append(i)
V.sort()
for j in V[-3:]:
B.append(j)
z=[x for x,y in D.items() if y in B]
print(z)
'''
'''
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
n=sorted(list(my_dict.values()))[3:]
l=[i for i in my_dict.keys() if my_dict[i] in n][::-1]
print(l)
'''
'''
price={'apple':1.55,'orange':0.54,'milk':3.50,'hotdog':8.70,'beer':4.00,'meat':12.30}
values=list(price.values())
values.sort()
last3=values[-3:]
for i in price:
if price[i] in last3:
print(i, price[i])
'''
'''
dic = {'a':23,'b':32,'c':37,'d':50,'e':76,'f':65}
a = []

for values in dic.values():
a.append(values)
a.sort()
print(a[:-4:-1])
'''
'''
d1 = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
list1=list(sorted(d1.values(),reverse=True))
print (list1[:3])
'''
'''
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
list1 = [value for value in my_dict.values()]
list1.sort()
print list1[-3:]
'''
'''
'''


