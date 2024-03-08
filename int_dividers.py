def int_dividers(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)
    return dividers

num = int(input('Введите делимое число: '))
dividers = int_dividers(num)
print('Список положительных делителей для числа {}:'.format(num))
print(dividers)