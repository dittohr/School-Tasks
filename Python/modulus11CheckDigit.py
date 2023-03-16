# 10자리 수(2진수)를 받고 check digit 뭐시기를 확인해줌. 이게 뭔지 기억이 나지 않는다. 변수명 짓기 참 힘들다

code = input("Enter 9 digits + 1 check digit(Overall 10): ")


def checkDigit(strCode):
  n = len(strCode)

  sum = 0
  
  for i in range(n - 1):
    sum += (n - i) * int(strCode[i])

  check_digit = (11 - sum % 11) % 11

  
  givinCheckDigit = int(strCode[-1])

  if check_digit == givinCheckDigit:
    return "Vaild Check Digit"
  else:
    return "Invalid Check Digit"

print("Check digit = ", checkDigit(code))