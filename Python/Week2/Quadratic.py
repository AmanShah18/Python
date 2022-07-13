# declaration of varaiables
a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
c=int(input("Enter the c:"))

# Logic of the program
x=(-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
x1=(-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a

#Output of the program or the value of x
print("The Value of X is",x)
print("The Value of X is",x1)
