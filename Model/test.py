import math

# Function to evaluate user input
def evaluate_function():
    # Get user input for the function
    user_function = input("Enter a mathematical function (e.g., sin(x), cos(x)): ")

    # Get user input for the value at which to evaluate the function
    value = float(input("Enter the value at which you want to evaluate the function: "))

    try:
        # Evaluate the function at the given value
        result = eval(user_function.replace("x", str(value)))
        print(f"The result of {user_function} at {value} is: {result}")
    except Exception as e:
        print("Error:", e)

# Call the function
evaluate_function()