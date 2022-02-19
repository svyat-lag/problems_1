def kindaBubbleSort(mass):
    for i in range(len(mass)):
        iversonConditionFlag = 0
        for j in range(len(mass) - i - 1):
            if isBigger(mass[j], mass[j + 1]):
                # print(mass)
                # print(mass[j], mass[j+1])
                # print('')
                mass[j], mass[j+1] = mass[j+1], mass[j]
                iversonConditionFlag += 1
        if iversonConditionFlag == 0:
            return mass
    return mass


def isBigger(s1, s2):
    new_s1 = s1 + s2
    new_s2 = s2 + s1
    if new_s1 > new_s2:
        return True
    else:
        return False


def maxNumber(mass):
    mass = kindaBubbleSort(mass)
    # print(mass)
    s = ''
    for i in range(len(mass)-1, -1, -1):
        s += mass[i]
    return s


# new_list = ['10', '100', '20', '200', '102', '9', '13']
# print(new_list)
# print(maxNumber(new_list))
