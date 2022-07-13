# #Question number 1
# number=int(input("Enter the number of elements:"))#upto where you want the list
# lst=[]

# for i in range(0,number):#loop uo to the range
#     ele=int(input("Enter element:"))#Enterting the number
#     lst.append(ele)#adding to the list
# print(lst)

# even=0
# odd=0

# for i in range(0,number):
#     if lst[i] %2==0:
#         even +=lst[i]
#     else:
#         odd +=lst[i]

#print("The sum of Even is",even)
#print("The sum of ODD is",odd)


#Question number 2
# number=int(input("Enter the number of elements:"))#upto where you want the list
# lst=[]
# for i in range(0,number):#loop uo to the range
#     ele=int(input("Enter Element:"))#Enterting the number
#     lst.append(ele)#adding to the list
# print(lst)
# smallest=lst[1]
# biggest=0
# for j in range(number):
#     if (smallest > lst[j]):
#         smallest=lst[j]
#     if (biggest< lst[j]):
#         biggest=lst[j]
# print("The minium number is ",smallest)
# print("The maximum number is",biggest)




# print("The maximum is ",max(lst))
# print("The minium is ",min(lst))



#Question number 3
# a=int(input("Enter the terms:"))
# b=1                                        
# c=1     
# lst=[]                                    
# if a<=0:
#     print("The requested series is 0")
# else:
#     #print(b,c,end=" ")
#     lst.append(b)
#     lst.append(c)
#     for x in range(2,a):        
#         next=b+c                           
#         #print(next,end=" ")
#         lst.append(next)
#         b=c
#         c=next
# print(lst)
