# TODO
from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

cents = round(change * 100)

number = 0

while cents > 0:
    if cents >= 25:
        cents -= 25
        number += 1
    elif cents >= 10:
        cents -= 10
        number += 1
    elif cents >= 5:
        cents -= 5
        number += 1
    else:
        cents -= 1
        number += 1

print(number)
