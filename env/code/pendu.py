#encoding:utf8

import math,random

def pendu():
    continuer = "1"
    while continuer == "1" or continuer == "yes" or continuer == "y" or continuer == "oui":
        print("\n")
        print("bonjour bienvenue dans le pendu un mot aléatoire va être choisi et vous allez devoir le trouver lettre par lettre \n")
        nom = input("veuillez entrez votre nom :")
        score = 1200
        listeMots = ["aligator", "stalactite", "stalagmite", "australopitheque", "cyclomoteur", "vampire", "torche", "serpent", "python", "revolver", "animateur", "josé", "moine", "mathematiques","bonheur","antenne","téléviseur","audiovisuel","connard","bonobo","inspiration","atomique"]
            
        mot = listeMots[random.randint(0, len(listeMots) - 1)]

        motCache = ""

        i=0
        while i < len(mot):
            motCache += "*"
            i += 1
        del i

        listeLettre = []

        for lettre in motCache:
            listeLettre.append(lettre)
        
        lettreDonnées = []
        lettresFausses = []

        print(motCache)

        compteur1 = 0
        compteur2 = 0

        while 1:
            guess = input("essayez de deviner une lettre :")
            
            try:
                if guess in listeLettre:
                    raise NameError("you have already use this letter")

                if not len(guess) == 1:
                    raise ValueError("you have to choose a letter not more not less")

                if not guess.lower() in "azertyuiopqsdfghjklmwxcvbnéèàêùç":
                    raise TypeError("Pick letter please")
                
                for i in range(0, len(mot)):
                    if guess == mot[i]:
                        listeLettre[i] = guess
                        compteur2 += 1
                
                if compteur2 == compteur1:
                    score -=100
                    print("mauvaise réponse la lettre {} n'est pas dans le mot il te reste {} tentatives et {} lettres...bonne chance...\n".format(guess, score // 100, len(listeLettre) - compteur2))
                    lettreDonnées.append(guess)
                    lettresFausses.append(guess)

                if compteur2>compteur1:
                    print("bien joué tu as trouver la lettre {} qui apparait {} fois. Tu as deja trouver {} lettres , plus que {} lettres.\n".format(guess, compteur2 - compteur1, compteur2, len(mot) - compteur2))
                    compteur1 = compteur2
                    lettreDonnées.append(guess)

                if "".join(listeLettre) == mot:
                    print("Tu as trouver le mot était bel et bien : {}".format(mot))
                    print("ton score est de {}".format(score))
                    break

                if score == 0:
                    print('tu as perdu... Le mot était : {}'.format(mot))
                    break

                print("".join(listeLettre))
            except ValueError:
                print("\ntu dois choisir une et une seule lettre ")
                continue
            except NameError:
                print("\ntu as déja choisi cette lettre")
                continue
            except TypeError:
                print("\ntu dois choisir une lettre et non un chiffre ou un caractère spécial")
                continue
            except KeyboardInterrupt:
                print("vous avez manuellement quitter le programme bye...")
                return

        print("la partie est terminée")
        continuer = input("cliquer sur 1 pour continuer et sur n'importe quelle autre touche pour quitter: ")
        with open("dbpendu","a") as db:
            db.write("\n{} | {}".format(nom,score))
    

pendu()

class penduManager:

    nbmanager = 0
    def __init__(self,name,game,score):
        self.name = name
        self.game = game
        self._score = score
        self.users = {}
    
    def addPenduManager(self, target):
        name, instance = target
        self.users[name] = instance
    
    def _get_score(self):
        return self._score
    
    def _set_score(self,score):
        self._score = score

    def _del_score(self):
        del self._score
    
    def increment(cls):
        cls.nbmanager += 1

    def test():
        print("this is a static method")
    
    increment = classmethod(increment)
    score = property(_get_score,_set_score,_del_score,"""this is the score of the player""")
    test = staticmethod(test)
        
    
                
    
