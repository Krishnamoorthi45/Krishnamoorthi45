1. You are developing a Python program for an online food ordering system that includes decision-making elements. The system should allow users to browse a menu, add items to their cart, specify delivery details, and place orders. Additionally, the system should dynamically apply discounts based on order totals, validate delivery addresses for availability, and adjust delivery times based on current order volume.
Your program should include the following functionalities incorporating decision-making logic:
Dynamic Discounts: Implement a system that automatically applies discounts based on the total amount of the order. For example, offer a 10% discount for orders above $50 and a 15% discount for orders above $100.
•        Test Case Description: Verify that discounts are applied correctly based on the total order amount.
•        Input: User adds items to the cart, resulting in different total amounts.
•        Expected Output: Discounts are applied according to predefined thresholds, and the order total reflects the correct discounted amount.

Address Validation: Validate delivery addresses to ensure they are within the delivery radius of the restaurant. If the address is outside the delivery area, prompt the user to choose another address or opt for pickup.
•        Test Case Description: Test the system's ability to validate delivery addresses.
•        Input: User enters different delivery addresses, some within the delivery radius and some outside.
•        Expected Output: Valid addresses are accepted, while invalid addresses prompt the user to choose another address or opt for pickup.


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

class OrderSystem:
    DISCOUNT_THRESHOLDS = {
        50: 0.10,
        100: 0.15
    }

    def __init__(self):
        self.shopping_cart = ShoppingCart()

    def apply_discount(self, total_amount):
        discount_rate = 0
        for threshold, rate in self.DISCOUNT_THRESHOLDS.items():
            if total_amount >= threshold:
                discount_rate = max(discount_rate, rate)
        return total_amount * (1 - discount_rate)

    def validate_address(self, address):
        # Add logic to validate address within delivery radius
        pass

    def place_order(self, delivery_address):
        total_amount = self.shopping_cart.calculate_total()
        discounted_amount = self.apply_discount(total_amount)
        if self.validate_address(delivery_address):
            # Proceed with order
            print(f"Order total: ${discounted_amount:.2f}")
            # Add logic to adjust delivery time based on order volume
        else:
            print("Delivery address is not valid. Please choose another address or opt for pickup.")

def main():
    order_system = OrderSystem()

    # Test dynamic discounts
    cart = order_system.shopping_cart
    cart.add_item(MenuItem("Pizza", 20))
    cart.add_item(MenuItem("Burger", 40))
    cart.add_item(MenuItem("Salad", 35))
    total_amount = cart.calculate_total()
    discounted_amount = order_system.apply_discount(total_amount)
    print(f"Total amount: ${total_amount:.2f}, Discounted amount: ${discounted_amount:.2f}")

    # Test address validation
    delivery_address = "123 Main St, City, State, ZIP"
    order_system.validate_address(delivery_address)

if __name__ == "__main__":
    main()
[20/05, 8:55 am] Chandru: 1.        Write a Python program to check if a given number is positive, negative, or zero 
 n=int(input("Enter to a number to find positive or negative :"))
 if n==0:
     print(f"{n} it is  Zero")
 elif n>0:
     print(f"{n} is Positive")
 else:
     print(f"{n} is Negative.")



2.        Create a program that takes a user's age as input and outputs whether they are eligible to vote or not (considering the legal voting age is 18).

 age=int(input("Enter your age : "))
 if age>=18:
     print("Your are eligible for voting ")
 else:
     print("Your are not eligible for voting ")



3.        Write a Python program to determine whether a given year is a leap year or not

 y=int(input("Enter year to find leap year or not :"))
 if (y%4==0 and y%100==0 ) and y%400==0:
     print(f"{y} is Leap year..")
 elif (y%4==0 and y%100!=0 ) and y%400!=0:
     print(f"{y} is Leap year..")
 else:
     print(f"{y} is Not a Leap year..")



