"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""


from uuid import uuid4
import hashlib


salt = uuid4().hex


def get_hash(passwd):
    return hashlib.sha256(passwd.encode('utf-8') + salt.encode('utf-8')).hexdigest()


passwd_hash_stored = get_hash(input('Введите строку пароля: '))
print(f'Хеш вашего пароля: {[passwd_hash_stored]}')
passwd_check = get_hash(input('Введите строку пароля для доступа: '))

if passwd_hash_stored == passwd_check:
    print('Доступ предоставлен')
else:
    print('Пароль неверный!')
