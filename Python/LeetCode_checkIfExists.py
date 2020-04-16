def checkIfExist(arr):
    for i in arr:
        if (i == 0):
            if (arr.count(0) > 1):
                return True
        elif (((i*2) in arr) | ((i/2) in arr)):
            return True
    return False

print(checkIfExist([-2,0,10,-19,4,6,-8]))
