function = int(input("Would you like to\n1) Double a number\n2) Half a number\n3) Quit\n"))
while function != 3:
    number = input("Which number would you like to operate on?\n")
    if function == 1:
        print(2 * int(number))
    elif function == 2:
        print(0.5 * int(number))
    function = int(input("Would you like to\n1) Double a number\n2) Half a number\n3) Quit\n"))
print("Goodbye")
