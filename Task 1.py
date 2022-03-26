numb_karta = input('Введите номер кредитной карты: ')

def karta(a):
    return '*' * len(a[:-4]) + a[-4:]

print(karta(numb_karta))

