def desc_number(num):
    digit_list = sorted(str(num), reverse=True)
    desc_number = int("".join(digit_list))
    return desc_number


print(desc_number(31572))
