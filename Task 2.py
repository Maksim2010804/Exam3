str_1 = input('Введите строку: ')

def palindrome(data):
    data = data.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'

print(palindrome(str_1))