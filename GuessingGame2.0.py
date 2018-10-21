# Guessing Game2.0
import random

print('Hello what is your name?')
name = input()

number = random.randint(1, 20)

print('Well, ' + name + ' I am thinking of a number between 1 and 20')

tries = 4
guessesTaken = 1
while tries > 0:


    print('Take a guess.')
    guess = int(input())

    if guess < number:
        print('That was too low, try again')



    if guess > number:
        print('That was to high, try again')



    if guess == number:
            break



    guessesTaken = guessesTaken + 1
    tries = tries -1
    print('You have ' + str(tries)+ ' gueeses left.')



if guess == number:
    print('Good Job ' + name + 'it took you ' + str(guessesTaken) + ' tries!!')



else:
    number = str(number)
    print('Nice try but you suck bye bye L.O.L')
    print('The number I was thinking of was ' + number)
