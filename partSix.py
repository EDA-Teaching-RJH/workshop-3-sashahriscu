student = input("Are you a student?: ").lower()
age = int(input("Enter age: "))

if age <12 or age >=65:
    price = 5
elif student == "yes":
    price = 8
else:
    price = 10

print(f"Your ticket is £{price}")
