import random
import decimal

while True:
    num = random.randint(10000000000000, 2000000000000000000000000000000000000000000000)
    print (decimal.Decimal(num)/100000)