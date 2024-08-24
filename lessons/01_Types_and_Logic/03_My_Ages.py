
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

# Ask the user's age
age = simpledialog.askinteger("Your age", 'How old are you?')
# Use if statements to determine the age group
# and create a message
if age ==14:
    print("You are pretty awesome?")
elif age >= 0 and age <=2:
    group = "baby"
elif age >= 3 and age <=5:
    group = "toddler"
elif age >=6 and age <= 12:
    group = "child"
elif age >=13 and age <= 19:
    group = "teen"
elif age >=20 and age <=64:
    group = "adult"
else:
    group = "senior"
# Show the message to the user
messagebox.showinfo(None, message="You are a "+group)


window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
