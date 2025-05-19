# Task 1: Calculate area and perimeter of a rectangle

length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)




# Task 2: Compare two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("First number is greater than the second.")
elif num1 < num2:
    print("First number is less than the second.")
else:
    print("Both numbers are equal.")
    




# Task 3: Check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")    
    
    
    
    
# Task 4: Arithmetic and logical operations

a = 15
b = 4

# Arithmetic
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Logical
x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)




# Task 5: Concatenate and print two strings

str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print("Concatenated string:", result)