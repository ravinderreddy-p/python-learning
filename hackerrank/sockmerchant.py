input_list = [10, 20, 10, 10, 20, 30, 50, 10]
counter = 0
length_of_input_list = len(input_list)
index = 0
while index < length_of_input_list:
    sub_list = input_list[index+1 : length_of_input_list]
    if input_list[index] in sub_list:
        same_color_count = sub_list.count(input_list[index])
        pair_count = int((same_color_count+1)/2)
        counter += pair_count
        index += 1
print(counter)