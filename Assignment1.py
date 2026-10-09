# 1. Check if a number is positive, negative, or zero.

print("1. Check if a number is positive, negative, or zero.")

num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} : Positive")
elif num < 0:
    print(f"{num} : Negative")
else:
    print(f"{num} : Zero")

# 2. Check whether a number is even or odd.

print("2. Check whether a number is even or odd.")

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"Even: {num}")
else:
    print(f"Odd: {num}")

# 3. Find the greater of two numbers.

print("3. Find the greater of two numbers.")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(f"Number: {a} is greater than Number: {b}")
elif b > a:
    print(f"Number: {b} is greater than Number: {a}")
else:
    print("Both numbers are equal.")

# 4. Find the greatest of three numbers.

print("4. Find the greatest of three numbers.")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"Greatest Number: {a}")
elif b >= a and b >= c:
    print(f"Greatest Number: {b}")
else:
    print(f"Greatest Number: {c}")

# 5. Check if a person is eligible to vote (age >= 18).

print("5. Check if a person is eligible to vote (age >= 18).")

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

# 6. Check whether a year is a leap year.

print("6. Check whether a year is a leap year.")
import calendar
year = int(input("Enter year: "))

if calendar.isleap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 7. Check if a character is a vowel or consonant.

print("7. Check if a character is a vowel or consonant.")

character = input("Enter an alphabet: ").lower()

if len(character) != 1 or not character.isalpha():
    print("Please enter a single alphabet.")
elif character in "aeiou":
    print(f"{character} is a vowel")
else:
    print(f"{character} is a consonant")

# 8. Check whether a number is divisible by 5 and 11.

print("8. Check whether a number is divisible by 5 and 11.")

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
else:
    print(f"{num} is not divisible by both 5 and 11")

# 9. Check if a number is a multiple of both 3 and 7.

print("9. Check if a number is a multiple of both 3 and 7.")

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 3 and 7")
else:
    print(f"{num} is not a multiple of both 3 and 7")

# 10. Assign grades based on marks.

print("10. Assign grades based on marks.")

marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Enter a value from 0 to 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 11. Check if a character is uppercase or lowercase.

print("11. Check if a character is uppercase or lowercase.")

character = input("Enter a character: ")

if len(character) != 1 or not character.isalpha():
    print("Please enter a single alphabet.")
elif character.isupper():
    print(f"{character} is uppercase")
else:
    print(f"{character} is lowercase")

# 12. Find whether the entered alphabet is a vowel using if-elif.

print("12. Find whether the entered alphabet is a vowel using if-elif.")

character = input("Enter an alphabet: ").lower()

if len(character) != 1 or not character.isalpha():
    print("Please enter a single alphabet.")
elif character == "a":
    print("Vowel")
elif character == "e":
    print("Vowel")
elif character == "i":
    print("Vowel")
elif character == "o":
    print("Vowel")
elif character == "u":
    print("Vowel")
else:
    print("Consonant")

# 13. Check if three sides can form a triangle.

print("13. Check if three sides can form a triangle.")

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if (side1 > 0 and side2 > 0 and side3 > 0
        and side1 + side2 > side3
        and side1 + side3 > side2
        and side2 + side3 > side1):
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")

# 14. Determine the type of triangle.

print("14. Determine the type of triangle (Equilateral, Isosceles, Scalene).")

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if (side1 <= 0 or side2 <= 0 or side3 <= 0
        or side1 + side2 <= side3
        or side1 + side3 <= side2
        or side2 + side3 <= side1):
    print("The sides cannot form a triangle.")
elif side1 == side2 and side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# 15. Find the largest among four numbers.

print("15. Find the largest among four numbers.")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print(f"Largest number: {a}")
elif b >= a and b >= c and b >= d:
    print(f"Largest number: {b}")
elif c >= a and c >= b and c >= d:
    print(f"Largest number: {c}")
else:
    print(f"Largest number: {d}")

# 16. Check whether a number is a three-digit number.

print("16. Check whether a number is a three-digit number.")

num = int(input("Enter an integer: "))

if 100 <= abs(num) <= 999:
    print(f"{num} is a three-digit number")
else:
    print(f"{num} is not a three-digit number")

# 17. Calculate electricity bill using slab rates.

print("17. Calculate electricity bill using slab rates.")

