print("Enter principal: ")
principal = float(input())

print("Enter rate of interest: ")
rate = float(input())

print("Enter time: ")
time = float(input())

si = (principal * rate * time) / 100
ci = principal * ((1 + rate / 100) ** time) - principal

print("Simple Interest =", si)
print("Compound Interest =", ci)
