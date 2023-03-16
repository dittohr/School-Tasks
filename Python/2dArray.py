# 왜 만들라 한건지 모르겠는데

import random

print("2D array")
row = 10
column = 5

arrays = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
]

def alphabets():
    randomLetter = random.choice('가나다라마바사아자차카타파하')
    # Korean alphabet
    return randomLetter

for i in range(row):
    for j in range(column):
        arrays[i][j] = alphabets()

for i in range(row):
    for j in range(column):
        print(arrays[i][j], '  ', end = '')
print()