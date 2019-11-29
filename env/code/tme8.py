#Tme 8

#exercice 8.2

#question 1

def moyenne(listOfNumber):
    """list[number]->float
    retourne la valeur moyenne de l 'ensemble des valeurs contenues dans la liste"""

    #result:float
    result = 0.0

    #number:number
    for number in listOfNumber:
        result = result + number
    return result/len(listOfNumber)
    
#question 2

def ecart_nombre(L,x):
    """list[number]*number->list[number]
    retourne la valeur absolue de la difference entre les valeurs de L et x """

    #element:number
    return [element - x if element-x>=0 else element-x*(-1) for element in L]
    
#question 3

def liste_carre(L):
    """list[number]->list[number]
    retourne la liste contenant les elements au carre de L """
    
    #element:number
    return [element ** 2 for element in L]
    
#question 4

def variance(L):
    """list[number]->float
    retourne la variance associe a la liste L """

    #element:number
    return moyenne(liste_carre(ecart_nombre([element for element in L], moyenne(L))))
    
#question 5

def variance_plus(L):
    return moyenne([(element-moyenne(L))**2 if (element-moyenne(L))>=0 else (element-moyenne(L)*(-1))**2 for element in L])


#exercice 8.4

#question 1

def liste_non_multiple(n,L):
    """int*list[int]->list[int]
    hyp:n>0 
    retourne la liste des elements de L qui ne sont pas multiple de n """
    
    #element:int
    return [element for element in L if not element % n == 0]

#question 2

def erathostene(n):
    """int->list[int]
    hyp:n>0
    retourne la liste des nombres premiers inferieurs a n """
    #liste:list[int]
    liste = [i for i in range(2, n + 1)]

    #liste_erathostene:list[int]
    liste_erathostene = []

    while len(liste)>0:
        liste_erathostene.append(liste[0])
        liste = [j for j in liste if not j%liste[0] == 0]
    return liste_erathostene


#question 3

def liste_facteurs_premiers(n):
    """int->list[int]
    hyp:n>2
    retourne la liste des facteurs premiers de n """
    
    liste_erathostene = erathostene(n)
    return [j for j in liste_erathostene if n % j == 0]
    

#exercice 8.6

BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

#question 1

def mauvaise_note(etu):
    """etudiant->bool
    retourne true si l 'etudiant a obtenu au moins une note en dessous de la moyenne sinon retourne false"""
    
    (nom, prenom, ide, notes) = etu
    for note in notes:
        if note < 10:
            return True
    return False

#question 2

def eleve_mauvaise_note(database):
    """list[etudiant]->list[etudiant]
    retourne une liste contenant les etudiants ayant eu des notes en dessous de la moyenne """
    
    return [eleve for eleve in database if mauvaise_note(eleve)]

#question 3

def nom_eleve_mauvaise_note(database):
    """list[etudiant]->list[etudiant]
    retourne une liste contenant le nom des etudiants ayant eu des notes en dessous de la moyenne """
    
    return [eleve[0] for eleve in database if mauvaise_note(eleve) ]

#print(nom_eleve_mauvaise_note(BaseUPMC))

#question 4

def ide_eleve_bonne_note(database):
    """list[etudiant]->list[etudiant]
    retourne une liste contenant les identifiants des etudiants ayant aucunes notes en dessous de la moyenne """
    
    return [eleve[2] for eleve in database if not mauvaise_note(eleve)]
    
print(ide_eleve_bonne_note(BaseUPMC))