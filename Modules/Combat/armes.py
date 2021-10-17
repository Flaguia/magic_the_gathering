from math import sqrt
from classe import Classe_joueur
class Armes:
    def __init__(self,name,durability, damage, magic_damage, classe_equipable):
        self.name=name 
        self.durability=durability
        self.damage=damage
        self.experiance=[1,0,100] # Le niveau, l'xp, l'xp max pour lvl up
        self.magic_damage = magic_damage
        if classe_equipable == []:  # si la classe n'est pas spécifié l'arme est disponible pour tout le monde 
            for c in Classe_joueur.self.classe:
                classe_equipable.append(c)
        self.classe_equipable = classe_equipable

    def __str__(self):
        return f"{self.name}, niveau {self.experiance[0]} ({self.experiance[1]}/{self.experiance[2]}), durabilité: {self.durability}"

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
        self.durability-=damage
        if self.durability<0:
            print(f"Votre {self.name} s'est cassé")


        

    