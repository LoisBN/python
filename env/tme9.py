#encoding:utf8
#tme9

#exercice 9.5

def est_lettre(c):
    """ str -> bool
    Hypothese : len(c) == 1 (caractere)
    Retourne True si le caractere c est une lettre, ou False sinon."""
    return ((c >= 'a') and (c <= 'z')) \
    or ((c >= 'A') and (c <= 'Z')) \
    or (c in {'é', 'è', 'à', 'ù', 'œ'})

def chargement_texte(fichier):
    """ str -> str
    Hypothèse : le fichier est présent sur le disque
    Retourne la chaîne de caractères correspondant au contenu
    du fichier."""
    # contenu : str
    contenu = '' # contenu du fichier
    with open(fichier, 'r') as f:
        contenu = f.read()
    return contenu


#question 1

def frequence_lettre(s):
    """str->dict[str:int]
    retourne les frequences des lettres de s sous la forme d 'un dictionnaire"""
    
    frequence = {}
    for i in s:
        if est_lettre(i):
            frequence[i] = 0

    for caractere in s:
        if est_lettre(caractere) and frequence[caractere] >=0:
            frequence[caractere] = frequence[caractere] + 1
    return frequence

#question 2

def lettre_freq_max(D = {}):
    """dict[str:int]
    retourne la lettre qui a la frequence d 'apparition la plus élevé"""
    
    max = {"lettre":"","frequence":0}

    for lettre, frequence in D.items():
        if frequence > max["frequence"]:
            max["frequence"] = frequence
            max["lettre"] = lettre
    return max["lettre"]

        
#question 3

def lecture_fichier(fichier):
    """str->dict[str:int]"""

    return frequence_lettre(chargement_texte(fichier))

def freq_max_fichier(fichier):
    """"""
    return lettre_freq_max(frequence_lettre(chargement_texte(fichier)))

            
    
#exercice 9.7

#question 1

def valeur_decomposition(D):
    """dict[int:int]->int"""

    result = 1
    compteur = 0
    for nb,freq in D.items():
        while compteur<freq:
            result = result * nb
            compteur = compteur+1
    return result

#question 2

def decomposition(L):
    """list[int]->dict[int:int]"""

    result = {}
    for number in L:
        result[number] = 0
    for number in L:
        result[number] = result[number] + 1
    return result

assert decomposition([3, 3, 3, 4, 4, 5, 1]) == {1: 1, 3: 3, 4: 2, 5: 1}
assert decomposition([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == {2: 10}

#question 3

def liste_facteurs_premiers(n):
    """int->listt[int]"""
    nb = n
    result = []
    liste = [i for i in range(2, n + 1)]

    #liste_erathostene:list[int]
    liste_erathostene = []

    while len(liste)>0:
        liste_erathostene.append(liste[0])
        liste = [j for j in liste if not j % liste[0] == 0]
    i=0
    while nb>1:
        if nb % liste_erathostene[i] == 0:
            result.append(liste_erathostene[i])
            nb = nb / liste_erathostene[i]
        else:
            i = i+1

    return result