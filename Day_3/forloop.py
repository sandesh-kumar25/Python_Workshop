"""WAP TO FIND FACTORIAL USING FOR LOOP"""
n=int(input("Enter the value of n:"))
j=1
for i in range(1,n+1):
    j=j*i
print(f"The factorial of {n} is {j}") #OR use print("The factorial is",j) 
