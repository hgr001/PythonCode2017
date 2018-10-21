import random
import time


# Print out intro text
def displayInfo():
    print()
    print('You are in Horror City.  In front of you, you see a girl bleeding.')
    time.sleep(3.5)
    print('After running away from the insane Asylum and escaping the guards.')
    time.sleep(3.5)
    print('You run to her without hesitation because, you are desperate for someone \nto talk to.')
    time.sleep(3.5)
    print('While you are bandaging her up from the badages you stole from the insane \nAsylum.')
    time.sleep(3.5)
    print('You remember someone that looks just like her.')
    print()


# Choose what  to tell her
def chooseOption():
    print('Do you tell here you just escaped from the Insane Asylum?')
    print('Yes - 1\nNo - 2')
    option = int(input())
    return option


# Check if good or bad to say
def optionOne():
    print('She leans in closer...')
    time.sleep(3)
    print('You feel that something bad is going to happen...')
    time.sleep(2.5)
    print('She gets closer')
    time.sleep(2)
    print('Your heart starts to best faster and faster by the second')
    time.sleep(1.5)
    print('She gets closer, she leans in...')
    time.sleep(1)
    print('You figure out this is a setup')
    time.sleep(2)
    print('You see her reaching for your knife you had')
    time.sleep(3)
    print('She grabs the knife and swings and she stabs you in the head')
    time.sleep(5)
    print('THE END!!!')
    time.sleep(2)
    print('PS: You died')


def optionTwo():
    print('')


# Ask to read again
def runGame():
    displayInfo()
    choice = chooseOption()

    if choice == 1:
        optionOne()
    elif choice == 2:
        optionTwo()


runGame()
