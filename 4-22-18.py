def add(x,y):
    sum = x + y
    return sum


def minus(l,w):
    subtract = l - w
    return subtract
import time

def multiply(t,y):
    times =  t * y
    return times


def divide(q,k):
    slash = q/k
    return slash



print('Select operation.')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

choice = input('Enter choice(1,2,3,4):')
if (int(choice) < 1 or int(choice) > 4):
    print('TRASH!!!')
    time.sleep(1)
    print('Pure Buns!!!')
    time.sleep(1)
    print('GO HOME!!!')
    exit(9)


num1 = int(input('Enter a first number:'))
num2 = int(input('Enter a second number:'))

if(choice == '1'):
    print(num1, '+', num2, '=', add(num1, num2))

elif(choice =='2'):
    print(num1, '-', num2, '=', minus(num1, num2))

elif(choice =='3'):
    print(num1, '*', num2, '=', multiply(num1, num2))


elif(choice =='4'):
    print(num1, '/', num2, '=', divide(num1, num2))

else:
    print('Invalid operation!!!!')



































