'''
write a python program to check whether an element exists within a tuple.
'''
#compete                                            #Python takes all the input as a string input by default.
t=(1,55,98,75,"rignesh")                            #To convert it to any other data type we have to convert the input explicitly.
i=int(input("enter the find elements in tuple:"))   # if we do not write int then it gives not exist output evenif element is present in tuple
#i=input("enter the find elements in tuple:")        # means it considers bydeafult string so if we find string element then it gives exist result if it presents
#i=5                                                #  and not exist if it not present.
if i in t:
    print("exist",i)
else:
    print("not exist",i)


#2) method
'''
t=(1,55,98,75,"Rignesh")
print( 55 in t)   # automatically give output of True if elements present and False if not present.
print( "Rignesh" in t)
print( 5 in t)
'''