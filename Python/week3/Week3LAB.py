# # Question number 1 
# input1=int(input("Enter First number:"))
# input2=int(input("Enter Second number:"))
# if input2>input1:
#     print("The second",input2,"number is greater")
# else:
#      print("The First",input1,"number is greater")


# #Question numebr 2
# input1=int(input("Enter the number:"))
# if input1 % 2==0:
#     print("Even")
# else:
#     print("ODD")


# #Question number 3
# day=input("Enter the day:")
# if day=="Saturday":
#     print("Happy weekday! Work hard!")
# else:
#     print("Enjoy your weekend!")



# #Question number 4
# name = input("Enter your name:")
# English=int(input("Enter your marks in English:"))
# Math=int(input("Enter your marks in Math:"))
# Nepali=int(input("Enter your marks in Nepali:"))
# Science=int(input("Enter your marks in Science:"))
# Social=int(input("Enter your marks in Social:"))
# Avg= (English+Math+Nepali+Science+Social)/5
# print("The name of student is ",name)
# print("The marks of English is ",English)
# print("The marks of Math is ",Math)
# print("The marks of Nepali is ",Nepali)
# print("The marks of Science is ",Science)
# print("The marks of Social is ",Social)
# print("The average marks is",Avg,"%")
# print("You have Scored:")
# if Avg>=70 and Avg<=100:
#     print("You have Scored A")
# elif Avg>=60 and Avg<=69:
#     print("You have Scored B")
# elif Avg>=50 and Avg<=59:
#     print("You have Scored C")
# elif Avg>=43 and Avg<=49:
#     print("You have Scored D")
# elif Avg>=40 and Avg<=42:
#     print("You have Scored E")
# elif Avg>=0 and Avg<=39:
#     print("You have Scored F")
# else:
#     print("Invalid Input")


# Question number 5
# # while loop
# a = int(input("Enter the number:"))  # taking input
# check = False # insitalizing as a boolen 
# b = 2 # using 2 as to run the look
# #when you entered 11 it will be divided and the out put willbe 5 and the loop will run five time until the b is greater than a
# #the b will be add to + 1 each time if the moduler is not 0 
# # when the moduler is 0 it will break the while loop and go to next statement and changed the boolen to true
# while b <= a/2: 
#     if a % b == 0:
#         check = True
#         break
#     b = b+1

# #check if the value is if its divided it is not prime
# if check == True:
#     print("No it not" )
# else:
#     print("Prime number is :", a)



#Question number 7
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


# Question number 8
# a=int(input("Enter the terms:"))
# b=1                                        
# c=1                                         
# if a<=0:
#     print("The requested series is 0")
# else:
#     print(b,c,end=" ")
#     for x in range(2,a):        
#         next=b+c                           
#         print(next,end=" ")
#         b=c
#         c=next



# # Prime number or not
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