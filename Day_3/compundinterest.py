#compund interest
P=float(input("Enter the value of P:"))
R=float(input("Enter the value of R:"))
T=float(input("Enter the value of T:"))
CI=P*(1 + R/100)** T - P
SI=(P*R*T)/100
print("The Compound interest is:",CI) 
print("The Simple interest is:",SI)
