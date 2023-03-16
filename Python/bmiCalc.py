# BMI 수치 검사

print("Body Mass Index (BMI)")
name=input("Enter your name: ")

mass = float(input('Enter your mass: '))
height = float(input('Enter your height: ')) / 100
bmi = round(float(mass / (height * height)), 2)

print(name + ', your bmi is ', str(bmi))

if bmi > 25:
  print('you are overweight')
elif bmi < 18.5:
  print('you are underweight')
else:
  print('you are ok')