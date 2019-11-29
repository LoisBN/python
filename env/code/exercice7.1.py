#encoding:utf8
#exercice 7.1

#question 1

def partie_reelle(c):
    return c[0]

def partie_imaginaire(c):
    return c[1]

#question 2
def addition_complexe(c1,c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

#question 3
def produit_complexe(c1,c2):
    terme1 = c1[0] * c2[0] - c1[1] * c2[1]
    terme2 = c1[0] * c2[1] + c1[1] * c2[0]
    return (terme1, terme2)

#exercice 7.3
def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b,r)

def fraction(a,b):
    return (a / pgcd(a, b), b / pgcd(a, b))
    
print(fraction(121, 187))