


def loe_failist(file:str)->list:
    """Loeme failist read ja lisame järjendisse
    :param str file: Faili nimetus
    """
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def list_failisse(mas:list,file:str):
    """Salvestame loetelu failisse
    :param str file: Faili nimetus
    :param list mas: loetelu
    """
    f=open(file,"w",encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def elem_listisse(p:list,i:list):
    n=int(input("Mitu iminesi lisame?"))
    for j in range(n):
        nimi=input("Nimi: ")
        i.append(nimi)
        palk=input("Palk: ")
        p.append(palk)

    return p,i

def kustutamine(nimi:str,p:list,i:list):
    n=i.count(nimi)
    pos=0
    for j in range(n):
        ind=i.index(nimi,pos)
        pos=ind
        i.remove(nimi)
        p.pop(ind)
    return p,i

def maksimaalne_palk(p:list,i:list):
    p=list(map(int,p))
    max_palk=max(p)
    n=p.count(max_palk)
    pos=0
    print(f"Maksimaalne palk on {max_palk}\nInimeste nimed:")
    for j in range(n):
        ind=p.index(max_palk,pos)
        nimi=i[ind]
        print(f"{nimi}")
        pos=ind+1

def sorteerimine(p:list, inimesed:list,a:int): #0 kasvab ,1 kahaneb
    N=len(p)
    p=list(map(int,p))
    if a==0:
        for i in range(0,N-1):
            for j in range(i+1,N):
                if p[i]<p[j]:
                    abi=p[i]
                    p[i]=p[j]
                    p[j]=abi
                    abi=inimesed[i]
                    inimesed[i]=inimesed[j]
                    inimesed[j]=abi
    else:
        for i in range(0,N-1):
            for j in range(i+1,N):
                if p[i]>p[j]:
                    abi=p[i]
                    p[i]=p[j]
                    p[j]=abi
                    abi=inimesed[i]
                    inimesed[i]=inimesed[j]
                    inimesed[j]=abi
    return p,inimesed
        








def Kontroll(isikukood:str):
    """Isikukoodi kontroll number
    On vaja isikukood sisestada
    :param str isikukood: Inimese isikukood
    :rtype: var Märamata tüüp
    """
    ik_list=list(isikukood)
    s=0
    for i in range(0,10):
        s+=(i%9+1)*int(ik_list[i])
        print(f"{i%9+1}*{int(ik_list[i])}+", end="")
    print(s)
    s=s-(s//11)*11
    print(s)
    if s==int(ik_list[10]):
        vastus=s
    else:
        vastus="Kontroll number on vale"
    return vastus
def Haigla(ik3:int):
    """Haigla 3 isikukoodi numbri alusel
    :param int ik3: Isikukoodi 3 numbrid
    :rtype: str Haigla ja koht
    """
    if ik3>1 and ik3<=10:
        haigla="Kuresaare"
    elif ik3>10 and ik3<=19:
        haigla="Tartu"
    elif ik3>190 and ik3<=225:
        haigla="Haigla"
    # jne
    return haigla
def Sugu(ik1:int)->str:
    """

    """
    if ik1%2==0:
        a="naine"
    else:
        a="mees"
    return a