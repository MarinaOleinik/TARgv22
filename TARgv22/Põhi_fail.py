from operator import xor
from Funktionid import *
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
