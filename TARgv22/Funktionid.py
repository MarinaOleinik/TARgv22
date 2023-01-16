from math import *
from random import choice
from re import T

import string

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
    