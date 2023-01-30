'''
how do you traverse through a dictionary object in python?
how do you check the presence of a key in a dictionary?
'''

dictionary = {
   "NAME": "RIGNESH MUKESHBHAU PATEL",
   "DOB": "11/8/1997",
   "ZENDER": "MALE",
   "AGE": 25
}
for keys, values in dictionary.items():
   print(keys ,values)





#2)
'''
d={1:"Rignesh",2:"mukeshbhai",3:"patel"}
i=int(input("enter the key:"))
#for i in d:
if i in d:
    print(i,"exist",d[i])
else:
    print("not exist")
'''
