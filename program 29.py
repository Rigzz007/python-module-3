'''
write a python script to concatenate following dictionaries to create a new one.
'''
#complete

d={1:"rignesh"}
d1={2:"patel"}
d.update(d1)
print(d)
#d2=d|d1             #new method for merge two dictionary
#print(d2)

'''
d = {'a': 10, 'b': 8}
d1 = {'d': 6, 'c': 4}
d2 = {**d, **d1}
print(d2)
'''
'''
d1={"Name":"arti" , "Age":23}
d2={"City": "surendranagar", "Gender": "female"}
d3={"Mark":450}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)
'''