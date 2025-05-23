# oop in python 
# to map with real world scenarios, we started using objects in code. this is called object oriented programming.

# class & object in python
# class is a blueprint for creating objects.

# class Student:
#     name = "aqsa shah"
    
    
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)



# __init__ function
# constructor
# all classes have a finction called _init_(), which is always executed when the class is being initiated.

# class Student:
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in Database.")

# s1 = Student("aqsa")
# print(s1.name)



# CLASS & INSTANCE ATTRIBUTES


# class Person:
#     def __init__(self, name, age, Rollno):
#         self.name = name
#         self.age = age
#         self.Rollno = Rollno

#     def get_info(self):
#         return f'Name: {self.name}, age: {self.age}, Rollno: {self.Rollno}'

#     def change_name(self, new_name):
#        self.name = new_name
#        return f'Name changed to {self.name}'

# person1:Person = Person("Aqsa Shah", 20, 17)
# print(person1)



