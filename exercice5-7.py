#encoding:utf8
#exercice 5.7

#question 1

"""specification de la fonction ord:
str->int
retourne le numéro unicode correspondant au caractère entré"""


def chiffre(x):
    """int->int\n
    hypothèse: x est un chiffre compris entre 0 et 9 inclus\n
    retourne l'entier correspondant au caractère x donné"""
    return ord(x)-ord("0")

#question 2
def entier(s):
    #number:int
    number = 0

    #i:int
    i = 0
    while i<len(s):
        number = number*10 + chiffre(s[i])
        i = i+1
    return number

#question 3

"""spécification de la fonction chr:
int->str
retourne un caractère à partir du numéro unicode entré en paramètre"""

def caractere(x):
    """int->str\n
    hypothèse : x est un entier naturel et x < 10\n
    retourne l'entier x entré en paramètre sous la forme d'une chaine de caractère"""
    return chr(x + ord('0'))


def chaine(n):
    chaine = ""
    while n>= 1:
        chaine = caractere(n%10) + chaine
        n = n//10
    return chaine

print(chaine(1122343))