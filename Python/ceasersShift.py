# 유니코드를 이용한 간단한 암호화 코드

print("Ceasar's shift")
print("--------------")
plainText = input("Enter plain text: ")
key = int(input("Enter shift key: "))

def encrypt(txtPlain, shiftKey):
  
  asdf = ""

  for character in txtPlain:
    enCharacter = ord(character)
    enShiftKey = int(shiftKey)
    asdf = asdf + chr(enCharacter + enShiftKey)

  return asdf

def decrypt(txtCipher, shiftKey):

  asdf = ""

  for character in txtCipher:
    deCharacter = ord(character)
    deShiftKey = int(shiftKey)
    asdf = asdf + chr(deCharacter - deShiftKey)

  return asdf

cipherText = encrypt(plainText, key)
print("Cipher text is: ", cipherText)
print("Plain text was: ", decrypt(cipherText, key))
print("Shift Key =", key)