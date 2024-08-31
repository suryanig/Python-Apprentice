"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import Tk, messagebox, simpledialog
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
num1 = simpledialog.askinteger(None, prompt="What is the first number you would like?")
# Ask the user for the second number
num2 = simpledialog.askinteger(None, prompt="What is the second number you would?")
# Ask the user for the math operation
operation = simpledialog.askstring(None, prompt = "Would you like to add, subtract, multiply, or divide these two number.")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == "add":
    answer = num1 + num2
elif operation == "subtract":
    answer = num1 - num2
elif operation == "multiply":
    answer = num1 * num2
elif operation == "divide":
    answer = num1/num2
else:
    messagebox.showerror
messagebox.showinfo(None, message = "The answer to the operation is " + str(answer))
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
