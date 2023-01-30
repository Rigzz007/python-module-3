'''
1)write a python function that checks whether a passed string is palindrome or not
2)how many basic type of functions are available in python?
'''

#palindrom means a string we can read or write same from both side like level,radar

n=input("enter string:")
d=[]
j=1
for i in n:
    d.append(i)
print(d)
if d[::1]==d[::-1]:
    print("string is palindrom")
else:
    print("string is not palindrom")


'''
n=input("enter string:")
if n==n[::-1]:
    print("palindrom")
else:
    print("not")
'''
'''
*****There are three types of functions in Python:

#->Built-in functions, such as help() to ask for help, min() to get the minimum value, print() to print an object to the terminal;and
#->User-Defined Functions (UDFs), which are functions that users create to help them out; And
#->Anonymous functions, which are also called lambda functions because they are not declared with the standard def keyword.
'''