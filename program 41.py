'''
write a python program to create a dictionary from a string.
note: track the count of the letters from the string.
sample string:'w3resource'
expected output:
    {'3':1,'s':1,'r':2,'u':1,'w':1,'c':1,'e':2,'o':1}
'''

n=input("Enter the string:")
d={}
for i in n:
    if i in d:
        d[i] +=1
    else:
        d[i] =1
print(d)


'''
#from collections import defaultdict, Counter
str1 = 'w3resource'
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
'''

