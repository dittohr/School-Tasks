# IGCSE Computer Science 시험의 결과에 따라 등급을 계산해준다

print('Grades Calculator')

def grade(intScore):
    if intScore >= 85:
        grade = 'A*'
    elif intScore >= 75:
        grade = 'A'
    elif intScore >= 65:
        grade = 'B'
    elif intScore >= 55:
        grade = 'C'
    elif intScore >= 45:
        grade = 'D'
    elif intScore >= 35:
        grade = 'E'
    else:
        grade = 'U'
    return grade

scoreCount = 1
score = ''

while score != 'S':
    score = input('Enter Score ' + str(scoreCount) + ' (/100) or S to stop: ')

    if score != 'S':
        print('Grade', str(scoreCount), '=', grade(int(score)))
        scoreCount += 1