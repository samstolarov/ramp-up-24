def loopyloop(num):
    fac = 1
    for i in range(1, num + 1):
        fac = fac * i
    return fac
def recursion(num):
    if(num == 1):
        return 1
    else:
        return num * recursion(num - 1)

