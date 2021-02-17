# Program to convert Binary to Decimal or vice versa


import keyboard


print("\nPress 'b' to convert decimal number into binary, 'd' to convert binary to decimal or 'e' to exit.\n")
while True:
    if keyboard.is_pressed("b"):
        keyboard.send("backspace")
        print("\nDecimal to binary\n")
        keyboard.send("backspace")
        a = (input("Enter decimal no: "))
        b = bin(int(a))
        print("\n", a, "in binary is ", b[2:])
        print("\nPress 'b' to convert decimal number into binary, 'd' to convert binary to decimal or 'e' to exit.\n")

    elif keyboard.is_pressed("d"):
        keyboard.send("backspace")
        print("\nBinary to Decimal\n")
        keyboard.send("backspace")
        a = input("Enter binary no: ")

        still_testing = True

        while still_testing:
            if len(a):
                still_testing = False
                for (num) in a:
                    if int(num) not in [0, 1]:
                        print("Invalid input for", num)
                        a = input()
                        still_testing = True

        while not still_testing:
            print(f"\n {a} in decimal is ", int(a, 2))
            print("\nPress 'b' to convert decimal number into binary, 'd' to convert binary to decimal or 'e' to exit."
                  " \n")
            still_testing = True
    elif keyboard.is_pressed("e"):
        print("\n\nNow Exiting...")
        keyboard.send("ctrl+F2")
        break
