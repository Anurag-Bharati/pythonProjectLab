# Program to calculate various parameter of different shapes
# Currently it can calculate Area and Perimeter of Circle, Rectangle, Square, Triangle

import keyboard
import time
import math

# CONSTANTS----------------------------
Pi = math.pi
intensity = 1
"""log = math.log(intensity / 10 ** (-12))"""
# CONSTANTS----------------------------


def tt(text, delay):
    for i in text:
        print(end=i)
        time.sleep(delay)
    print()


tt("\n\t pCalculator V1.0 - Console", 0.02)
tt("\n\t\t\t  Hello!", 0.02)

tt("\nWhat shapes do you want to calculate?", 0.02)
tt("-------------------------------------", 0.02)
tt("\nPress key 'c' to select Circle\nPress key 'r' to select Rectangle\nPress key 's' to select Square"
   "\nPress key 't' to select Triangle\nPress key 'i' to select Intensity of Sound\nPress 'e' to exit\n\n", 0.008)


while True:
    #                         -------------Algorithm for Circle-------------

    if keyboard.is_pressed("c"):
        time.sleep(.1)
        print("\nCircle")
        tt("------", 0.01)
        print("\nPress 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
        time.sleep(.5)
        while True:
            if keyboard.is_pressed("p"):
                time.sleep(.1)
                r = input("\nEnter the value of radius of a circle: ")
                r = float(r)
                print("\nThe perimeter of circle is: ", 2*Pi*r)
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
            elif keyboard.is_pressed("a"):
                time.sleep(.1)
                r = input("\nEnter the value of radius of a circle: ")
                r = float(r)
                print("\nThe Area of circle is: ", Pi*r**2)
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
            elif keyboard.is_pressed("b"):
                time.sleep(.5)
                print("\n\n\nNow returning back")
                time.sleep(.5)
                tt("..................", 0.01)
                tt("\nPress key 'c' to select Circle\nPress key 'r' to select Rectangle\nPress key 's' to select Square"
                   "\nPress key 't' to select Triangle\nPress key 'i' to select Intensity of Sound"
                   "\nPress 'e' to exit\n\n", 0.008)
                break

    #                         -------------Algorithm for Rectangle------------
    elif keyboard.is_pressed("r"):
        time.sleep(.1)
        print("\nRectangle")
        tt("---------", 0.01)
        print("\nPress 'p' to calculate the perimeter or 'a' to calculate the area.")
        time.sleep(.5)
        while True:
            if keyboard.is_pressed("p"):
                time.sleep(.1)
                length = input("\ntEnter the value of length of a rectangle: ")
                breath = input("Enter the value of breath of a rectangle: ")
                length, breath = float(length), float(breath)
                print("\nThe perimeter of rectangle is: ", 2*(length+breath))
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
                break
            elif keyboard.is_pressed("a"):
                time.sleep(.1)
                length = input("\nEnter the value of breath of a rectangle: ")
                breath = input("Enter the value of breath of a rectangle: ")
                length, breath = float(length), float(breath)
                print("\nThe Area of rectangle is: ", length*breath)
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
                break
            elif keyboard.is_pressed("b"):
                time.sleep(.5)
                print("\n\n\nNow returning back")
                time.sleep(.5)
                tt("..................", 0.01)
                tt("\nPress key 'c' to select Circle\nPress key 'r' to select Rectangle\nPress key 's' to select Square"
                   "\nPress key 't' to select Triangle\nPress key 'i' to select Intensity of Sound"
                   "\nPress 'e' to exit\n\n", 0.008)
                break

    #                         -------------Algorithm for Square------------
    elif keyboard.is_pressed("s"):
        time.sleep(.1)
        print("\nSquare")
        tt("------", 0.01)
        print("\nPress 'p' to calculate the perimeter or 'a' to calculate the area.")
        time.sleep(.5)
        while True:
            if keyboard.is_pressed("p"):
                time.sleep(.1)
                length = input("\nEnter the value of length of a square: ")
                length = float(length)
                print("\nThe perimeter of square is: ", 4*length)
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
            elif keyboard.is_pressed("a"):
                time.sleep(.1)
                length = input("\nEnter the value of length of a square: ")
                length = float(length)
                print("\nThe Area of square is: ", length**2)
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
            elif keyboard.is_pressed("b"):
                time.sleep(.5)
                print("\n\n\nNow returning back")
                time.sleep(.5)
                tt("..................", 0.01)
                tt("\nPress key 'c' to select Circle\nPress key 'r' to select Rectangle\nPress key 's' to select Square"
                   "\nPress key 't' to select Triangle\nPress key 'i' to select Intensity of Sound"
                   "\nPress 'e' to exit\n\n", 0.008)
                break

    #                         -------------Algorithm for Triangle------------
    elif keyboard.is_pressed("t"):
        time.sleep(.1)
        print("\nTriangle")
        tt("--------", 0.01)
        print("\nPress 'p' to calculate the perimeter or 'a' to calculate the area.")
        time.sleep(.5)
        while True:
            if keyboard.is_pressed("p"):
                time.sleep(.1)
                sideA = input("\nEnter the value of Side 'A' of a Triangle: ")
                sideB = input("Enter the value of Side 'B' of a Triangle: ")
                sideC = input("Enter the value of Side 'C' of a Triangle: ")
                sideA, sideB, sideC = float(sideA), float(sideB), float(sideC)
                print("\nThe perimeter of rectangle is: ", sideA+sideB+sideC)
                time.sleep(1)
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
            elif keyboard.is_pressed("a"):
                time.sleep(.1)
                base = input("\nEnter the value of Base of a Triangle: ")
                height = input("Enter the value of Height of a Triangle: ")
                base, height, = float(base), float(height)
                print("\nThe Area of square is: ", 0.5*base*height)
                print("\n\nYou can now continue on!")
                print("Press Press 'p' to calculate the perimeter, 'a' to calculate the area or 'b' to return back.")
            elif keyboard.is_pressed("b"):
                time.sleep(.5)
                print("\n\n\nNow returning back")
                time.sleep(.5)
                tt("..................", 0.01)
                tt("\nPress key 'c' to select Circle\nPress key 'r' to select Rectangle\nPress key 's' to select Square"
                   "\nPress key 't' to select Triangle\nPress key 'i' to select Intensity of Sound\n"
                   "Press 'e' to exit\n\n", 0.008)
                break

    #                         -------------Algorithm for Intensity------------
    elif keyboard.is_pressed("i"):
        time.sleep(.1)
        print("\nIntensity of Sound (in dB)")
        tt("--------------------------", 0.01)
        print("\nPress 'i' to calculate the or 'b' to return back.")
        time.sleep(.5)
        while True:
            if keyboard.is_pressed("i"):
                time.sleep(.1)
                intensity = input("\nEnter the Intensity of the sound: ")
                intensity = float(intensity)
                if intensity <= 0:
                    print("Please a Valid No.")
                    print("\nPress 'i' to calculate the or 'b' to return back.")
                else:
                    print("\nThe Intensity of the sound is: ", 10 * math.log(intensity / (10 ** (-12))))
                    print("Press 'i' to calculate the or 'b' to return back.")

            elif keyboard.is_pressed("b"):
                time.sleep(.1)
                print("\n\n\nNow returning back")
                time.sleep(.5)
                tt("..................", 0.01)
                tt("\nPress key 'c' to select Circle\nPress key 'r' to select Rectangle\nPress key 's' to select Square"
                   "\nPress key 't' to select Triangle\nPress key 'i' to select Intensity of Sound\nPress 'e' to exit"
                   "\n\n", 0.008)
                break
        break

    elif keyboard.is_pressed("e"):
        time.sleep(.5)
        print("\n\n\nNow Exiting")
        time.sleep(.5)
        tt("..................", 0.01)
        keyboard.send("ctrl+F2")

