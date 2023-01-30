'''
1)how will you set the string value in generating random numbers?
2)how will you randomizes the items of a list in place?
3)write a python program to read a random line from a file.
'''
#1)
'''
import random
import string
def Upper_Lower_string(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length))) # run loop until the define length
    print(" Random string generated in Lowercase: ", result)

    # Print the string in Uppercase
    result1 = ''.join((random.choice(string.ascii_uppercase) for x in range(length))) # run the loop until the define length
    print(" Random string generated in Uppercase: ", result1)

Upper_Lower_string(5) # define the length
'''
import string
import random
def random_number(s):
    result="".join(random.choice(string.digits))
    print("generating random string numbers",result)
random_number("rignesh")
#2)
'''
#The shuffle() method randomizes the items of a list in place.
#Following is the syntax for shuffle() method −
#shuffle (lst,[random])

#****Note − This function is not accessible directly, so we need to import shuffle module
#           and then we need to call this function using random static object.

#Parameters
#lst − This could be a list or tuple.
#random − This is an optional 0 argument function returning float between 0.0 - 1.0. Default is None

#This method changes the original list, it does not return a new list.

import random
l=["Patel","Rignesh","Mukeshbhai",11,8,1997]
random.shuffle(l)
print(l)
'''
#3)
'''
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))

'''