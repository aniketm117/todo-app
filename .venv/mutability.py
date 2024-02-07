#type of errors

def per_cent():
    try:
        total_value = float(input("Enter total value: "))
        value = float(input("Enter value: "))

        per_cent = (value / total_value) * 100

        print("That is " + str(per_cent) + " %")
        return

    except TypeError:

        print("You need to enter a number. Run the program again")
        return

    except ZeroDivisionError:

        print("Your total value cannot be zero")
        return

"""
import glob

myFiles = glob.glob('Files/*.txt')

print(myFiles)"""

import webbrowser

webbrowser.open("https://duckduckgo.com/?q=cats")

