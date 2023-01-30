'''
write a python script to check if a given key already exists in a dictionary.
'''
d={1:"Rignesh",2:"Mukeshbhai",3:"Patel"}
i=int(input("enter key:"))
if i in d:
    print("key",i, "is present in this dictionary and value is:",d[i])
else:
    print("key is not present in this dictionary")

'''
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
'''