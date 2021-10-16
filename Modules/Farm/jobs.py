# Le metier doit être unique à chaque personage

# Pour acceder à prompt_toolkit
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
#-- 

#from Interface import ProgressBar

from math import sqrt
import time, random

class Job:
    def __init__(self, name):
        self.name=name
        self._experiance=[1,0,100] # Le niveau, l'xp, l'xp max pour lvl up
        self._speed=1
        self._looting=1
        
    def work(self,tool, place):
        self.addXp(50)
        if tool.durability<0:
            return print(f"Votre {self.name} est cassé")

        tool.use(50,20) # Utilise l'outil
        
        ressourcesNames=[]
        weights=[]
        for ressource in place.ressources: # Pour chaque ressources
            ressourcesNames.append(ressource["name"])
            weights.append(1/ressource["rarity"]*10) # Plus c'est rare,  plus le poid est petit. *10 pour augmenter le poid (sinon c'etais vraiment trop rare)

        print(ressourcesNames)
        collectedRessources={} # Un dictionnaire des ressources collectées: {"cobble":3,"wood":10,...}
        if ressourcesNames!=[]: # Verrifie qu'il y ai des ressources a recup
            ressourcesToClame = random.choices(ressourcesNames, weights=weights, k=len(ressourcesNames))
            random.shuffle(ressourcesToClame) # On mélange un peut la liste pour ne pas miner que la même chose d'affiler.
            
            timeToAllBreak=0
            timeToAllBreak+=(ressource["timeToBreak"]*1-(self._speed/100)*1-(tool._speed/100))

            print("Temps de travail:", len(place.ressources)) # TODO faire une bar de progression
            for r in ressourcesToClame: # Pour chaque ressource dans la liste des ressource a récuperer
                for i in range(len(place.ressources)): 
                    if place.ressources[i]["name"]==r: # Récupère le dictionaire de la ressource (dans l'object Place)
                        ressource=place.ressources[i] # Pour pas avoir le long nom a se trainer..
                        ressource['stock']-=1 # On retire dans l'e stock de l'object place
                        try: collectedRessources[r]+=1 # On essaye de rajouter 1 a la ressource dans le dictionnaire 
                        except: collectedRessources[r]=1 # Si on y arrive pas, c'est qu'il existe pas, alors on le créé
                        break
                time.sleep(1)
        
        return collectedRessources



    def addXp(self,nbXp):
        # On décompose la liste proprement
        lvl=self._experiance[0]
        xp=self._experiance[1]
        xpMax=self._experiance[2]

        xp+=nbXp # on ajoute l'xp gagné à l'xp du métier

        if xp>xpMax: # Si l'xp du métier dépasse l'xp max, alors on monte d'un niveau
            self._experiance=[lvl+1,xp-xpMax,xpMax*sqrt(2)] # On monte d'un niveau, on retire l'xp du niveau d'avant, et on change le nouveau xpMax
            self._speed+=1
            self._looting+=1
            print(f"Votre {self.name} viens de passer niveau {lvl}")



