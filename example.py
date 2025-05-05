import random

msg = "hello"
print(msg)
print("hello world")


# if else statement
if 5 > 2:
    print("5 is greater than 2")

if (6 *2 == 12) and (4 + 4 == 8):
    print("True")
else:
    print("False")

x = str(3)
y = float(3)
z = int(3)
a = 2j
print(x, y, z, type(a))

fruits = ["apple", "banana", "cherry"]
# a,b,c = fruits
# print(x, y, z,)
fruits.append("orange")
fruits.insert(1, "grapes")
fruits.sort()  # sorts the list in ascending order  
# fruits.remove("banana")
print(fruits)

# checks whether "apple" is in the list
# print("apple" in fruits)

# prints the range of 2-5 of the selected fruits in the list
# print(b[2:5])

# print(a.upper())  # prints all of the string in upper case

# print(a.replace("l", "p"))  # replaces the letter l with p in the string

# print(a.split(","))  #  splits the string into substrings ,


age = 45
txt = f"My name is \"John\", and I am {age}"
# print(txt.format(age=age))
print(txt)


# looping through an array
# for x in fruits:
#     print(x)
# for x in range(len(fruits)):
#     print(fruits[x])

# i=0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

newlist = []

for x in fruits:
  if "n" in x:
    newlist.append(x)

print(newlist)

# print(fruits[0])

# randomizes numbers in the range of 1-10
# j = random.randrange(1, 10)
# print(j)   


# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))

x = [200, 300, 400]
print(isinstance(x, list))  # checks if x is an instance of int

thisList = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisList[-1])  # prints the list of fruits

fruits.extend(thisList)
fruits.remove("banana")
fruits.clear()  # removes the first occurrence of banana from the list
print(fruits)  # prints the list of fruits
print(fruits.count("apple"))  # counts the number of times apple is in the list

# sort list in which strating number starts with 50
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# liKist = [1, 2, 3, 4, 5]
# liKist.append(6)  # adds 6 to the end of the list
# myGee = liKist[:]
# print(myGee, liKist)  # prints the list of liKist

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = list1 + list2  # concatenates the two lists
# print(list3)  # prints the list of list3
# for x in list2:
#     list1.append(x)
# print(list1)
# prints the list of list3

thistuple = ("apple", "banana", "cherry")
w = list(thistuple)  # converts the tuple into a list
w[1] = 'orange'
v = tuple(w)  # converts the list into a tuple
print(v)  # prints the tuple of v
