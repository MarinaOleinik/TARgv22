from operator import xor
from Funktionid import *



while True:
    choice = input("Выберите опцию: 1. Регистрация, 2. Вход, 3. Выход\n")

    if choice == '1':
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        register(username, password)
    elif choice == '2':
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if login(username, password):
            break
    elif choice == '3':
        break
    else:
        print("Неправильный выбор.")
sala=salasona(10)
print(sala)


#3
for i in range(3):
    P,S,d=square(input())
    print(f"Läbimõõt: {P}")
    print(f"Pindala: {S}")
    print(f"Diagonaal: {d}")

#2
print(is_year_leap(input()))

#1
answer=arithmetic(2.5,"+",1.8)
print(answer)
answer=arithmetic(input(),input(),input())
print(answer)
