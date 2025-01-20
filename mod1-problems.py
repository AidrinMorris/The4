# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
def main():
    output = ("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. "
              "Then, everything changed when the Fire Nation attacked.")
    print(output)

if __name__ == "__main__":
    main()

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
def main():
    # Will prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Will perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Will handle division with a check for division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "undefined (cannot divide by zero)"

    # Will output the results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

if __name__ == "__main__":
    main()
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math

def main():
    # Prompt the user for the lengths of the sides of the triangle
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    # Check if the triangle inequality holds
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter
        s = (a + b + c) / 2

        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Output the area
        print(f"The area of the triangle is: {area}")
    else:
        print("The provided lengths do not form a valid triangle.")

if __name__ == "__main__":
    main()
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import statistics

def main():
    # Will prompt the user for five numbers
    numbers = []
    for i in range(1, 6):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)

    # Will calculate statistics
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    range_value = maximum - minimum
    std_deviation = statistics.stdev(numbers)

    # Will output the statistics
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Range: {range_value}")
    print(f"Standard Deviation: {std_deviation}")

if __name__ == "__main__":
    main()
