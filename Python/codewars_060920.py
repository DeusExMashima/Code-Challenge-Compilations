def digital_root(n):
    num_string = str(n)
    
    while len(num_string) > 1:
        last_sum = 0
        for i in num_string:
            last_sum += int(i)
        num_string = str(last_sum)
    return int(num_string)

print(digital_root(16))
print(digital_root(942))
# print(digital_root(132189))
