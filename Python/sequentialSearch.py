# 선형 알고리즘

print('Sequential Search')

target = input('Please enter a fruit to find: ')

items = ['Pear', 'Apple', 'Banana', 'Orange', 'Lemon']

def sequentialSearch(items, item_to_find):
  index = 0
  found = False
  n = len(items)
  
  while (found == False) and (index < n):
    if items[index] == item_to_find:
      found = True
    else:
      index = index + 1

  if found == True:
    return (f'Item found at index {index}')
  else:
    return ('Item not found')


print(sequentialSearch(items, target))
