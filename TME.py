#encoding:utf8


#Exercice 4.4
#question 1
def nb_couples_intervalle(n,p):
    """int+int->int\n
    hypothèse : n<=p\n
    retourne le nombre de couples d'entier (i,j) appartenant à l'intervalle [n,p]"""
    compteur = 0
    i=n
    j=p
    while (i<j):
        while True:
            if j == i+1:
                j = p
                break
            compteur = compteur + 1
            j = j-1
        compteur = compteur + 1
        i = i+1
    return compteur
        

assert nb_couples_intervalle(-1,3) == 10   
assert nb_couples_intervalle(2,4) == 3
assert nb_couples_intervalle(0,0) == 0    

#question 2
def nb_couples_divise(n,p):
    """
    int+int->int\n
    hypothèse : n ≤ p\n
    retourn le nombre de couples entiers (i,j) dans l'intervalle [n,p] tels que i divise j"""
    compteur = 0
    i = n
    j = p
    while j>n:
        while True:
            if i==p:
                i = n
                break
            if (i!=0 and j!=i and j%i == 0):
                compteur = compteur +1
            i = i+1
        j = j-1
    return compteur

assert nb_couples_divise(4,6) == 0
assert nb_couples_divise(2,6) == 3
assert nb_couples_divise(1,10) == 17

#question 3
def nb_couples_divise_trace(n,p):
    """
    int+int->int\n
    hypothèse : n ≤ p\n
    retourn le nombre de couples entiers (i,j) dans l'intervalle [n,p] tels que i divise j en affichant une trace de l'avancement du programme lors de l'execution"""
    compteur = 0
    i = n
    j = p
    while j>n:
        while True:
            if i==p:
                i = n
                break
            if (i!=0 and j!=i and j%i == 0):
                print("---------------")
                print(i," divise ",j)
                print("--------------")
                compteur = compteur +1
            print("couple (",i,",",j,")")
            i = i+1
        j = j-1
    return compteur

#question 4
def existe_couples_divise(n,p):
    """ int * int -> bool\n
Hypothèse : n <= p\n
renvoie True s'il existe un couple (i,j) d'entiers appartenant
à l'intervalle [n,p] tels que i != j et i divise j,
ou False sinon."""
    compteur = 0
    i = n
    j = p
    while j>n:
        while True:
            if i==p:
                i = n
                break
            if (i!=0 and j!=i and j%i == 0):
                compteur = compteur +1
            i = i+1
        j = j-1
    return compteur>0

assert existe_couples_divise(0, 0) == False
assert existe_couples_divise(2, 6) == True
assert existe_couples_divise(-1, 1) == True
assert existe_couples_divise(1, 10) == True
assert existe_couples_divise(21, 34) == False


def existe_couples_divise_rapide(n,p):
    """ int * int -> bool\n
Hypothèse : n <= p\n
renvoie True s'il existe un couple (i,j) d'entiers appartenant
à l'intervalle [n,p] tels que i != j et i divise j,
ou False sinon."""
    compteur = 0
    i = n
    j = p
    while j>n:
        while True:
            if i==p:
                i = n
                break
            if (i!=0 and j!=i and j%i == 0):
                compteur = compteur +1
                break
            i = i+1
        if compteur>0:
            break
        j = j-1
    return compteur>0

assert existe_couples_divise_rapide(0, 0) == False
assert existe_couples_divise_rapide(2, 6) == True
assert existe_couples_divise_rapide(-1, 1) == True
assert existe_couples_divise_rapide(1, 10) == True
assert existe_couples_divise_rapide(21, 34) == False

def existe_couples_divise_rapide2(n,p):
    """ int * int -> bool\n
Hypothèse : n <= p\n
renvoie True s'il existe un couple (i,j) d'entiers appartenant
à l'intervalle [n,p] tels que i != j et i divise j,
ou False sinon."""
    compteur = 0
    i = n
    j = p
    while j>n:
        while True:
            if i==p:
                i = n
                break
            if (i!=0 and j!=i and j%i == 0):
                compteur = compteur +1
                return compteur>0
            i = i+1
        j = j-1
    return compteur>0

assert existe_couples_divise_rapide2(0, 0) == False
assert existe_couples_divise_rapide2(2, 6) == True
assert existe_couples_divise_rapide2(-1, 1) == True
assert existe_couples_divise_rapide2(1, 10) == True
assert existe_couples_divise_rapide2(21, 34) == False


#question 6
def existe_couples_divise_trace_tour(n,p):
    """ int * int -> bool\n
Hypothèse : n <= p\n
renvoie True s'il existe un couple (i,j) d'entiers appartenant
à l'intervalle [n,p] tels que i != j et i divise j,
ou False sinon."""
    compteur = 0
    compteur2 = 0
    i = n
    j = p
    while j>n:
        while True:
            if i==p:
                i = n
                break
            if (i!=0 and j!=i and j%i == 0):
                compteur = compteur +1
            i = i+1
            compteur2 = compteur2 +1
        j = j-1
    print("nombre de couples testés : ",compteur2)
    print(compteur>0)
    return compteur>0

assert existe_couples_divise(0, 0) == False
assert existe_couples_divise(2, 6) == True
assert existe_couples_divise(-1, 1) == True
assert existe_couples_divise(1, 10) == True
assert existe_couples_divise(21, 34) == False

existe_couples_divise_trace_tour(3,1000)

def existe_couples_divise_rapide_trace_tour(n,p):
    """ int * int -> bool\n
Hypothèse : n <= p\n
renvoie True s'il existe un couple (i,j) d'entiers appartenant
à l'intervalle [n,p] tels que i != j et i divise j,
ou False sinon."""
    compteur = 0
    compteur2 = 0
    i = n
    j = p
    while j>n:
        while True:
            if i==p:
                i = n
                break
            if (i!=0 and j!=i and j%i == 0):
                compteur = compteur +1
                break
            i = i+1
            compteur2 = compteur2 + 1
        if compteur>0:
            break
        j = j-1
    print("nombre de couples testés : ",compteur2)
    print(compteur>0)
    return compteur>0

existe_couples_divise_rapide_trace_tour(3,1000)

assert existe_couples_divise_rapide(0, 0) == False
assert existe_couples_divise_rapide(2, 6) == True
assert existe_couples_divise_rapide(-1, 1) == True
assert existe_couples_divise_rapide(1, 10) == True
assert existe_couples_divise_rapide(21, 34) == False