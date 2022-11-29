from math import *
#Korduslaused
j=0
for i in range(0,15,1): # for i in range(15):
    A=float(input(f"{i+1} Sisesta A  : ")) #A=5.0 int(A)==A =True
    if int(A)==A: j+=1
print(j)
j=0
i=0
while True:
    i+=1
    A=float(input(f"{i} Sisesta A  : "))
    if int(A)==A: j+=1
    if i==15: break
print(j)
j=0
i=0
while i<15:
    i+=1
    A=float(input(f"{i} Sisesta A  : "))
    if int(A)==A: j+=1
print(j)


print("Tere! Olen sinu uus sõber - Python!")
a=input("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if a=="1":

    while True:
        try:
            pikkus=int(input("Pikkus: "))
            if pikkus>0 and pikkus<273: break
        except:
            print("Error") 
    mass=-1
    while mass<0 or mass>400:
        try:
            mass=int(input("Mass: "))        
        except:
            print("Error")

    try:
        index=mass/pikkus
        if index<16:
            pass
        elif index>=16 and index<19:
            pass
    except:
        print("Error")


else:
    print("Kahju! See on väga kasulik info!")



#print("Tere tulemast!!!") #kommenteerime

arv=input("Arv")


try:
    arv=int(arv)
    print("Int")  
except:
    try:
        arv=float(arv)
        print("Float")
    except:
        print("Tekst")

#If kasutamine

v=input("Kas tahad dekodeerida?")
if v.upper()=="JAH":
    n=int(input("Sisesta number 1 - 7"))
    if n==1:
        paev="esmaspäev"
    elif n==2:
        paev="teisipäev"

    print(f"{n} - {paev}")
else:
    print("Head aega")

a,b,g=input("Sisesta nurgade suuruseid ").split()
a=int(a)
b=int(b)
g=int(g)
if a>0 and b>0 and g>0:
    if a+b+g==180:
        if a==b and b==g:
            tuup="võrdkülgne"
        elif a==b or a==g or b==g:
            tuup="võrdhaarne"
        else:
            tuup="mitmekülgne"
    else:
        tuup="ei ole kolmnurk"
else:
    tuup="on vaja >0 "
print(tuup)
#Tekstilised funktsioonid ja sissend, väljund 
vastus=input() #jah, Jah,JAH
print(vastus.upper()) #JAH, lower():jah
if vastus.upper()=="JAH":
    tulemus="Suured tähed"

arv=input("Sisesta arv")
#print(arv[:1])
if arv.isalpha():
    print("See on tekst")
elif arv.isdigit():
    arv=int(arv) #str->int
    if arv>0:
        if arv%2==0:
            print(f"{arv} on paaris arv")
        else:
            print(f"{arv} on paaritu arv")
    else:
        print(f"{arv} - ei sobi negatiivne arv")
else:
    print(f"{arv} - segatud tekst ja numbrid")

hinne=int(input("Mis hinne sa sai täna?"))
if hinne>=1 and hinne<=5:
    if hinne==1 or hinne==2:
        vastus="Väga halb töö!"
    elif hinne==3:
        vastus="Rahuldav"
    elif hinne==4:
        vastus="Hea"
    else:
        vastus="Vaga hea"
else:
    vastus="Viga andmetega!"
print(vastus)

a=float(input("Kõrgus: ")) # int, float, str, bool
b=float(input("Laius: "))
if a>0 and b>0:  # ==,!=,>=,<=  or,not          True and True=True
    S=a*b #*,/,+,-,//,%,**, d=e=4
else:
    S="ei saa leida"
print("Pindala: ",S)

d=round(sqrt(a**2+b**2),2)
print("d= "+str(d))
text="A"
print(text*5,end=' ')
print(text)
