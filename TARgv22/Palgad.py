from Oma_moodul import *
palgad=[]
inimesed=[]
while True:
    print("--------------------------")
    print("0-loe failist\n1-andmete lisamine\n2-salvestame failisse\n3-kustuta nimi järgi\n4-max palk ")
    v=int(input())
    if v==0:
        palgad=[]
        inimesed=[]
        palgad=loe_failist("Palgade_file.txt")
        inimesed=loe_failist("Nimede_file.txt")
        #palgad=str_to_int(palgad)
        print(palgad)
        print(inimesed)

    elif v==1:
        palgad, inimesed=elem_listisse(palgad,inimesed)
        print(palgad)
        print(inimesed)
    elif v==2:
        list_failisse(palgad,"Palgade_file.txt")
        list_failisse(inimesed,"Nimede_file.txt")
    elif v==3:
        palgad,inimesed=kustutamine(input("Sisesta nimi"),palgad,inimesed)
        print(palgad)
        print(inimesed)
    elif v==4:
        maksimaalne_palk(palgad,inimesed)
    elif v==5:
        palgad,inimesed=sorteerimine(palgad,inimesed,0)
        for i in range(len(palgad)):
            print(f"{palgad[i]} - {inimesed[i]}")
