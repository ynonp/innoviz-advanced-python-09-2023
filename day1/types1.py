items = [{'a': 10, 'b': 20, '_id': 1},
         {'a': 12, 'b': 31, '_id': 2}]

def print_item(items, index):
   i = items[index]
   del(i['_id'])
   print(i)


print(items)
print_item(items, 0)
print_item(items, 1)
print(items)


num: int = 920
sum_of_digits = 0
while num > 0:
    sum_of_digits += (num % 10)
    num = num // 10

print(sum_of_digits)