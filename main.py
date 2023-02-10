x = open('test.txt')
a = list(map(int, x.readline()))

m = []


def convert_number_to_words(number):
    digit_words = {
        '0': 'ноль',
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
    number_in_words = ""
    for digit in str(number):
        number_in_words += digit_words[digit] + " "
    return number_in_words


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for i in range(len(a)-2):
    s = str(a[i]) + str(a[i+1]) + str(a[i+2])
    if int(s) <= 1000 and s[-2] == '4' and is_prime(int(s)):
        m += [int(s)]

print(m)
print(f'Максимальное число: {convert_number_to_words(max(m))}')
print(f'Минимальное число: {convert_number_to_words(min(m))}')