# Question 4
# Write a program to use for loop to print the following reverse number pattern

a = int(input("Enter how big the pattern should be: "))
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()