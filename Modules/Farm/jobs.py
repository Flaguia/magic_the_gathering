# Le metier doit être unique à chaque personage
from math import sqrt

class Job:
    def __init__(self):
        self.lvl=0
        self.xp=0
        self.multiplier=1
        
    def work(self,outil, place):
        self.addXp(50)        

        if outil.durability<0:
            return print(f"Votre {self.name} est cassé")

        outil.use(50,20) # Utilise l'outil

        ressources=[]
        for ressource in place.ressources:
            nb=ressource["multiplier"]*outil.multiplier*self.multiplier
            ressources.append({"name":ressource["name"], "collect":nb})

        return ressources

    def addXp(self,nbXp):
                # On décompose la liste proprement
        lvl=self.experiance[0]
        xp=self.experiance[1]
        xpMax=self.experiance[2]

        xp+=nbXp # on ajoute l'xp gagné à l'xp du métier

        if xp>xpMax: # Si l'xp du métier dépasse l'xp max, alors on monte d'un niveau
            self.experiance=[lvl+1,xp-xpMax,xpMax*sqrt(2)] # On monte d'un niveau, on retire l'xp du niveau d'avant, et on change le nouveau xpMax
            print(f"Votre {self.name} viens de passer niveau {lvl}")



