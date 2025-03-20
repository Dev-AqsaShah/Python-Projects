
#!(if, elif, else)
#! question 1 
# a = int(input("PLEASE ENTER YOUR FIRST NUMBER: "))
# b = int(input("PLEASE ENTER YOUR SECOND NUMBER: "))
# if a > b:
#     print(f"{a} is greater than {b}. ")
# elif b > a:
#     print(f"{b} is greater than {a}. ")
# else:
#     print("both numbers are equal...")

#! question 2 
# gander = input("provide your gander M or F : ")

# if gander == "M":
#     print("Good Morning Sir")
# elif gander == "F":
#     print("Good Morning Ma'am")
# else:
#     print("Invalid input")

#! question 3
# a = int(input("provide your number :"))
# if a %2 == 0:
#     print("even number")
# else:
#     print("odd number")

#! question 4
# name = input("your name :")
# age = int(input("your age "))
# if age >18 :
#     print(f"{name} you can vote")
# elif age <18 and age >0:
#     print(f"{name} you can't vote")
# else:
#     print("invalid")

#! question 5
# year = int(input("your year : "))
# if year %4 == 0 and year %100 != 0:
#     print("leap year")
# elif year %100 == 0 and year %400 == 0:
#     print("leap year")
# else:
#     print("not leap year")

#! LOOPS 
#! question 1
# a = int(input("your number"))
# for i in range(1,a+1):
#     print(i)

#! question 2
# n = int(input("your number"))
# for i in range(n,0,-1):
#     print(i)

#! question 3 
# n = int(input("which number table u want? : "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

#! question 4
# n = int(input("your number"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

#! question 5
# n = int(input("please tell your number"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact *i
# print(fact)

#! question 6
# n = int(input(" your number"))
# print("all the factors are")
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i,end = "")

#! question 7 
# n = int(input("your number"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i
# if sum == n:
#     print("yes this is a strong number")
# else: 
#     print("not a strong number")

#! question 8 
# n = int(input("your num"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count +1
# if count == 2:
#     print("prime num")
# else:
#     print("composite num ")

#! question 9
# a = int(input("your number"))
# while a > 0:
#     print(a%10)
#     a = a//10

#!  STRING METHODS
#! question 10
a = "aqsa"
# b = a  #? copy
# print(len(a)) #? length

# for i in range(len(a)-1,-1,-1):
    # print(a[i])        #?reverse

# print(a[::-1])  #? reverse

#! question 11

# a = "aqsa How aRe you?"
# b = ''
# for i in a:
#     if i.islower():
#         b = b + i
# for i in a:          #? is logic m hm n kiya h k jo hamari line m capita letter h wo last m print honge or small letter pehle.
#     if i.isupper():
#         b = b + i
# print(b)

#! question 12
# str = "P@#yn26at^&i5ve"
# chr = 0
# dig = 0
# spchr = 0
# for i in str:
#     if i.isdigit():
#         dig = dig +1
#     elif i.isalpha():
#         chr = chr +1
#     else:
#         spchar = spchr = spchr +1
# print(f"your countings are \nnumbers = {dig}\ncharacters = {chr}\nspecial characters = {spchr}") 

#! question 13
# a = "hey girls im alone can i join you please"
# vowel = 0 
# const = 0
# for i in a:
#     if i in "aeiouAEIOU":
#         vowel = vowel +1
#     elif i == " ":            #? counting
#         continue
# else: 
#     const = const +1
# print(f"your total vowels are {vowel} and consonants are {const}")

#! question 14                    
# a = "aqsa"
# b = ""
# for i in range(len(a)-1,-1,-1):       #? pallindrome
#     b = b + a[i]
# if a == b:
#     print("pallindrome")
# else:
#     print("hello hello")

#! list
#! question 15
# l = []
# count = int(input("how many number you want"))
# for i in range(count):
#     z = int(input("tell your number and press enter"))
#     l.append(z)      #? for create list from input
# print(l)

#! question 16
# a = [1,2,3,4,5,6]
# b = []
# for i in range(len(a)-1,-1,-1):  #? reverse list
#     b.append(a[i])
# print(b)

# a = [1,75,9,98,58,92,48,93,99]
# max = 0
# index = 0
# for i in range(len(a)):    #? max value dega ye
#     if a[i] > max:
#         max = a[i]
#         index = i
#     print(f"your largest num is {max} at index {index}")

