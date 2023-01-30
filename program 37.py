'''
1)write a python program to print all unique values in a dictionary.
2)why do you use the zip() method in python?
'''
'''
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)
'''
l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",l)
#d=set(val for i in l for val in i.values())
d=[z for z in l for z in z.items()]
#[z for z in d for z in z.items()]
print(dict(d))


'''
l= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
dic = []
for i in l:
    for j in i.values():
        if j not in dic:
            dic.append(j)
print(set(dic))
'''
'''
d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
a=[]
for i in d:
    for j in i.values():
        a.append(j)
print(set(a))

'''
'''
# print unic key
d= [{"V":"9S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
d1 = [z for z in d for z in z.items()]
print(dict(d1))

'''
'''

s= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
a = set()
for i in s:
    for j in i.values():
        #a.append(j)          #'set' object has no attribute 'append'
        a.add(j)
print(a)

'''
'''
data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
c=[]
for key in data:
    for i in key:
        if key[i] in c:
            pass
        else:
            c.append(key[i])
print(c)
'''
'''
sample = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
temp_list = []
for item in sample:
    for value in item.values():
        temp_list.append(value)
print(set(temp_list))

'''
'''
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

def findo(arg):
    listo = []
    for dic in arg:
        listo += dic.values()
    return set(listo)
print(findo(L))

'''
'''
d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
l1=[]
for i in d1:
    for x,y in i.items():
        if y not in l1:
            l1.append(y)
s = set(l1)
print(s)

'''
'''
l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
a=set(val for i in l for val in i.values())
print(a)

'''