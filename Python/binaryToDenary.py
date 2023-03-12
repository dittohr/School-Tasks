print("Binary to Denary converter")

binary = ""

while len(binary) != 8:
  binary = input("Enter 8-bit binary number: ")

denary = 0
power = 7

for bit in binary:
  denary = denary + int(bit) * pow(2, power)
  power -= 1

print(f'Binary to Denary = {denary}')