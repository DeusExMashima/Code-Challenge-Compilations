def reverse(num):
    #convert number to string
    #check the length of the number
    # [_, _, _, | _, _, _]
    #switching first with last, and onwards
    #find the half point which will be the stopping point
    
    #if the length of it is odd
        # the half point would be 2.5 > 3 floor + 1
        # that is when the loop stop
    
    #loop over each number and switch

    #convert back to the number


    string_num = str(num)
    string_num = [num_char for num_char in string_num]
    is_negative = None
    midpoint = None
    if '-' in string_num:
        is_negative = '-'
        string_num = string_num[1:]
    midpoint = len(string_num) // 2
    
    for each_num in range(midpoint):
        if each_num != midpoint:
            string_num[each_num], string_num[-(1+each_num)] = string_num[-(1+each_num)], string_num[each_num]
            #this should work in case of the length is an even number

    if is_negative is not None:
        string_num = ['-'] + string_num
    fin_num = ''.join(string_num)
    fin_num = int(fin_num)
    limit = 2 ** 31
    if fin_num < (limit-1) and fin_num > limit * (-1):
        return fin_num
    else:
        return 0

print(reverse(10))
print(reverse(123))
print(reverse(-1534236469))




