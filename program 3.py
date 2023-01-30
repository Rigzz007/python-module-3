'''
write a python program to count the number of string where the string length is 2 or more
and the first and last character are same from a given list of strings.
'''
#complete

s=0
l=['patelp','rignesh','mukeshbhaim','joitabhai',"rar"]
l1=len(l)
print("Number of string in list are:",l1)
for i in l:
    if len(i)>=2 and i[0]==i[-1]:
        print("the given words are:",i)
        s=s+1
print("no of words are:",s)
