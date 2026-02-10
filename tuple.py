# dont change when created


my_tuple = (1, 2, 4, 5)

print(my_tuple[1])

try:
    my_tuple[0] = 1
except Exception as e:
    print(e)
