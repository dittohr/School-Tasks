#버블 정렬 알고리즘

print("Bubble Sort")

print("-----------")
myList = ["Pear","Apple","Banana","Orange","Lemon"]
print("Unsorted list:")
for x in myList:
  print(x)
print("-----------")

def bubbleSortAscending(items):
  n = len(items)
  swapped = True

  while (n > 0) and (swapped):
    swapped = False
    n = n - 1

    for index in range(0, n):
      if items[index] > items[index + 1]:
        temp = items[index]
        items[index] = items[index + 1]
        items[index + 1] = temp
        swapped = True
  
  return items

bubbleSortAscending(myList)

print("Sorted list (A-Z):")

for x in myList:
  print(x)