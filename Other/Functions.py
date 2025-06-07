from collections import UserDict

class ClassOne:
        name = "Alina"

def printHello():
        print("Hello World")

#x = ClassOne()

printHello()


# COLLECTIONS: List, Tuple, Set, Dictionary
# LIST :
# List (list)
# Mutable: You can change, add, or remove elements after the list is created.
#
# Syntax: Created using square brackets []
#
# Use Case: When you need a dynamic collection of items that may change.
#
# Methods: Has many built-in methods like .append(), .remove(), .pop(), etc.

listOne = ["London,", "New York", "Paris"]
print(listOne[1])

listOne[1] = "Monako"
print(listOne)

for item in listOne:
        print(item)
print(len(listOne))

listOne.append("Rome")
print(listOne)

listOne.insert(1, "Rome")
print(listOne)

listOne.remove("Rome")# Removes 1st found Value!
print(listOne)

listOne.pop()# Removes last Index
print(listOne)

#TUPLES == ArrayList
# Immutable: Once a tuple is created, you cannot change its contents.
#
# Syntax: Created using parentheses () or just commas.
#
# Use Case: When you need a fixed collection of items that should not change (e.g., coordinates, config settings).
#
# Performance: Slightly faster and uses less memory than lists.

tupleOne = ("London", "New York", "Paris")
print(tupleOne)

print(len(tupleOne))
print(tupleOne[1])
print(tupleOne[-1])

for item in tupleOne:
        print(item)

tupleTwo = ((1,2,30), ['a','b','c'], "London", "New York", "Paris")
tupleTwo[1][1] = 'New Jersey'
print(tupleTwo)
#tupleTwo[0][1] = 'New Char' ---> TypeError: 'tuple' object does not support item assignment, Only in List is OK

print(33 in tupleTwo[0])

#SET ---> Can't access by Index order, Unordered, Insertion order not guaranteed

setOne = {"Boston", "Brazil", "Madrid"}
print(setOne)

for item in setOne:
        print(item)

print("Rio-De-Janeiro" in setOne)
setOne.add("Rio-De-Janeiro")
print(setOne)
setOne.remove("Brazil")
print(setOne)
setOne.discard("Rio-De-Janeiro")
print(setOne)
#setOne.remove("Rio-De-Janeiro") If ran 2nd time it will through Error: KeyError: 'Rio de Janeiro'

setOne.pop()
print(setOne)

setTwo = {"Apple", 1.99, "Banana", 'abc'}
print(setTwo)

#Converting List to SET:
listThree = [1, 2, 3]
setThree = set(listThree)
print(setThree)

# MATH Operations available in SET: UNION | INTERSECTION | DIFF | SYMMETRIC DIFF

A = {'A', 'B', 'C', 'D', 'E'}
B = {'C', 'D', 'E', 'F', 'G'}

print(A.union(B)) # Prints unique values in both Sets, discards Duplicates
print(A | B)

print(A.intersection(B))  # Visa versa to UNION
print(A & B)

print(A.difference(B))
print(A - B)
print(B.difference(A))
print(A - B)

print(A.symmetric_difference(B)) # prints All differences across A & B
print(A ^ B)


# DICTIONARY :

dicOne = {
        "Class" : "Super",
        "Fruit" : "Apple",
        "Animal" : "Puppy",
        "Age" : 28
}
print(dicOne)
print(dicOne.keys())
print(dicOne.values())
print(dicOne.items()) # dict_items([('Class', 'Super'), ('Fruit', 'Apple'), ('Anima', 'Puppy'), ('Age', 28)])

for key, value in dicOne.items():
        print("Prints in items() method : ", key, value)


for itemsInDic in dicOne:
        print("Prints in regular way : ", dicOne[itemsInDic]) # Prints only Values 4 separate Lines!


# Usage
#dicOne = CaseInsensitiveDict()
#dicOne['Animal'] = 'Tiger'
#dicOne['animal'] = 'Lion'  # This will overwrite the earlier value




