import maxPerimeterTriangle
import maxNumber
import diagonalsSoringInMatrix


if __name__ == '__main__':
    list_of_tasks = {
        '1': 'Треугольник с максимальным периметром',
        '2': 'Максимальное число',
        '3': 'Сортировка диагоналей в матрице'
    }
    for key, val in list_of_tasks.items():
        print(key, val)
    task_number = int(input('Введите номер задачи: '))


    if task_number == 1:
        # Формируем список из введенной строки
        s = input()
        some_list = s.split()
        some_list = [int(number) for number in some_list]

        print(maxPerimeterTriangle.maxPerimeterTriangle(some_list))
    elif task_number == 2:
        # Формируем список из введенной строки
        s = input()
        some_list = s.split()
        some_list = [number for number in some_list]

        print(maxNumber.maxNumber(some_list))
    elif task_number == 3:
        # Ввод параметров матрицы
        m = int(input('Количество строк: '))
        n = int(input('Количество столбцов: '))

        a = diagonalsSoringInMatrix.matrixGenerator(m, n)
        diagonalsSoringInMatrix.diagonalSort(a, m, n)

        print('')
        for i in range(m):
            print(a[i])
    else:
        print("Кажется, задачи с таким номеров не существует")