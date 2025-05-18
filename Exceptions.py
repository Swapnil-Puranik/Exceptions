# Task 1 - Handling Division with Exceptions

while True:
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"100 divided by {num} is {result}.")
        break

print("-"*40 )

#Task 2 - Raising and Handling Different Exceptions

# IndexError Example
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Accessing index 5, which doesn’t exist
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError Example
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])  # 'age' key doesn't exist
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError Example
try:
    result = "Hello" + 5  # Can't add str and int
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

print("-"*40)

#Task 3 - try...except...else...finally Structure

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
