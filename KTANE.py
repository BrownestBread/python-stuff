#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      14sambellsr
#
# Created:     30/04/2018
# Copyright:   (c) 14sambellsr 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#used to play the game keep talking and nobody explodes
x = 0
done = 0

def three(serial, wires):
    x = 0
    done = 0
    
    for i in range(2):
        if wires[i] == '1':
            x = x + 1
    if x == 0:
        if done == 0:
            print('\nCut wire 2\n')
            done = 1
    x = 0

    if wires[2] == '5':
        if done == 0:
            print('\nCut wire 3\n')
            done = 1

    for i in range(2):
        if wires[i] == '2':
            x = x + 1
    if x > 1:
        if done == 0:
            print('\nCut last blue wire\n')
            done = 1
    x = 0

    if done == 0:
        print('\nCut wire 3\n')



def four(serial, wires):
    x = 0
    done = 0

    for i in range(3):
        if wires[i] == '1':
            x = x + 1
    if x > 1:
        if int(serial[-1]) % 2 != 0:
            if done == 0:
                print('\nCut last red wire\n')
                done = 1
    x = 0

    if wires[-1] == '3':
        for i in range(3):
            if wires[i] == '1':
                x = x + 1
        if x == 0:
            if done == 0:
                print('\nCut wire 1\n')
                done = 1
    x = 0

    for i in range(3):
        if wires[i] == '2':
            x = x + 1
    if x == 1:
        if done == 0:
            print('\nCut wire 1\n')
            done = 1
    x = 0


    for i in range(3):
        if wires[i] == '3':
            x = x + 1
    if x > 1:
        if done == 0 :
            print('\nCut wire 4\n')
            done = 1
    x = 0

    if done == 0:
        print('\nCut wire 2\n')



def five(serial, wires):
    x = 0
    done = 0

    if wires[-1] == '4':
        if int(serial[-1]) % 2 != 0:
            if done == 0:
                print('\nCut wire 4\n')
                done = 1
    x = 0

    for i in range(4):
        if wires[i] == '1':
            x = x + 1
    if x == 1:
        x = 0
        for i in range(4):
            if wires[i] == '3':
                x = x + 1
        if x > 1:
            if done == 0:
                print('\nCut wire 1\n')
                done = 1
    x = 0

    for i in range(4):
        if wires[4] == '4':
            x = x + 1
    if x == 0:
        if done == 0:
            print('\nCut wire 2\n')
            done = 1
    x = 0



def six(serial, wires):
    x = 0
    done = 0
    
    for i in range(5):
        if wires[i] == '3':
            x = x + 1
    if x == 0:
        if int(serial[-1]) % 2 != 0:
            if done == 0:
                print('\nCut wire 3\n')
                done = 1
    x = 0

    for i in range(5):
        if wires[i] == '3':
            x = x + 1
    if x == 1:
        x = 0
        for i in range(5):
            if wires[i] == '5':
                x = x + 1
        if x > 1:
            if done == 0:
                print('\nCut wire 1\n')
                done = 1
    x = 0

    for i in range(5):
        if wires[i] == '1':
            x = x + 1
    if x == 0:
        if done == 0:
            print('\nCut wire 6\n')
            done = 1
    x = 0

    if done == 0:
        print('\nCut wire 4\n')
    





serial = input('Enter last digit of Serial Number: ')
    
while True:

    wires = input('\nRed = 1\nBlue = 2\nYellow = 3\nBlack = 4\nWhite = 5\nEnter string: ')

    if len(wires) == 3:
        three(serial, wires)

    if len(wires) == 4:
        four(serial, wires)

    if len(wires) == 5:
        five(serial, wires)

    if len(wires) == 6:
        six(serial, wires)
  

