# Question 2
# Write a program to use for loop to print the following reverse number pattern

a = int(input("enter how big the pattern should be"))

for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")