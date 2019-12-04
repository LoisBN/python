#encoding:utf8

#tme 10

#exercice 1
import math

Liste = [ 2, 5, 12, 31, 2, 17, 31, 42, 2 ]
Dico = {'xx': 'bli', 'yzy': 'blo', 'cuicui': 'toutou', 'miaou': 'toutou'}
Ens = {2.7, 4.12, 3.31, 8.29, 1.13, 12.31}

#q1

[('xx', 'bli'), ('yzy', 'blo'), ('cuicui', 'toutou'), ('miaou', 'toutou')]
[('xx', 'bli'), ('yzy', 'blo'), ('cuicui', 'toutou'), ('miaou', 'toutou')]
['bli', 'blo', 'toutou', 'toutou']
['bli', 'blo', 'toutou', 'toutou']

#q2

{'a', 'b', 'c', ' '}
{'a', 'b', 'c'}
{('cuicui', 'toutou'), ('miaou', 'toutou'), ('yzy', 'blo'), ('xx', 'bli')}
{'bli', 'toutou', 'blo'}
{'bli', 'toutou', 'blo'}
{'miaous', 'cuicuis'}
{0, 1, 2}
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#On remarque lorsque l'on compare la compréhension de liste et la compréhension d'ensemble  qu'elles contiennent les  mêmes valeurs mais que la compréhension d'ensemble a suprimer les doublons,on remarque aussi dans la compréhension de liste que la série 0,1,2,...,9 se répète  20//10 fois.


#q3

{'xx': 'bli', 'yzy': 'blo', 'cuicui': 'toutou', 'miaou': 'toutou'}
{'bli': 'xx', 'blo': 'yzy', 'toutou': 'miaou'}
{'blibli': 'xx', 'bloblo': 'yzy', 'toutoutoutou': 'miaou'}
{'blibli': 'xx', 'bloblo': 'yzy', 'toutoutoutou': 'miaou'}
{1: 2, 2: 5, 3: 12, 4: 31, 5: 2, 6: 17, 7: 31}
{1: 42, 2: 42, 3: 42, 4: 42, 5: 42, 6: 42, 7: 42, 8: 42, 9: 42}

#exercice 10.2

#q1
def diff_sym(E1, E2):
    return {k for j in zip(E1,E2) for k in j if not ((k in E1) and (k in E2))}

#q2
def fourchette_prix(mini,maxi,prix):
    return {a for a, b in prix.items() if b >= mini and b <= maxi}

#q3

Dessert = {
'gateau chocolat' : {'chocolat', 'oeuf', 'farine', 'sucre', 'beurre'},
'gateau yaourt' : {'yaourt', 'oeuf', 'farine', 'sucre'},
'crepes' : {'oeuf', 'farine', 'lait'},
'quatre-quarts' : {'oeuf', 'farine', 'beurre', 'sucre'},
'kouign amann' : {'farine', 'beurre', 'sucre'}
}

def recette_avec(D,i):
    return {a for a, b in D.items() for c in b if c == i}

def tous_ingredients(D):
    return {c for a, b in D.items() for c in b}
    
def table_ingredient(D):
    return {a:{b for b in {u for u,r in D.items() for x in r if x==a}} for c,d in D.items() for a in d}

def recette_sans(D,i):
    return {c:b for c, b in D.items() if not (i in b)}

#q4

def lettre_freq_inf(freqs,fseuil):
    return {j for j, i in freqs.items() if i <= fseuil}

#q5
Dict_Ang_Fra = {'the': 'le', 'cat': 'chat','fish': 'poisson', 'catches': 'attrape'}
Dict_Fra_Ita = {'le': 'il', 'chat': 'gatto','poisson': 'pesce', 'attrape': 'cattura'}

def traduction_mot_a_mot(L,D):
    return [b for a,b in D.items() for q in L if a==q]
















#exercice 10.3

#q1
def melement_list(L):
    return {a for a in L}

def melement_dict(D):
    return {a for a,b in D.items()}

#q2
def mdict_de_mlist(L):
    i = 0
    mdict = {}
    for a in L:
        mdict[a] = 0
    while i<len(L):
        mdict[L[i]] += 1
        i += 1
    return mdict

#q3
def mlist_de_mdict(D):
    liste = []
    for a,b in D.items():
        for i in range(b):
            liste.append(a)
    return liste

def mlist_de_mdict_comprehension(D):
    return [a for x, y in D.items() for a in [x for i in range(y)]]

#q4
def minter_dict(D1,D2):
    liste = [{x for x, y in D1.items()}, {x for x, y in D2.items()}]
    dico = {x: 0 for z in liste for x in z if (x in D1) and (x in D2)}
    for element in dico:
        dico[element] = min(D1[element], D2[element])
    return dico

minter_dict({'a': 2, 'b': 4, 'c': 3}, {'f': 1, 'a': 1, 'b': 3})

#q5
def minter_list(L1,L2):
    return mlist_de_mdict_comprehension(minter_dict(mdict_de_mlist(L1), mdict_de_mlist(L2)))

#q6
def munion_list(L1,L2):
    liste = []
    for i in range(len(L1)):
        liste.append(L1[i])
    for i in range(len(L2)):
        liste.append(L2[i])
    return liste

#on peut en effet effectuer la fonction munion_dict par comprehension en recuperant les cles et les valeurs dans des listes et en les parcourants par comprehension en les mettants dans des dictionnaires

#exercice 10.5
