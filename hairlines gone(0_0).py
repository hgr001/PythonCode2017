import mymodules

def doomsday(timeleft):
    while timeleft > 0:
        if(timeleft > 3):
            print('%d seconds left UNTIL BLACK PEOPLE LOSE THEIR HAIRLINE'% timeleft)
        elif(timeleft == 3):
            print('SOON')
        else:
            print('ONLY %d SECONDS LEFT!' % timeleft)

        mymodules.wait(timeleft)
        timeleft = timeleft - 1



    mymodules.kill()




doomsday(6)