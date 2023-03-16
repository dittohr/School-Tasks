# 뀨

print ("Word Counter")

def wordcount(myString):
  counter = 0
  for char in myString:
    if char == " " or char == "." or char == "!" or char == "?":
      counter = counter + 1
  return counter + 1

sentence = input("Enter sentence: ")

print(wordcount(sentence), 'words')