import time
from random import randint

#FUNCTIONS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def display_card(card):
    print('\n\nYour current card is called', card[0])
    time.sleep(0.08)
    print('\nIt\'s exercise value is', card[1] , '/5')
    time.sleep(0.08)
    print('It\'s intellgience value is', card[2], '/100')
    time.sleep(0.08)
    print('It\'s friendliness value is', card[3], '/10')
    time.sleep(0.08)
    print('It\'s drool value is', card[4], '/10')
    time.sleep(0.08)
def choose_size():
    
    size = int(input('How many cards would you like to play with?\nThe number must be even and between 4 and 30\n'))
    while size % 2 == 1 or (( size < 4) or (size > 30)):
        size = int(input('Sorry, that doesn\'t seem right.\nHow many cards would you like to play with?\nThe number must be even and between 4 and 30\n'))

    return(size)

def choose_trait():
    
    trait = int(input('\n\nWhich trait would you like to play?\nType 1-4:\n'))
    while (trait < 1) or (trait > 4):
        trait = int(input('Sorry, that doesn\'t seem right.\nWhich trait would you like to play?\nRemember the number must be between 1 and 4\n'))

    return(trait)

def deal(size):
    
    file = open('dogs.txt', 'r')
    deck = []
    for i in file:
        deck.append(i[:-1])
        
    hand1 = []
    hand2 = []
    for i in range(size):
        card = randint(0, len(deck)-1)
        if i % 2 == 0:
            hand1.append(deck[card])
        else:
            hand2.append(deck[card])
        deck.pop(card)
        
    return(hand1, hand2)

def assign(hand):
    for i in range(len(hand)):
        hand[i] = [hand[i], randint(1, 5), randint(1, 100), randint(1, 10), randint(1, 10)]

def compare(trait):
    print('\n\nYou were playing against', hands[1][0], '\n')
    input('\nPress ENTER to continue')
    time.sleep(0.1)
    if trait < 4:
        if hands[0][0][trait] >= hands[1][0][trait]:
            print('\nYou won and gained', hands[1][0][0])
            hands[0].append(hands[1].pop(0))
            hands[0].append(hands[0].pop(0))
        else:
            print('\nYou lost and and gave away', hands[0][0][0]) 
            hands[1].append(hands[1].pop(0))
            hands[1].append(hands[0].pop(0))
    else:
        if hands[0][0][trait] <= hands[1][0][trait]:
            print('\nYou won and gained', hands[1][0][0])
            hands[0].append(hands[1].pop(0))
            hands[0].append(hands[0].pop(0))
        else:
            print('\nYou lost and and gave away', hands[0][0][0]) 
            hands[1].append(hands[1].pop(0))
            hands[1].append(hands[0].pop(0))
    print('\nYou now have', len(hands[0]), 'cards and your opponent has', len(hands[1]), 'cards')
    input('Press ENTER to continue')

#MAIN CODE------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

menu = input('1. Play Game\n2. Quit\n')
if (menu  != '1') and (menu != '2'):
    print('Invalid Reponse: Enter \'1\' or \'2\'')
    menu = input('1. Play Game\n2. Exit\n')

while menu == '1':

    print('--------------------------------------------\n|                                          |\n|     Welcome to Illegal Dog Fighting!     |\n|                                          |\n--------------------------------------------\n')
    time.sleep(1)
    input('\nPress ENTER to continue\n')
    hands = deal(choose_size())
    assign(hands[0])
    assign(hands[1])
    
    while (len(hands[0]) > 0) and (len(hands[1]) > 0):
        display_card((hands[0])[0])
        compare(choose_trait())
        
    if len(hands[0]) == 0:
        print('\nYou lost \ncause your bad\n\n')
    else:
        print('\nCongrats - you won!\n\n')

    menu = input('1. Play Game\n2. Quit\n')
    while (menu != '1') and (menu != '2'):
        print('Invalid Reponse: Press \'1\' or \'2\'')
        menu = input('1. Play Game\n2. Exit\n')
        
    time.sleep(1)


print( 'Goodbye!')
time.sleep(1)
