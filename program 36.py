'''
write a python program to combine two dictionary adding values for common keys.
d1={'a':100,'b':200,'c':300} o d2={'a':300,'b':200,'d':400}
sample output:counter ({'a':400,'b':400,'d':=400,'c':300})
'''

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
for i in d1:
    if i in d2:
        d2[i]=d2[i]+d1[i]
    else:
        d2[i]=d1[i]
print(d2)
'''

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
'''