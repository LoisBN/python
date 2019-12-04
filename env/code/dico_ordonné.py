#encodint:utf8

class Dico_ordonné:
    """Ceci est un dictionnaire imitant le comportement d'une liste et étant relativement ordonné,peut donc être soumis à des méthodes de tri"""
    def __init__(self,dico=None,**keyValue):
        self.keys = []
        self.values = []
        if dico is not None:
            for key,value in dico.items():
                self.keys.append(key)
                self.values.append(value)
        for key,value in keyValue.items():
            self.keys.append(key)
            self.values.append(value)
            
    def __str__(self):
        dico = {}
        for i in range(0,len(self.keys)):
            dico[self.keys[i]] = self.values[i]
        return str(dico)
                
        
    def __getitem__(self,index):
        i = 0
        while i < len(self.keys):
            if self.keys[i] == index:
                return {self.keys[i]:self.values[i]}
            i += 1
    
    def __setitem__(self,index,value):
        i = 0
        while i < len(self.keys):
            if self.keys[i] == index:
                self.values[i] = value
                return
            i += 1
        self.keys.append(index)
        self.values.append(value)

    def __delitem__(self,index):
        i = 0
        while i<len(self.keys):
            if self.keys[i] == index:
                del self.keys[i]
                del self.values[i]
            i += 1
    
    def __contains__(self,key):
        return key in self.keys
    
    def __len__(self):
        return len(self.keys)

    def __iter__(self):
        return Dico_ordonné_Iterator(self)
    
    def __add__(self,dict2):
        self.keys.extend(dict2.keys)
        self.values.extend(dict2.values)
    
    def key(self):
        for key in self.keys:
            yield key
    
    def value(self):
        for value in self.values:
            yield value

    def items(self):
        for i in range(len(self.keys)):
            yield self.keys[i], self.values[i]

    def sort(self):
        liste = []
        for i in range(0,len(self.keys)):
            couple = (self.keys[i], self.values[i])
            liste.append(couple)
        liste.sort(key=lambda couple: couple[0])
        self.keys = []
        self.values = []
        for a, b in liste:
            self.keys.append(a)
            self.values.append(b)

    def reverse(self):
        liste1 = [element for element in self.keys]
        liste2 = [element for element in self.values]

        self.keys = []
        self.values = []
        i = len(liste1) - 1
        for a in liste1:
            self.keys.append(liste1[i])
            i -= 1
        for b in liste2:
            self.values.append(liste2[i])
            i -= 1
        
    

class Dico_ordonné_Iterator:
    def __init__(self,target):
        self.target = target
        self.position = 0
    
    def __next__(self):
        if self.position == len(self.target)-1:
            raise StopIteration
        self.position += 1
        return self.target[self.position]
    
    
    
dico = Dico_ordonné({"cle1":2,"cle2":1})
dico2 = Dico_ordonné({"cle8": 12, "cle9": 19})
dico3 = Dico_ordonné(zou= "a", ru = "b", ale = "c", bisou = "d", damien = "z")
print(dico3)
dico3.sort()
print(dico3)
dico3.reverse()
print(dico3)
print(dico["cle1"])
dico["cle1"] = 3
dico["cle3"] = 4
print(dico["cle1"])
del dico["cle1"]
dico2 + dico
print(dico2)
print(dico)
print("cle2" in dico)
print(len(dico))
for i in dico.items():
    print(i)

        