units = float(input("Enter electricity units used: "))

if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 300:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6
    print(f"Electricity bill: {bill:.2f}")

# 18. Calculate income tax based on income slabs.

print("18. Calculate income tax based on income slabs.")

income = float(input("Enter annual income: "))

if income < 0:
    print("Income cannot be negative.")
else:
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 250000 * 0.05 + (income - 500000) * 0.20
    else:
        tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30
    print(f"Income tax: {tax:.2f}")

# 19. Check if a student passes (minimum 35 marks in each subject).
print("19. Check if a student passes (minimum 35 marks in each subject).")

subject1 = float(input("Enter marks in subject 1: "))
subject2 = float(input("Enter marks in subject 2: "))
subject3 = float(input("Enter marks in subject 3: "))

if subject1 >= 35 and subject2 >= 35 and subject3 >= 35:
    print("Student passes")
else:
    print("Student fails")

# 20. Find whether a number is within a given range.
print("20. Find whether a number is within a given range.")

num = float(input("Enter a number: "))
lower = float(input("Enter range start: "))
upper = float(input("Enter range end: "))

if lower > upper:
    print("Invalid range: start must not be greater than end.")
elif lower <= num <= upper:
    print(f"{num} is within the range")
else:
    print(f"{num} is outside the range")

# 21. Build a simple calculator using if-elif-else.
print("21. Build a simple calculator (+, -, *, /).")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {num1 / num2}")
else:
    print("Invalid operator.")

# 22. Check if a year is a century leap year.
print("22. Check if a year is a century leap year.")

year = int(input("Enter year: "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a century leap year")
else:
    print(f"{year} is not a century leap year")

#23. Determine the season based on the month number.

print("23. Determine the season based on the month number.")

month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month number.")
elif month in (3, 4):
    print("Spring")
elif month in (5, 6):
    print("Summer")
elif month in (7, 8):
    print("Monsoon")
elif month in (9, 10):
    print("Autumn")
elif month in (11, 12):
    print("Pre-winter")
else:
    print("Winter")

# 24. Find the number of days in a month.
print("24. Find the number of days in a month.")

month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month number.")
elif month == 2:
    year = int(input("Enter year: "))
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("February has 29 days")
    else:
        print("February has 28 days")
elif month in (4, 6, 9, 11):
    print("This month has 30 days")
else:
    print("This month has 31 days")

# 25. Check if a password meets minimum conditions.

print("25. Check if a password meets minimum conditions.")

password = input("Enter password: ")

has_uppercase = any(character.isupper() for character in password)
has_lowercase = any(character.islower() for character in password)
has_digit = any(character.isdigit() for character in password)
has_special = any(not character.isalnum() for character in password)

if (len(password) >= 8 and has_uppercase and has_lowercase
        and has_digit and has_special):
    print("Password meets the minimum conditions.")
else:
    print("Password does not meet the minimum conditions.")

# 26. Determine ticket price based on age category.

print("26. Determine ticket price based on age category.")

age = int(input("Enter age: "))

if age < 0:
    print("Age cannot be negative.")
elif age < 13:
    print("Ticket price: 100")
elif age < 60:
    print("Ticket price: 200")
else:
    print("Ticket price: 150")

# 27. Calculate discount based on purchase amount.

print("27. Calculate discount based on purchase amount.")

amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Purchase amount cannot be negative.")
else:
    if amount >= 10000:
        discount_rate = 0.15
    elif amount >= 5000:
        discount_rate = 0.10
    elif amount >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0
    discount = amount * discount_rate
    print(f"Discount: {discount:.2f}")
    print(f"Amount to pay: {amount - discount:.2f}")

# 28. Check if a person is eligible for a driving license.
print("28. Check if a person is eligible for a driving license.")

age = int(input("Enter age: "))
has_good_eyesight = input("Is eyesight adequate? (yes/no): ").lower()

if age >= 18 and has_good_eyesight == "yes":
    print("Eligible for a driving license")
else:
    print("Not eligible for a driving license")

# 29. Create a login system with username and password validation.

print("29. Create a login system with username and password validation.")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "Pass123!":
    print("Login successful")
else:
    print("Invalid username or password")

# 30. Create a menu-driven calculator using if-elif-else.
print("30. Create a menu-driven calculator.")

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting calculator.")
        break
    elif choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid choice.")