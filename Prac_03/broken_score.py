"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def Main():
    global score
    score = float(input("Enter score: "))


Main()


def Determine():
    if score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    elif score > 0:
        print("Bad")
    else:
        print("Invalid score")


Determine()


