'''
write a python program to replace last value of tuples in a list.
'''

l=[(1,25,59,98),(92,46,76,3)]
print([t[:-1]+("python",) for t in l])
'''
l = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + ("python",) for t in l])
'''