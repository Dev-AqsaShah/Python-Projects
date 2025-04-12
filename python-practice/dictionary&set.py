# dictionary
# dictionaries are used to stor data values in key.value pairs
# they are unordered mutable(changeable) and dont allow duplicate keys
# ditionary ko hm curly brackets m likhte hn
# info = {
#     "key" : "value",
#     "name" : "aqsa",
#     "leaning" : "codding",
#     "age" : 20,
#     "is_adult" : True,
#     "marks" :94.4
# }
# print(info)
# is m hm list or tupls ko bhi likh sakt hn

#nested dictionary
# student = {
#     "name" : "aqsa",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }
# print(list(student.keys{}))
# print(student["subject"] ["chem"])

# dictionary m dublicat value allow nhi hoti 
# student = {
#     "name" : "aqsa",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95
#     }
# }
# new_dict = {"name": "aqsu", "age": 20}
# student.update(new_dict)

# print(student)


# SET IN PYTHON
# set is mutable
# set is the collection of the unordered items.
# each elements in the set must be unique and immutable
# set duplicat valu ko ignor krta h
# collection = {1, 2, 3, 4, "aqsa"}
# print(collection)
# print(type(collection))

# set methods
# set.add(el) adds an element
# set.remove(el) removes the element 
# set.clear() empties the set
# set.pop() removes a random value

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add((1, 2, 4)) tupl add kr sakte hn
# collection.([1,2,4]) list add nhi kr sakte error ayega
# collection.remove(2)
# collection.clear()
# print(collection)
# set k ander hashable values ati hn mtlb immutable

# collection = {"hello", "aqsa", "fasih"}
# print(collection.pop())
# print(collection.pop())

# set.union(set2) combines both set values & returns new
# set.intersection(set2) combines common values and return new

# set1 = {1, 2, 3}
# set2 = {1, 2, 3}

# print(set1.union(set2)) ans {1,2,3,4}
# print(set1)


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.intersection(set2)) ans {2,3,}
# print(set1)

# PRACTICE QUESTION 1
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts and figures"]

# }

# print(dictionary)

# q2

# subjects = {
#     "python", "java", "c++", "python", "javascript", "java",
#     "python", "java", "c++", "c"
# }
# print(len(subjects))