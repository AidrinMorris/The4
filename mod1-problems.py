# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

# A simple line of string
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

# Prompts user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performs calculations based on numbers inserted and prints the final results
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
# Will stop division by zero
print("Division:", num1 / num2 if num2 != 0 else "undefined (division by zero)")

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math

# Input the lengths of the triangle's sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Will calculate the area using Heron's formula from the numbers inputed
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Will print the area that was calculated
print("Area:", area)
# Wont work if the numbers cant equal a triangle

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import statistics

# Input five numbers and saves them for calculations
numbers = [float(input("Enter a number: ")) for _ in range(5)]

# Compute and print statistics for all six
print("Total:", sum(numbers))
print("Average:", sum(numbers) / 5)
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Range:", max(numbers) - min(numbers))
print("Standard Deviation:", statistics.stdev(numbers))
