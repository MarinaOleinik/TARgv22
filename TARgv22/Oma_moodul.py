
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