import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7,8,9])
print(arr[1:6])
print(arr[1:6:3])

print("\n")
print(arr[::2])
print(arr[:2])

print("\n")
print(arr[2:])
print(arr[2::])
print(arr[2::2])


print("\n")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) 

print("\n")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [12, 12, 13, 14, 15]])
print(arr[0:3, 3])
print(arr[0:2, 3])
print(arr[0:2, 2])
print(arr[0,3])

import array as arr
# creating an integer data type array
x = arr.array('i', [1,2,3,4,5,6,7])

# using the tolist() function to change the array to a list
y = x.tolist()


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])


#list
mylist = ["apple", "banana", "cherry"]


#tuple
thistuple = ("apple", "banana", "cherry")

#set
set1 = {"apple", "banana", "cherry"}
#or we can do 
thisset = set(("apple", "banana", "cherry"))

#dictionnaries
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#converting the previous dictionnary to list
items = list(thisdict.items())
keys = list(thisdict.keys())
values = list(thisdict.values())
#or bydoing
resultList = [(key, value) for key, value in inputDictionary.items()]

#what is noticed that when we need filter, or sort we have to convert to list, but all of them have in common the clear an copy except tuple have only count and index methods.


#to use filter and map etc.. we have built-in functions we can use them.