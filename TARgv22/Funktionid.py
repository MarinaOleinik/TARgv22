from math import *
from random import choice

import string
logins = []
passwords = []

def register(username, password=None):
    """
    Регистрация нового пользователя.Если не вводит пароль-то программа сделает за него свой.
    """
    if password is None:       
        str0 = ".,:;!_*-+()/#¤%&"
        str1 = "0123456789"
        str2 = "abcdefghijklmnopqrstuvwxyz"
        str3 = str2.upper()
        passwd = "".join(random.sample(str0+str1+str2+str3, 8))
    else:
        passwd = password
        
    logins.append(username)
    passwords.append(passwd)
    print(f"Регистрация прошла успешно. Ваш пароль {passwd}")

def login(username, password):
    """
    Проверяет, соответствует ли пароль к пользователю.
    """
    if username in logins:
        index = logins.index(username)
        if passwords[index] == password:
            print("Вход успешен.")
            return True
    print("Неправильный пароль или имя пользователя.")
    return False
def salasona(k: int):
    sala=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        sala+=choice(t_num)
    return sala



def arithmetic(a1:float,sym:str,a2:float)->any:
    """Lihtne kalkulaator
    +  liitmine, - lahutamine, * korrutamine,/ jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :rtype: var Määramata tüüp
    """
    if sym in ["+","-","/","*"]:
        if sym=="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+sym+str(a2))
    else:
        vas="Tundmatu tehe!"
    return vas
def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab True kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype: bool, str Funktsioni vastus loogilises formaadis
    """
    aasta=int(aasta)
    if aasta%4==0:
        t=True
    else:
        t=False
    return t
def square(a: float):
    """
    """
    try:
        a=float(a)
        if a>0:
            P=4*a
            S=a**2
            d=a*sqrt(2)
            return P,S,d
        else:
            v="---"
            return v

    except:
        v="---"
        return v
    