4.        Develop a program that takes a user's temperature as input and outputs whether they have a fever or not (considering a fever if temperature is equal to or above 100.4°F or 38°C).

 h=int(input("Enter your choice 1.Faherinheit or 2.Celsius:"))
 if h==1:
     f=float(input("Enter the temperature in Faherinheit :"))
     if f>=100.4:
         print("You have a fever")
     else:
         print("You have no fever..")
 elif h==2:
     c=float(input("Enter the temperature in Celsius :"))
     if c>=32:
         print("You have a fever")
     else:
         print("You have no fever..")
 else:
     print("Invalid Input...")



5.        Create a Python program to find the largest among three numbers entered by the user.
 a,b,c=input("Enter any three number :")
 if a>b and a>c:
     print(f"{a} is the biggest number")
 elif b>a and b>c:
     print(f"{b} is the biggest number")
 else:
     print(f"{c} is the biggest number")



6.        Write a program to calculate the total cost of a meal, including tax and tip, based on user input for the meal cost and percentage rates for tax and tip.

 cost=int(input("Enter the cost of the meals :"))
 tax=float(input("Enter the tax :"))
 tip=float(input("Enter the tips :"))
 taper=(tax*cost)/100
 tiper=(tip*cost)/100
 print("The total cost for meals (incl tax and tip) : ",cost+taper+tiper)



7.        Develop a program to classify a triangle based on the lengths of its sides (scalene, isosceles, or equilateral).

 s1,s2,s3=input("Enter the three sides of a triangle :")
 if s1==s2==s3:
     print("Its is Equilateral Triangle ")
 elif s1==s2 or s1==s3 or s2==s3:
     print("Its is Isoceles Triangle")
 else:
     print("Its is Scalene Triangle")



8.        Create a program that determines whether a given year is a leap year and has 366 days or a common year with 365 days.
 y=int(input("Enter year to find leap year or not :"))
 if (y%4==0 and y%100==0 ) and y%400==0:
     print(f"{y} is Leap year..\nIts has 366")
 elif (y%4==0 and y%100!=0 ) and y%400!=0:
     print(f"{y} is Leap year..\nIts has 366")
 else:
     print(f"{y} is Not a Leap year..\nIts has 365")



9.        Write a Python program to check whether a character entered by the user is a vowel or a consonant.
 ch=input("Enter the character to check for vowels or not :")
 vo=['a','e','i','u','o']
 if ch in vo:
     print("The Character is Vowels...")
 else:
     print("The Character is not Vowels...")


10.        Write a Python program that prompts the user to enter three numbers and then outputs them in ascending order.
 a,b,c=input("Enter any three number :")
 k=sorted([a,b,c])
 print(f"The numbers in ascending order :")
 for i in k:
     print(i,end=" ")
[20/05, 8:55 am] Chandru: 1. Develop a program that takes a user's score as input and outputs their corresponding grade based on the following grading scale: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59).
•        Test Case 1: Input score: 85. Expected output: Grade B.
•        Test Case 2: Input score: 60. Expected output: Grade D.
•        Test Case 3: Input score: 95. Expected output: Grade A.

def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 0 <= score <= 59:
        return "F"
    else:
        return "Invalid score"

test_cases = [85, 60, 95]
expected_outputs = ["B", "D", "A"]

for i, test_case in enumerate(test_cases):
    result = get_grade(test_case)
    print(f"Input score: {test_case}. Expected output: Grade {expected_outputs[i]}. Actual output: Grade {result}.")


2. Create a program that simulates a simple ATM machine, prompting the user for their account balance and withdrawal amount, then outputs whether the transaction is successful or not based on the available balance and withdrawal amount.
•        Test Case 1: Account balance: $1000, Withdrawal amount: $500. Expected output: Transaction successful.
•        Test Case 2: Account balance: $200, Withdrawal amount: $300. Expected output: Insufficient funds.
•        Test Case 3: Account balance: $1500, Withdrawal amount: $1500. Expected output: Transaction successful

