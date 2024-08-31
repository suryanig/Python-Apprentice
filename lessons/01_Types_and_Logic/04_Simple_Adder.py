"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


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
# Display the sum of the two numbers 
sum = num1 + num2
messagebox.showinfo(None, message="The sum of the two number is " + str(sum))
# Keep the window open

