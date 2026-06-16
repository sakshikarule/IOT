op1 = int(input("Enter op1 : "))
op2 = int(input("Enter op2 : "))

print("1. Add\n2. Sub\n3. mul\n4. Div")
choice = int(input("Enter your choice :"))

if choice == 1:
    print(f"{op1} + {op2} = {op1 + op2}")
elif choice == 2:
    print(f"{op1} - {op2} = {op1 - op2}")
elif choice == 3:
    print(f"{op1} * {op2} = {op1 * op2}")
elif choice == 4:
    print(f"{op1} / {op2} = {op1 / op2}")
else:
    print("invaild choice") 
              