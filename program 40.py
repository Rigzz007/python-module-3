'''
write a python program to combine values in python list of dictionaries.
sample data:[{'item':'item1','amount':400},{'item':'item2','amount':300}, {'item':'item1','amount':750}]
expected output:counter ({'item1':1150,'item2':300})
'''
'''
Things to google:

python list comprehension
python dict comprehension
python star
python dict get
python set union
'''
'''
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)

'''
#Using loop
#This task can be performed using brute force way.
#In this we iterate for all the dictionaries and perform the concatenation of like keys by adding one list element to other on the key match.
test_list = [{'A': [1, 5, 6, 7], 'B': [9, 6, 2, 10],'C': [4, 5, 6]},{'A': [5, 6, 7, 8], 'C': [5, 7, 10]},{'A': [7, 5], 'D': [5, 7]}]

# printing original list
print("The original list is : " + str(test_list))

# Concatenate Similar Key values
# Using loop
res = dict()
for dict in test_list:
    #print(dict)
    for list in dict:
        #print(list)
        if list in res:
            res[list] =res[list] + dict[list]
        else:
            res[list] = dict[list]
# printing result
print("The concatenated dictionary : " + str(res))

'''
#I have a list of dictionaries in the following format
foo = [{'a': 'x', 'b': 'y', 'c': 'z'},{'a': 'j', 'c': 'z'}]
#I want to group this list of dictionaries into a single dictionary, like:

bar = {'a': ['x', 'j'],'b': ['y', None],'c': ['z', 'z']}
#What I've currently done is, looping through all the dicts in foo and create a list of keys and then looping again over the same to create bar.
#I wonder whether there is a simpler way to accomplish this. Can anyone help?
#**answer
bar = {
    k: [d.get(k) for d in foo]
    for k in set().union(*foo)
}
'''
#I am just going to complement Alex Hall solution here, so that it does not return a lot of "None" values:
'''
def merge_dictionary_list(dict_list):
  return {
    k: [d.get(k) for d in dict_list if k in d] # explanation A
    for k in set().union(*dict_list) # explanation B
  }
'''
#Explanation:
'''
The whole thing inside {} is a dictionary comprehension
Explanation A: Go through all elements in dictionary list and get values for current key k if the current dictionary (d) being evaluated actually has that key.
OBS: Without the if k in d expression there could be a bunch of None values appended to the arrays in case the list of dictionaries contains different types of keys.

Explanation B: gets all keys from list of dictionary and unite them distinctly by using set().union. After all we can only have distinct elements in set data structure.
If you want to do it the traditional way, just go with:
'''
'''
def merge_list_of_dictionaries(dict_list):
  new_dict = {}
  for d in dict_list:
    for d_key in d:
      if d_key not in new_dict:
        new_dict[d_key] = []
      new_dict[d_key].append(d[d_key])
  return new_dict
'''
#I think the first solution looks more elegant, but the second one is more legible/readable.

#2)Use a dict comprehension to create the desired result:
'''
>>> bar = {key: [d.get(key) for d in foo] for key in all_keys}
>>> bar
{'a': ['x', 'j'], 'b': ['y', None], 'c': ['z', 'z']}
'''