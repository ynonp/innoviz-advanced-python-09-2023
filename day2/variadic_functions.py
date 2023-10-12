def sum_squares(*list_of_numbers: int):
    return sum(x * x for x in list_of_numbers)


print(sum_squares(1, 2, 3))

values = [1, 2, 3]
print(sum_squares(*values))
