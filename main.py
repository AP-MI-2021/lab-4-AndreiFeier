def citire_lista():
    '''
    Citeste lista
    :return:list,lista de numere
    '''
    lista =input("lista : ")
    lista=lista.split()
    lista=[int(el)for el in lista]
    return lista
def afisare_negative(lista):
    '''
    Afiseaza numerele negative din lista
    :param lista:list,lista de numere initiala
    :return:None
    '''
    for el in lista :
        if el < 0:
            print(el)
def afisare_mic(lista,cifra):
    '''
    Afiseaza cel mai mic numar pozitiv cu ultima cifra parametrul cifra
    :param lista:list,lista de numere initiala
    :param cifra: int,ultima cifra
    :return: int,cel mai mic numar
    '''
    ok=False
    for el in lista:
        if el % 10 ==cifra and el>10:
            ok=True
            minim=el
            break
    if ok == True:
        for el in lista :
            if el % 10==cifra and minim >el and el > 10:
                minim = el
        print(minim)
    else:
        print("Nu exista")
def is_prime(n):
    '''
    Verifica daca n este numar prim
    :param n: int,numarul pe care vrem sa il verificam
    :return: True daca n prim,False altfel
    '''
    for i in range(2,n-1):
        if n%i == 0:
            return False
    return True
def test_is_prime():
    assert(is_prime(5)==True)
    assert (is_prime(2) == True)
    assert (is_prime(4) == False)
    assert (is_prime(13) == True)
def is_superprim(n):
    '''
    Verifica daca numarul n este superprim
    :param n: int,numarul pe care vrem sa il verificam
    :return: True daca n superprim,False altfel
    '''
    if n<=1:
        return False
    while n!=0:
        if is_prime(n)==False:
            return False
        n=n//10
    return True
def test_is_superprim():
    assert(is_superprim(123)==False)
    assert (is_superprim(239) == True)
    assert (is_superprim(23) == True)
    assert (is_superprim(1045) == False)
def afisare_superprim(lista):
    '''
    Afiseaza toate numerele superprime din lista
    :param lista: list,lista initiala
    :return: None
    '''
    for el in lista :
        if is_superprim(el)==True:
            print(el)
def cmmdc(a,b):
    '''
    Afla cmmdc dintre a si b
    :param a:int
    :param b:int
    :return:int,cmmdc dintre a si b
    '''
    if b==0:
        return a
    return cmmdc(b,a%b)
def test_cmmdc():
    assert(cmmdc(24,16)==8)
    assert (cmmdc(18, 27) == 9)
    assert (cmmdc(11, 23) == 1)
    assert (cmmdc(1,5) == 1)
def invers(a):
    '''
    Calculeaza numarul negativ inversat din numarul dat
    :param a:int
    :return:int,inversul lui a
    '''
    a=-a
    aux=0
    while a!=0:
        aux=aux*10+a%10
        a=a//10
    return -aux
def test_invers():
    assert(invers(-13)==-31)
    assert (invers(-1234) == -4321)
    assert (invers(-51) == -15)
    assert (invers(-6) == -6)
def afisare_modificat(lista):
    '''
    Afiseaza lista de numere modificate dupa cerinta
    :param lista:list,lista initiala
    :return:None
    '''
    rezultat=[]
    ok=True
    for el in lista :
        if el >0:
            ok=False
            d=el
            break
    if ok==False:
        for el in lista:
            if el>0:
                d=cmmdc(d,el)
    for el in lista:
        if el >0:
            rezultat.append(d)
        else :
            rezultat.append(invers(el))
    print("lista este: ",rezultat)
def print_menu():
    print("1. Citirea unei liste de numere întregi. Citirile repetate suprascriu listele precedente.")
    print("2. Afișarea tuturor numerelor negative nenule din listă")
    print("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
    print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
    print("5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
    print("6. Exit")
def start():
    lista=[]
    while True:
        print_menu()
        optiune=input("Selectati optiunea")
        if optiune == "1":
            lista=citire_lista()
        elif optiune=="2":
            afisare_negative(lista)
        elif optiune=="3":
            cifra=int(input("Ultima cifra : "))
            afisare_mic(lista,cifra)
        elif optiune=="4":
            afisare_superprim(lista)
        elif optiune=="5":
            afisare_modificat(lista)
        else:
            break
test_is_prime()
test_is_superprim()
test_cmmdc()
test_invers()
start()






