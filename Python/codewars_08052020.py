#https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(array):
    new_array = []
    count = 0
    for number in array:
        if number != 0 or isinstance(number, bool):
            new_array.append(number)
            count += 1
    return new_array +  ([0] * (len(array) - count))

print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print(move_zeros([0,1,None,2,False,1,0]))

#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
print('## maximum SubArray Sum ##')

def max_sequence(arr):
    max_sum = 0
    max_array = []
    for ind, num in enumerate(arr):
        sub_arr = arr[ind: ]
        while sub_arr:
            if sum(sub_arr) > max_sum:
                max_sum = sum(sub_arr)
                max_array = sub_arr
            sub_arr = sub_arr[:-1]
    return max_sum
            
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print('')

#https://www.codewars.com/kata/526989a41034285187000de4/train/python

print('## IP Between ##')
import socket,struct
def ips_between(start, end):
    ipstart = struct.unpack("!L", socket.inet_aton(start))[0]
    ipend = struct.unpack("!L", socket.inet_aton(end))[0]
    if ipstart > ipend:
        return ipstart - ipend
    else:
        return ipend - ipstart

print(ips_between("20.0.0.10", "20.0.1.0"))
