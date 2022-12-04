# Question 3
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

a = int(input("Enter number: "))
Sum = 0
for i in range(1,a+1):
    Sum = Sum + i
print(Sum)