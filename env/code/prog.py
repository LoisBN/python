#encoding:utf8

from operator import itemgetter,attrgetter

class Zdict:
    def __init__(self):
        self._dico = {}
    
    def __getitem__(self,index):
        return self._dico[index]
    
    def __setitem__(self, index, value):
        self._dico[index] = value
    
    def __delitem__(self,index):
        del self._dico[index]
    
    def __len__(self):
        return len(self._dico)
    
    def __contains__(self, element):
        for _,stuff in self._dico.items():
            if element == stuff:
                return True
    
    def getDico(self):
        return self._dico
    
    def __str__(self):
        return "je suis un dictionnaire tout ce qu'il y a de moins normal"
    dico = property(getDico)

class Duree:
    def __init__(self,minutes=0,sec=0):
        self.minutes = minutes
        self.sec = sec
    
    def __str__(self):
        return "{0:02} minutes: {1:02} seconds".format(self.minutes, self.sec)
    
    def __add__(self, number):
        nouvelleDuree = Duree()
        nouvelleDuree.sec = self.sec+number
        nouvelleDuree.minutes = self.minutes
        if nouvelleDuree.sec >= 60:
            nouvelleDuree.minutes = self.minutes + (1 * ((self.sec + number) // 60))
            nouvelleDuree.sec = (self.sec + number) % 60
        return nouvelleDuree

    def __radd__(self, number):
        nouvelleDuree = Duree()
        nouvelleDuree.sec = self.sec+number
        nouvelleDuree.minutes = self.minutes
        if nouvelleDuree.sec >= 60:
            nouvelleDuree.minutes = self.minutes + (1 * ((self.sec + number) // 60))
            nouvelleDuree.sec = (self.sec + number) % 60
        return nouvelleDuree
    
    def __gt__(self, duree):
        pass

# d1 = Duree(1, 5)
# print(d1)
# print(d1+12)
#  a = Zdict()
# b=[1,2,3]
# a["taille"] = 1.55
# print(1.55 in a)
# print(len(a.dico))
# del a["taille"]
# print(len(a._dico)



class Etudiants:
    def __init__(self,nom,age,moyenne):
        self.nom = nom
        self.age = age
        self.moyenne = moyenne
    
    def __repr__(self):
        return "étudiant {} : age {},moyenne {}".format(self.nom, self.age, self.moyenne)

etudiants = [
    Etudiants("Clément", 14, 16),
    Etudiants("Charles", 12, 15),
    Etudiants("Oriane", 14, 18),
    Etudiants("Thomas", 11, 12),
    Etudiants("Damien", 12, 15),
]

# print(sorted(etudiants,key=lambda etudiant: etudiant.age))

class LigneInventaire:
    
    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}X{}) \n>".format(
                self.produit, self.prix, self.quantite)

# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
]

# inventaire.sort(key=attrgetter("quantite"), reverse=True)
# print(sorted(inventaire, key=attrgetter("prix")))

inventaire2 = [
    ("pomme rouge", 1.2, 19),
    ("orange", 1.4, 24),
    ("banane", 0.9, 21),
    ("poire", 1.2, 24),
]

# inventaire2.sort(key=itemgetter(2),reverse=True)
# print(sorted(inventaire2,key=itemgetter(1)))

class Personne:
    def __init__(self,nom,prenom="inconnu"):
        self.prenom = prenom
        self.nom = nom
    
    def bonjour():
        print("bonjour")
    bonjour = staticmethod(bonjour)
    
    def __str__(self):
        return "Je suis {} {}\n".format(self.prenom, self.nom)
    
class AgentSpecial(Personne):
    def __init__(self,matricule,nom):
        self.matricule = matricule
        Personne.__init__(self, nom)
        
    def __str__(self):
        return "je suis l'agent {} matricule : {}\n prenom : {}".format(self.nom, self.matricule, self.prenom)

hitman = AgentSpecial("002", "Bloomberg")
# hitman.bonjour()
# # print(hitman)

# chaine = "ceci est un test"
# iterator = iter(chaine)
# i = 0
# while i < len(chaine):
#     print(next(iterator))
#     i += 1
# del i


class RevStr(str):
    def __iter__(self):
        return ItRevStr(self)

class ItRevStr:
    def __init__(self,target):
        self.target = target
        self.postion = len(target)
    
    def __next__(self):
        if self.postion == 0:
            raise StopIteration
        self.postion -= 1
        return self.target[self.postion]

def RevStrGen(string):
    i = len(string)-1
    while i>=0:
        yield string[i]
        i-=1
        
for i in RevStrGen("coucou"):
    print(i)
    
def generator(min, max):
    i = min+1
    while i<max:
        values = yield i * i
        if values is not None:
            i = values-1
        i+=1
        
        
generateur = generator(10, 21)
for nombre in generateur:
    if nombre == 12:
        generateur.send(15)
    print(nombre)