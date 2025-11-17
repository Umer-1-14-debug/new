value_to_check = 1
count = 0
for v in my_dict.values():
    if v == value_to_check:
        count += 1
print("Frequency:", count)
