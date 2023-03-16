# 문자열 갖고 놀기. 쉬운거

print("Strings")
#Learn about String methods in w3schools.

#Enter a sentence.
#  . Convert the sentence to upper case.
#  . Output the total number of characters (with and without spaces) in the sentence.
#  . Output the first character and the last character in the sentence.
#Enter a single character.
#  . Output the number of times the character is found in the sentence.

myString = input("Enter a sentence: ")
myString2 = input("Enter a single character: ")

toUpper = myString.upper()
countL1 = len(myString)
countL2 = len(myString.replace(" ", ""))

print(toUpper)
print(f'With space: {countL1} characters')
print(f'Without space: {countL2} characters')
print(myString[0], myString[-1])
print(f"{myString.count(myString2)} {myString2}'s in '{myString}'")