def atm_simulation():
    # Prompt the user to enter their account balance
    try:
        account_balance = float(input("Enter your account balance: $"))
    except ValueError:
        print("Invalid input. Please enter a valid number for the account balance.")
        return

    # Prompt the user to enter the withdrawal amount
    try:
        withdrawal_amount = float(input("Enter the withdrawal amount: $"))
    except ValueError:
        print("Invalid input. Please enter a valid number for the withdrawal amount.")
        return

    # Check if the withdrawal amount is less than or equal to the account balance
    if withdrawal_amount <= account_balance:
        print("Transaction successful.")
    else:
        print("Insufficient funds.")

# Run the ATM simulation
if _name_ == "_main_":
    atm_simulation()

3. Design a program that calculates the roots of a quadratic equation ax^2 + bx + c = 0 based on user input for the coefficients a, b, and c, and outputs the roots
•        Test Case 1: Coefficients: a=1, b=-3, c=2. Expected output: Roots: 2.0, 1.0.
•        Test Case 2: Coefficients: a=2, b=5, c=2. Expected output: Roots: -0.5, -2.0.
•        Test Case 3: Coefficients: a=1, b=-4, c=4. Expected output: Roots: 2.0, 2.0.

import math

def calculate_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root (double root)
        root = -b / (2*a)
        return root, root
    else:
        # No real roots
        return None, None

def main():
    try:
        # Prompt user for coefficients a, b, and c
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        # Calculate roots
        root1, root2 = calculate_roots(a, b, c)

        if root1 is not None and root2 is not None:
            print(f"Roots: {root1}, {root2}")
        else:
            print("No real roots.")

    except ValueError:
        print("Invalid input. Please enter valid numbers for the coefficients.")

if _name_ == "_main_":
    main()

4. Develop a program that takes a user's age and gender as input and outputs their recommended heart rate range during exercise based on the American Heart Association's guidelines.
•        Test Case 1: Age: 30, Gender: Male. Expected output: 93 - 157 bpm.
•        Test Case 2: Age: 45, Gender: Female. Expected output: 88 - 149 bpm.
•        Test Case 3: Age: 55, Gender: Male. Expected output: 85 - 145 bpm.


def calculate_target_heart_rate(age, gender):
    if gender.lower() == 'male':
        max_heart_rate = 220 - age
    elif gender.lower() == 'female':
        max_heart_rate = 226 - age
    else:
        return "Invalid gender input. Please enter 'male' or 'female'."

    lower_limit = int(0.5 * max_heart_rate)
    upper_limit = int(0.85 * max_heart_rate)

    return lower_limit, upper_limit

def main():
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")

    lower_limit, upper_limit = calculate_target_heart_rate(age, gender)
    if isinstance(lower_limit, int) and isinstance(upper_limit, int):
        print("Recommended heart rate range during exercise:", lower_limit, "-", upper_limit, "bpm")
    else:
        print(lower_limit)

if _name_ == "_main_":
    main()

5.Write a program that prompts the user to enter a month and year and then outputs the number of days in that month (considering leap years for February).
•        Test Case 1: Input month: February, year: 2020. Expected output: 29 days.
•        Test Case 2: Input month: April, year: 2023. Expected output: 30 days.
•        Test Case 3: Input month: December, year: 2021. Expected output: 31 days.


import calendar

def get_days_in_month(month, year):
    # Capitalizing the first letter of the month for consistency
    month = month.capitalize()

    # Getting the index of the month (1 for January, 2 for February, ..., 12 for December)
    month_index = list(calendar.month_name).index(month)

    # Using the monthrange function to get the number of days in the specified month and year
    num_days = calendar.monthrange(year, month_index)[1]

    return num_days

def main():
    month = input("Enter the month: ")
    year = int(input("Enter the year: "))

    days_in_month = get_days_in_month(month, year)

    print(f"Number of days in {month}, {year}: {days_in_month} days")

if _name_ == "_main_":
    main()