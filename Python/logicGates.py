# 간단한 논리 회로 계산기

print('Logic Gates')

def ANDgate(A, B):
  return (A & B)
  
def ORgate(A, B):
  return (A | B)
  
def XORgate(A, B):
  return (A ^ B)

gate = input('Gate? (AND, OR, XOR): ').upper()

if gate == 'AND':
  print('0', gate, '0', '=', ANDgate(0, 0))
  print('0', gate, '1', '=', ANDgate(0, 1))
  print('1', gate, '0', '=', ANDgate(1, 0))
  print('1', gate, '1', '=', ANDgate(1, 1))
elif gate == 'OR':
  print('0', gate, '0', '=', ORgate(0, 0))
  print('0', gate, '1', '=', ORgate(0, 1))
  print('1', gate, '0', '=', ORgate(1, 0))
  print('1', gate, '1', '=', ORgate(1, 1))
elif gate == 'XOR':
  print('0', gate, '0', '=', XORgate(0, 0))
  print('0', gate, '1', '=', XORgate(0, 1))
  print('1', gate, '0', '=', XORgate(1, 0))
  print('1', gate, '1', '=', XORgate(1, 1))