#variable 
age=21

print(age)
print(f"you are {age} years old")


#Integer
ages=21
player=4
quantity=3

print(f"you are {ages} years. and you play with {player} players. you have {quantity} balls")


#Float
a = 10.5
b = 2.0

print(a + b)   # 12.5
print(a - b)   # 8.5
print(a * b)   # 21.0
print(a / b)   # 5.25


#string
name="Bro"
email="Bro123@gmail.com"

print(f"im {name} and you can send mail about your new offers to my mail {email}")


#Boolean
age = 25

if age >= 18:
    print("Adult")
else:
    print("Minor")



#challenge-calculate area of rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print("Area of the rectangle is:", area)
