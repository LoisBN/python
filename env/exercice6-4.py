#exercice 6.4
#question 1
def liste_diviseurs(a):
    """
    Int->List
    hyp: a > 0
    retourne l'ensemble des diviseurs de a
    """
    #result: list
    result = []

    #i : int
    i = 1
    while(i <= a):
        if a%i == 0:
            result.append(i)
        i = i+1
    return result

assert liste_diviseurs(18) == [1, 2, 3, 6, 9, 18]
assert liste_diviseurs(24) == [1, 2, 3, 4, 6, 8, 12, 24]

def liste_diviseurs_impairs(a):
    """
    Int->List
    hyp: a > 0
    retourne l'ensemble des diviseurs de a impairs
    """

    #result : list
    result = []

    #i:int
    i = 1

    while i<=a:
        if a%i == 0 and not i%2 == 0:
            result.append(i)
        i = i + 1
    return result

assert liste_diviseurs_impairs(24) == [1, 3]
assert liste_diviseurs_impairs(8) == [1]
assert liste_diviseurs_impairs(15) == [1,3,5,15]
        
def liste_diviseurs_pairs(a):
    """
    Int->List
    hyp: a > 0
    retourne l'ensemble des diviseurs de a pairs
    """

    #result : list
    result = []

    #i:int
    i = 1

    while i<=a:
        if a%i == 0 and i%2 == 0:
            result.append(i)
        i = i + 1
    return result

assert liste_diviseurs_pairs(24) == [2, 4, 6, 8, 12, 24]
assert liste_diviseurs_pairs(7) == []
assert liste_diviseurs_pairs(8) == [2,4,8]