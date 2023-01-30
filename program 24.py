'''
write a python program to remove an empty tuple(s) from a list of tuples.
'''
'''
#complete

t=[(1,25),(),(54,65)]
t.remove(())
print(t)
#for i in t:
#    if i==()
'''
l=[(1,25),(),(5,95)]
for i in l:
    if i==():
        l.remove(i)
print(l)
'''
def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples


tuples = [(), ('aarti','12','6'), (), ('laxmi', 'sita'),
          ('krishna', 'vandana', '45'), ('',''),()]
print(Remove(tuples))
'''