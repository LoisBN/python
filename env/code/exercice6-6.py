#encoding:utf8

#exercice 6-6

#question 1

def list_mult(L,k):
    """
    List+Int->List
    hyp : k > 0 et L ne contient que des entiers
    retourne la liste L contenant l'ensemble des nombres de la liste initiale multiplié par k
    """

    #liste : list
    liste = []
    for i in range(0,len(L)):
        liste.append(L[i] * k)
    L = liste
    return L

assert list_mult([3, 5, 9, 4], 2) == [6, 10, 18, 8]

def list_div(L, k):
    """
    List+Int->List
    hyp : k > 0 et L ne contient que des entiers
    retourne la liste L contenant l'ensemble des nombres de la liste initiale multiplié par k
    """ 
    
    #liste : list
    liste = []
    for i in range(0,len(L)):
        if (L[i]% k == 0):
            liste.append(L[i] // k)
    L = liste
    return L

assert list_div([2, 7, 9, -24, 6], -3) == [-3, 8, -2]
assert list_div([2, 7, 9, 24, 6], 3) == [3, 8, 2]
assert list_div([2, 7, 9, 24, 6], 2) == [1, 12, 3]