def citire_lista():
    lista =input("lista : ")
    lista=lista.split()
    lista=[int(el)for el in lista]
    return lista
def afisare_negative(lista):
    for el in lista :
        if el < 0:
            print(el)
def afisare_mic(lista,cifra):
    ok=False
    for el in lista:
        if el % 10 ==cifra :
            ok=True
            minim=el
            break
    if ok == True:
        for el in lista :
            if el % 10==cifra and minim >el :
                minim = el
        print(minim)
    else:
        print("Nu exista")
def is_prime(n):
    for i in range(2,n-1):
        if n%i == 0:
            return False
    return True
def is_superprim(n):
    if n<=1:
        return False
    while n!=0:
        if is_prime(n)==False:
            return False
        n=n//10
    return True
def afisare_superprim(lista):
    for el in lista :
        if is_superprim(el)==True:
            print(el)
def cmmdc(a,b):
    if b==0:
        return a
    return cmmdc(b,a%b)
def invers(a):
    a=-a
    aux=0
    while a!=0:
        aux=aux*10+a%10
        a=a//10
    return -aux
def afisare_modificat(lista):
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
start()






