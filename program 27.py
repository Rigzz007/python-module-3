'''
how will you creat a dictionary using tuples in python?
'''
#complete

t=((1,"rignesh"),(2,"ankit"),(3,"arth"))
d=dict(t)
print(d)
'''
t = ((1, "rignesh"), (2, "ankit"), (3, "arth"))
print(t)

d = dict((y, x) for x, y in t)
print(d)
'''