# 바이너리 값이 약수/홀수 유무를 판단해줌

print("Parity check")
print("------------")
binary = input("Enter 8-bit binary number: ")
count = 0

for i in binary:
  count = count + int(i)

mod = count % 2

if mod == 0:
  print('Even')
else:
  print('Odd')