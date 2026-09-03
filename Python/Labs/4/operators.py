# number = float(input("Enter Your Number:"));

# if number%2 == 0:
#     print("Even");
# else:
#     print("Odd");
    
    
    
# a= int(input("Enter Your 1st Number:"));
# b =int(input("Enter Your 2nd Number:"));
# c= int(input("Enter Your 3rd Number:"));

# if a>b and a>c:
#     print("A is the greatest");
# elif b>a and b>c:
#     print("B is the greatest");
# else:
#     print("C is the greatest");


# >=80 A , 60-80 B , 40-60 C ,<40 F


cst = float(input("Enter Your Marks in CST:"));
bscp = float(input("Enter Your Marks in BSCPS:"));
maths = float(input("Enter Your Marks in Maths:"));
progAi = float(input("Enter Your Marks in Prog AI:"));

total = cst+bscp+maths+progAi;
percentage = total/4;

if percentage>=80:
    print("A");
elif percentage>=60 and percentage<80:
    print("B");
elif percentage>=40 and percentage<60:
    print("C");
else:
    print("F");