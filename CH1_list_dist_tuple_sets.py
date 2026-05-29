# =====================================================
# LIST IN PYTHON
# =====================================================
# -> List is mutable (can change)
# -> Ordered collection
# -> Allows duplicate values
# -> Different datatypes allowed

# intro = ["Ajay", "Pratap", 20, "Male", True, False, 77.7]

# print(intro)
# -> Prints complete list

# print(len(intro))
# -> len() gives total number of elements

# print(intro[2])
# -> Access element using index
# -> Index starts from 0

# intro[2] = 24
# -> Lists are mutable, so value can change

# print(intro[2])

# print(intro)

# print(intro[-3:-1])
# -> Negative slicing
# -> end index excluded


# =====================================================
# LIST METHODS
# =====================================================

# marks = [90, 80, 70, 60, 50]

# print(marks)

# marks.append(40)
# -> Adds element at END

# print(marks)

# marks.insert(1, 85)
# -> insert(index, value)

# print(marks)

# marks.remove(70)
# -> Removes first matching value

# print(marks)

# print(marks.count(90))
# -> Counts occurrences

# print(marks.index(60))
# -> Gives index of value

# print(marks.pop(4))
# -> Removes element using index
# -> pop() also RETURNS removed value

# Easy Revision:
#
# append() -> add at end
# insert() -> add at position
# remove() -> remove by value
# pop()    -> remove by index
# count()  -> count value
# index()  -> find position


# =====================================================
# TUPLES IN PYTHON
# =====================================================
# -> Immutable (cannot change)
# -> Ordered collection
# -> Faster than list
# -> Uses ()

# myTuple = (
#     43, 3, 44, 534, 23,
#     54, 64, 2, 5, 54,
#     3, "Ajay", "Pratap",
#     True, False, 77.7
# )

# print(len(myTuple))

# print(myTuple)

# print(myTuple[2])

# emptyTuple = ()
# -> Empty tuple

# print(emptyTuple)

# singeTuple = (1,)
# IMPORTANT:
# -> Comma is necessary for single value tuple

# print(singeTuple)

# print(myTuple.index("Ajay"))
# -> Finds index of element


# IMPORTANT DIFFERENCE
#
# List  -> mutable  -> []
# Tuple -> immutable -> ()


# =====================================================
# DICTIONARIES IN PYTHON
# =====================================================
# -> Mutable
# -> Key-value pairs
# -> Keys must be unique
# -> Uses {}

# dist = {
#     "name": "Ajay",
#     "age": 23,
#     "male": True,
#     "height": 77.7,
#     "marks": [90, 80, 70, 60, 50]
# }

# print(type(dist))

# print(dist)

# print(dist["name"])
# -> Access value using key

# print(dist["marks"])

# dist["name"] = "Pratap"
# -> Update value

# print(dist)

# print(dist.keys())
# -> Returns all keys

# print(dist.values())
# -> Returns all values

# dist["City"] = "Delhi"
# -> Add new key-value pair

# print(dist)

# dist.pop("age")
# -> Removes key-value pair

# print(dist)

# print(dist.items())
# -> Returns key-value pairs as tuples


# EASY MEMORY TRICK:
#
# keys()   -> all keys
# values() -> all values
# items()  -> both key + value
# pop()    -> remove key


# =====================================================
# SETS IN PYTHON
# =====================================================
# -> Unordered collection
# -> Unique elements only
# -> Duplicate values automatically removed
# -> Uses {}

# sets = {"Java", "Python", "C++", "JavaScript", "Python"}

# print(type(sets))

# print(sets)
# -> Duplicate "Python" removed automatically

# sets.add("Go")
# -> Adds new item

# print(sets)

# emptySet = set()
# IMPORTANT:
# -> {} creates dictionary
# -> set() creates empty set

# sets.remove("C++")
# -> Removes element

# sets.pop()
# -> Removes random element
# -> Because set is unordered

# print(sets)

# sets2 = {"Java", "Python", "C++", "JavaScript", "Go"}

# print(sets.union(sets2))
# -> Combines both sets

# print(sets.intersection(sets2))
# -> Common elements only

# sets.clear()
# -> Removes everything


# EASY REVISION:
#
# add()          -> add item
# remove()       -> remove item
# union()        -> combine sets
# intersection() -> common values
# clear()        -> empty set


# =====================================================
# REMOVE DUPLICATES USING SET
# =====================================================

list1 = [1,2,3,4,5,6,7,5,4,3,22,3,4]

# Convert list to set
# -> Removes duplicates automatically

set1 = set(list1)

print(set1)

# IMPORTANT:
# Output order may change
# Because sets are unordered


# =====================================================
# VERY IMPORTANT INTERVIEW / REVISION NOTES
# =====================================================

# LIST
# -> Ordered
# -> Mutable
# -> Duplicates allowed

# TUPLE
# -> Ordered
# -> Immutable
# -> Duplicates allowed

# DICTIONARY
# -> Key-value pairs
# -> Mutable
# -> Keys unique

# SET
# -> Unordered
# -> Unique values only
# -> Mutable


# =====================================================
# COMMON BEGINNER MISTAKES
# =====================================================

# WRONG:
# list = [1,2,3]

# WHY WRONG?
# -> list is built-in function name
# -> Avoid overwriting built-in names

# BETTER:
# myList = [1,2,3]


# =====================================================
# BETTER VERSION OF YOUR LAST CODE
# =====================================================

myList = [1,2,3,4,5,6,7,5,4,3,22,3,4]

# Remove duplicates
uniqueValues = set(myList)

print(uniqueValues)