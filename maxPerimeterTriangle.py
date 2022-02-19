def quickSort(mass):
    if len(mass) <= 1:
        return mass

    pivot = mass[0]
    less = [i for i in mass if i < pivot]
    equal = [i for i in mass if i == pivot]
    more = [i for i in mass if i > pivot]

    return quickSort(less) + equal + quickSort(more)


def maxPerimeterTriangle(mass):
    mass = quickSort(mass)
    while len(mass) > 2:
        # Записываю два наибольших числа и ищу им третью сторону
        a = mass[-1]
        b = mass[-2]
        for j in range(len(mass)-3, -1, -1):
            if (a + b > mass[j]) and (a + mass[j] > b) and (b + mass[j] > a):
                return a + b + mass[j]
        # Если сторону не нашел, то удаляю максимальный элемент и ищу в оставлемся списке
        del mass[-1]
    return 0