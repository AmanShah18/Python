# #Question number 1
# user_input=int(input("Enter the number:"))
# sum=0
# for i in range(1,user_input+1):
#     sum+=i
# print("The sum of total is",sum)


# #Question number 2
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

# print("The sum of Even is",even)
# print("The sum of ODD is",odd)


#Question number 3
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



#Question number 4
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


# #Question number 5
# a=[1,1,1,2,3,4,5,5,6,6,7,8,7,8,9,9,10,10,11,12,13,13]
# unique=[]
# for x in a:
#     if x not in unique:
#         unique.append(x)
# print(unique)


# #Question number 6
# a=[1,1,1,2,3,4,5,5,6,6,7,8,7,8,9,9,10,10,11,12,13,13]
# reve=[]
# for i in a[::-1]:#[start:stop:jump(-1 for backwaard)]
#     reve.append(i)
# print(reve)


