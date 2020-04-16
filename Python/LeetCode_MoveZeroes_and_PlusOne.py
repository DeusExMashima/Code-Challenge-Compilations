def moveZeroes(arr):
    zeroes = [zero for zero in arr if zero == 0]
    for i in zeroes:
        arr.remove(0)
    return arr + zeroes

print(moveZeroes([1,2,3,4,0,0,0]))

def plusOne(digits):
    num = ''.join([str(digit) for digit in digits])
    num = int(num) + 1
    new = []
    for i in str(num):
        new.append(int(i))
    return new

print(plusOne([1,2,3,4,5]))
print(plusOne([1,2,3,4,9]))
