# 랜덤 함수랑 리스트 사용해보라고 낸건 알겠는데 진짜 의미 없어요 선생님

import random

myList = ['Minji', 'Haerin', 'Danielle', 'Hanni', 'Hyein', 'Chaewon', 'Yunjin', 'Eunchae', 'Sakura', 'Kazuha']

while True:
  randomName = random.choice(myList)
  print(randomName)

  choice = input('Press N to stop. ')
  if choice == 'n' or choice == 'N':
    break