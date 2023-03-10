"""Вариант 4.
Натуральные простые числа, не превышающие 1 000, у которых средняя цифра равна 4. Минимальное и максимальное число выводятся прописью."""

m = []
chisl = ['0', '1', '2', '3', '4', '5', '6', '7','8','9']
znak = [' ', '!', '?', '.', ',', '\n', '']
buffer_len = 1
work_buffer = ''


def byk(x):
    a = {'0': 'ноль',
         '1': 'один',
         '2': 'два',
         '3': 'три',
         '4': 'четыре',
         '5': 'пять',
         '6': 'шесть',
         '7': 'семь',
         '8': 'восемь',
         '9': 'девять'
         }
    return a[x]


with open('text.txt') as f:
    buffer = f.read(buffer_len)
    if not buffer:
        print('Файл пуст.')
        quit()
    while buffer:
        while buffer not in znak:
            work_buffer += buffer
            buffer = f.read(buffer_len)
        if len(work_buffer) > 0:
            flag = True
            for i in range(len(work_buffer)):
                if work_buffer[i] not in chisl:
                    flag = False
                    break
            if flag and len(work_buffer) > 2:
                def is_prime(work_buffer):
                    if int(work_buffer) < int(2):
                        return False

                    for i in range(2, int(int(work_buffer) ** 0.5) + 1):
                        if int(work_buffer) % i == 0:
                            return False
                    return True
                if work_buffer[0] != '0' and work_buffer[-2] == '4' and int(work_buffer) < int(1000) and is_prime(int(work_buffer)):
                  m += [int(work_buffer)]
        work_buffer = ''
        buffer = f.read(buffer_len)
    if m:
        max_number = max(m)
        k = ''
        for i in range(len(str(max_number))):
            g = byk(str(max_number)[i])
            k += g + ' '
        print(f'Максимальное значение: {k}.')
    else:
        print('В файле нет подходящих значений.')
    if m:
        min_number = min(m)
        k = ''
        for i in range(len(str(min_number))):
            g = byk(str(min_number)[i])
            k += g + ' '
        print(f'Минимальное значение: {k}.')
    else:
        print('В файле нет подходящих значений.')
