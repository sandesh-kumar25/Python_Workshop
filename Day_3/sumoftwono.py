num1 = float(input("Enter 1st number: "))
num2= float(input("Enter 2nd number: "))
addition = num1+num2
print("Addition of them is:",addition)
    
#if use z=num1+num2 not add them , because python by deafult taking considering string.s
print("{}+{}={}".format(num1,num2,addition)) #this is format method
# f is string method
print(f"x:{num1} + y:{num2} = z:{addition}")
