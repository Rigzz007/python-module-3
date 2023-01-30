'''
write a python function to check whether a number is perfect or not.
perfect number means sum of numbers divider is equal to number means 6 can be divide by 1,2,3 and sum of all three divider is 6 so 6 is perfect number.
'''
'''
n=int(input("enter number:"))
d=[1]
for i in range(2,n):
    if (n % i)==0:
        d.append(i)
sum=sum(d)
if (sum==n):
    print("number is perfect number:")
else:
    print("number is not perfect number:")
'''

n=int(input("Enter number:"))
sum=0
for i in range(1,n):
    if (n%i)==0:
        sum=sum+i
if sum==n:
    print("perfect")
else:
    print("not perfect")




