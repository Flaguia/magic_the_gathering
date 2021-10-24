from math import sqrt
from Modules.Interface import decimalRom

class Tool:
    def __init__(self,name, efficacite, durability=False,):
        self.name=name 
        self.durability=[durability,durability] # Durabilité actuelle, durabilité max
        self.multiplier=efficacite
        self._speed=1
        self._looting=1
        self.experiance=[1,0,100] # Le niveau, l'xp, l'xp max pour lvl up

    def __str__(self):
        chaine=f"{self.name} {decimalRom(self.experiance[0])}"
        if self.durability[1]!=False: # Si il a une durabilité
            chaine+=f" ({self.durability[0]}/{self.durability[1]})" # Alors on l'affiche
        return chaine

    def _addXp(self,nbXp):
        # On décompose la liste proprement
        lvl=self.experiance[0]
        xp=self.experiance[1]
        xpMax=self.experiance[2]

        xp+=nbXp # on ajoute l'xp gagné à l'xp de l'outil

        if xp>xpMax: # Si l'xp de l'outil dépasse l'xp max, alors on monte d'un niveau
            self.experiance=[lvl+1,xp-xpMax,xpMax*sqrt(2)] # On monte d'un niveau, on retire l'xp du niveau d'avant, et on change le nouveau xpMax
            print(f"Votre {self.name} viens de passer niveau {lvl}")

    def use(self,xp,damage): # Quand on uttilise l'outil, ça lui fait gagner des niveaux, et predre de la durabilité
        self._addXp(xp)
        if self.durability[1]!=False: # Si durabilité n'est pas False
            if self.durability[0]>0: # Si l'outil n'est pas deja cassé
                self.durability[0]-=damage
                if self.durability[0]<1:
                    self.durability[0]=0
                    print(f"Votre {self.name} s'est cassé")