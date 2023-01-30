'''
write a python program to split a list into different variables.
'''
#complete

l=[1,2,45,86,"acx","axe"]
l1=[]
l2=[]
for i in l:
    if type(i)==int:
        l1.append(i)
    elif type(i)==str:
        l2.append(i)
    else:
        print("unrecognise")
print("LIST OF MIX DATA TYPE:",l)
print("LIST OF INT DATA TYPE:",l1)
print("LIST OF STRING DATA TYPE:",l2)

#using variable
#if list contain same group of data then we can devide list in same variables of the list like exemple we have a 3 group of data set thus
# we devide list into 3 variable.
'''
l = [("Patel", "@#$%^", 1,25,96), ("Rignesh", "#&*", 86),
         ("Mukeshbhai",58,"!")]
l1, l2, l3 = l
print("LIST OF MIX VARIABLE:",l)
print("LIST OF L1 VARIABLE:",l1)
print("LIST OF L2 VARIABLE:",l2)
print("LIST OF L3 VARIABLE:",l3)
'''