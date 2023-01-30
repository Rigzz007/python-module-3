'''
write a python function to calculate the factorial of a number (a nonnegative integer)
'''
'''
n=int(input("Enter the number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)
'''
def factorial(f):
    fac=1
    for i in range(1,f+1):
        fac=fac*i
    return print(fac)

n=int(input("Enter the number:"))
#print("factorial of the number is:",factorial(n))
factorial(n)

'''
def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
'''