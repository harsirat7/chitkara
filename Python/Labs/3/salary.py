basicSalary = int(input("Enter Basic Salary:"));
hra = int(input("Enter HRA:"));
da = int(input("Enter DA:"));
inc=int(input("Enter Incentives:"));
gross = basicSalary+(hra/100)+basicSalary+(da/100)+basicSalary+inc;
print("Gross Salary:",gross);