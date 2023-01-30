'''
write a python program to check multiple keys exists in a dictionary.
'''
d={"NAME":"RIGNESH PATEL","AGE":25,"ZENDER":"MALE","DOB":"11/8/1997"}
print(d.keys() >={"NAME","DOB"})
print(d.keys() >={"AGE","ZENDER"})



'''
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})
'''
'''
#Using if and all statement
#: In this method we will check that if all the key elements that we want to compare are present in our dictionary or not .

# initializing a dictionary
sports = {"geeksforgeeks" : 1, "practice" : 2, "contribute" :3}

# using if, all statement
if all(key in sports for key in ('geeksforgeeks', 'practice')):
    print("keys are present")
else:
    print("keys are not present")

# using if, all statement
if all(key in sports for key in ('geeksforgeeks', 'ide')):
    print("keys are present")
else:
    print("keys are not present")
Output:
keys are present
keys are not present
'''
'''
getsizeof():

Getsizeof() method from Python's sys library will tell you the size of a Python object in the memory.

import sys
x="Australia"
y=sys.getsizeof(x)
print(y)
Output:

58
The result is in bytes.

Getsizeof() will give the size of any Python object whatsoever. Range object, byte object, reversed object, list object, dictionary object, list goes on.

Let's create a huge list and see its size in bytes:

import sys
x=range(111010)
y=sys.getsizeof(list(x))
print(y)
Output:

999200

'''