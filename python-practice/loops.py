# count = 1
# while count<= 5 :
#     print("aqsa")
#     count += 1
# print(count)

# i = 1
# while i <= 10:
#     print(i)
#     i += 5
    
# print("end")
    
    
# q1
# print num from 1 to 100
# print num from 100 to 1
# print the multiplication tabl of a num n 
# print the elements of the following list using a loop
# search for a number x in this tuple using loop

# i = 1
# while i >+ 100:  stooping 
    # print(i)
    # i += 
    
# q3
# n = int(input("entr num:"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# q4
# num = [1,4,9,16,25,36,49,64,81,100]
# heros = ["aqsa", "fasih", "no", "haan"]

# traverse mtlb ek ek 
# idx = 0
# while idx < len(heros):
#     print(heros[idx])
#     idx += 1
    

# idx = 0 
# while idx < len(num):
#     print(num[idx]) #nums[0], nums[1], nums[2]
#     idx +- 1


num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36 )
x = 36

i = 0
while i < len(num):
    if(num[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding..")
    i += 1
    
#! break keyword : used to terminate the loop when encountered
#! continue : terminates execution in the current iteration & continues execution of the loop with the next iteration
# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1


#?  for loop 
#? loops are used for sequential traversal. for traversal for traversing list string tuples 

# q1 print th elements of the folloing list using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# search for a num x in this tupl using loop 
# [1, 4, 9, 16, 25, 36, 49, ]

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# x = 49

# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#     idx += 1
    
    #! range()
    
    # for i in range(10):  #range(stop)
    #     print(i)
        
    # for i in range(2, 10): #range(start, stop)
    #     print(i)
        
    #! pass statement
    #? pass is a null statement that does nothing it is used as a placeholder for future code.
    # for i in range(5):
    #     pass
    # print("some useful work")