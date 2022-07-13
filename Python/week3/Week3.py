# #ODD and Evevn
# a=int(input("Enter the number:"))
# if (a%2)==0:
#     print("Its Even")
# else:
#     print("ODD")


# #Greater among theree
# a=int(input("Enter the first numnber:"))
# b=int(input("Enter the second numnber:"))
# c=int(input("Enter the third numnber:"))

# if(a>b and a>c):
#     print("First is Greater")
# elif(b>a and b>c):
#     print("Second is the gretaer")
# else:
#     print("Third  is Greater")


# HCF
# m = int(input("Enter teh first:"))
# n = int(input("Enter the second:"))
# if(n<m):
#     temp=m
#     m=n
#     n=temp

# r = 1
# while r != 0: #jaba sama r zero ayudauna

#     r = m % n

#     if r == 0:
#         print(n)
#     else:
#         m = n
#         n = r


# # Factrioal
# n=int(input("Enter the number:"))

# if n < 0:
#     print(0)
# elif n == 0 or n == 1:
#     print(1)
# else:
#     fact = 1
#     while(n > 1):
#         fact=fact*n
#         n=n-1
#     print(fact)


# # # Prime number or not
# a = int(input("Enter the number:")) #taking input

# if a > 1:# checking if its positive or not
#     for i in range(2, a):# running a loop from 2 to the numeber a
#         if(a % i) == 0: # checking if the remainder is 0
#             print("NOT Prime")
#             break

#     else:
#         print("YES prime")

# else:
#     print("Put a positive number") # if not positive



# # while loop
# a = int(input("Enter the number:"))  # taking input
# check = False # insitalizing as a boolen 
# b = 2 # using 2 as to run the look
# #when you entered 11 it will be divided and the out put willbe 5 and the loop will run five time until the b is greater than a
# #the b will be add to + 1 each time if the moduler is not 0 
# # when the moduler is 0 it will break the while loop and go to next statement and changed the boolen to true
# while b < a: 
#     if a % b == 0:
#         check = True
#         break
#     b = b+1

# #check if the value is if its divided it is not prime
# if check == True:
#     print("No it not" )
# else:
#     print("Prime number is :", a)





