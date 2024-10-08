#write a program to find the median of 3 numbers without using the sort() function

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a > b and a < c) or (a > c and a < b):
    median = a
elif (b > a and b < c) or (b > c and b < a):
    median = b
else:
    median = c

print(f"The median of {a}, {b}, and {c} is {median}.")