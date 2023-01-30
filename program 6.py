'''
write a python function that takes two lists and return true if they have at least one common member.
'''
#complete

def list(l,l1,l2):
    for i in l:
        if i in l1:
            l2.append(i)
            print(l2)

    else:

        return False


a=[1,5,58,96,45,26,35]
b=[96,35,6,4,97,27,32]
c=[]
list(a,b,c)
