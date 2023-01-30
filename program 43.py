'''
write a python function to check whether a number is in a given range
'''

def isinrange(n):
    if n not in range(0,100):
        print("Number is not in range of (0,100):",n)
    else:
        print("Number is in range of (0,100):",n)

a=int(input("Enter number:"))
isinrange(a)

'''
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n)
    else :
        print("The number is outside the given range.")
test_range(5)
'''
