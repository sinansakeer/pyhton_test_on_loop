# Question 6
# Calculate the cube of all numbers from 1 to a given number

a = int(input("Enter end point: "))
for i in range(1,a+1):
    cube = i**3
    print("Current Number is : ",i,"and the cube is",cube)