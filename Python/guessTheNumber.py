# 말 그대로 숫자를 맞히는 게임

import random

print('Guess the Number')
print()

max = int(input('Enter maximum number: '))

random.seed()

randomNumber = random.randrange(1, max)

guesses = 0
guessNumber = 0

while (guessNumber != randomNumber):
    guessNumber = int(input('Guess number: '))
    if guessNumber == randomNumber:
        print('Correct (～￣▽￣)～')
    elif guessNumber > randomNumber:
        print('Smaller!')
    else:
        print('Larger!')