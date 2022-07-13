# Question number 1
# a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]
# div = []

# for i in a:
#     if i%2==0 and i%3 ==0:
#         div.append(i)

# print(div)


# Question number 2
# a=[43, 23, 21, 44, 56, 75]
# b=[]
# for i in range(len(a)):
#     if i %2==0:
#         b.append(a[i+1])
# print(b)


# Question number 3
# a=["a","b","c"]
# b=[1,2,3]
# c=[]
# for i in range(0,len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)


# Question number 4
# a=[1, 2, 3, 4, 5, 6]
# b=[1, 2, 3, 4, 5, 6]
# c=[]
# for i in range(len(a)):
#     d=a[i]+b[i]
#     c.append(d)
# print(c)

# Bubble sort
# list = [3, 1, 5, 8, 2, 10, 4,2,1,3,99,80,70,60,40,30]
# sort = False
# while sort == False:
#     num_swap = 0
#     for i in range(1, len(list)):
#         if list[i-1] > list[i]:
#             tmp = list[i-1]
#             list[i-1] = list[i]
#             list[i] = tmp
#             num_swap = num_swap+1
#     # print(list)
#     if num_swap == 0:
#         sort = True
#     else:
#         sort = False
# print(list)


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
 
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
 
        # if nothing moved, then array is sorted.
        if (swapped==False):
            break
 
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
 
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
 
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start+1
 
# Driver code to test above
a = [5, 1, 4, 2, 8, 0, 2]
cocktailSort(a)
print("Sorted array is:")
smallest=a[0]
biggest=0
for i in range(len(a)):
    print ("%d" %a[i], end=" ")
    print( )
for j in range (0,len(a)):
    if (smallest > a[j]):
        smallest=a[j]
    if (biggest< a[j]):
        biggest=a[j]
print("The minium number is ",smallest)
print("The maximum number is",biggest)

