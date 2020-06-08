array_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(len(array_list))
print(array_list[-2])
list_lenth = len(array_list)

if list_lenth % 2 == 0:
    print((list_lenth/2) * (array_list[-1] + 1))

else:
    print((list_lenth / 2) * (array_list[-2] + 1) + array_list[-1])
