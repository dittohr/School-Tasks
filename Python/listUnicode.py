print('Character codes')

#출력할 개수 입력
maxCode = int(input('Enter max code: '))

#1부터 maxCode 값만큼의 유니코드 출력
for i in range(maxCode):
    print('Code:', i + 1, 'Unicode:', chr(i + 1))