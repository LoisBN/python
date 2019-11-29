#encoding:utf8

#Exercice 6.9

#Question 1

def jonction(L,c):
    """ list[str] * str -> str
    Hypothèse : len(c) = 1
    retourne la chaîne composée de la jonction des
    chaîne de L séparées deux-à-deux par le
    caractère séparateur c.
    """
    texte = ""
    for i in range(0, len(L)):
        if L[i] != L[len(L)-1] :
            texte = texte + L[i] + c
        else:
            texte = texte + L[i]
    return texte

print(jonction(['les', 'mots', 'de', 'cette', 'phrase'], '/'))

def separation(L, c):
    """ str * str -> list[str]
    Hypothèse : len(c) = 1
    retourne la liste de chaînes composées des sous-chaînes
    de s séparées par le caractère séparateur c.
    Le séparateur c n 'est pas présent dans la chaîne résultat.
    """

    tableau = []
    index_sep = 0
    for i in range(0,len(L)):
        if L[i] == c:
            tableau.append(L[index_sep:i])
            index_sep = i + 1
        
        elif i == len(L)-1:
            tableau.append(L[index_sep:i+1])
    return tableau

print(separation('un.deux.trois quatre', '.'))
print(separation('les mots de cette phrase', ' '))

