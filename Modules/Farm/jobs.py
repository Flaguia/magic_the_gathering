# Le metier doit être unique à chaque personage

# Pour acceder à prompt_toolkit
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
#-- 

from math import sqrt
from Modules import Interface
import time, random, signal

class Job:
    def __init__(self, name):
        self.name=name
        self._experiance=[1,0,100] # Le niveau, l'xp, l'xp max pour lvl up
        self._speed=1
        self._looting=1
        
    def work(self,tool, place):
        if tool.durability<0:
            return print(f"Votre {self.name} est cassé")

        self.addXp(50) # Fait gagner de l'experiance de travail

        tool.use(50,20) # Utilise l'outil
        
        collectedRessources={} # Un dictionnaire des ressources collectées: {"cobble":3,"wood":10,...}
        if place.ressources!=[]: # Verrifie qu'il y ai des ressources a recup

            weights=[]
            for ressource in place.ressources: # Récupère le poid de chaque ressources
                weights.append(1/ressource["rarity"]*10) # Plus c'est rare, plus le poid est petit. *10 pour augmenter le poid (sinon c'etais vraiment trop rare)

            nbToClame=random.randint(2,5)*self._looting*tool._looting # Calcul du nombres de ressources a recuperer (en fonction du niveau du metier et de l'outil)
            ressourcesToClame = random.choices(place.ressources, weights=weights, k=nbToClame) # Choisit aléatoirement des ressources (en fonction de leur poid)
            random.shuffle(ressourcesToClame) # On mélange un peut la liste pour ne pas miner pleins de fois la même chose d'affiler.
            
            # Calcul du temps total qu'il va  mettre a miner (Pour l'affichage)
            timeToAllBreak=0
            for ressource in ressourcesToClame:
                timeToAllBreak+=ressource["timeToBreak"]*1-(self._speed/100)*1-(tool._speed/100)
            
            # Affiche la barre de progression
            # Il faut une boucle de temps, qui se repète toutes les 0.1s pour affichier proprement l'avancement du temps
            # Mais il faut récolter les ressources qu'a un certain temps
            # Exemple: Il va mettre 80s a tout recolter, et il va recolter de la pierre à la 3ème seconde et du charbon à la 3ème + 5ème seconde
            # Donc il faut un indice i qui va se repeter timeToAllBreak/0.1
            # Et un indice j qui va augmenter a chaque récolte de ressource

            ### Pour l'affichage de la barre de progression ###
            kb = Interface.KeyBindings()
            cancel = [False]
            @kb.add('x') # Le racourci clavier
            def _(event):
                " Send Abort (control-c) signal. "
                cancel[0] = True

            titleOfProgressBar = Interface.HTML('Travail en cour...')
            bottom_toolbar = Interface.HTML('Appuyez sur <b>[x]</b> pour arrêter maintenant.')
            custom_formatters = [
                Interface.formatters.Text('['),
                Interface.formatters.Percentage(),
                Interface.formatters.Text('] '),
                Interface.formatters.Bar(),
                Interface.formatters.Text('['),
                Interface.formatters.TimeLeft(),
                Interface.formatters.Text(']'),
                ]
            ####################################################

            timeStop=0 # Le nombre de 0.1s avant de passer a la ressource suivante
            j=0
            with Interface.ProgressBar(title=titleOfProgressBar,formatters=custom_formatters, bottom_toolbar=bottom_toolbar, key_bindings=kb) as pb:
                for i in pb(range(int(timeToAllBreak/0.1))): # Boucle sur le temps pour tout casser *0.1, la boucle se repète toutes les 0.1s
                    # TODO retirer l'object dans la place
                    if i == ressourcesToClame[j]["timeToBreak"]/0.1+timeStop: # Si le temps == nombre de 0.1s qu'a besoin la ressource a casser + le temps des anciennes ressources
                        try: collectedRessources[ressourcesToClame[j]["name"]]+=1 # On essaye de rajouter 1 a la ressource dans le dictionnaire 
                        except: collectedRessources[ressourcesToClame[j]["name"]]=1 # Si on y arrive pas, c'est qu'elle existe pas, alors on la créé
                        timeStop+=ressourcesToClame[j]["timeToBreak"]/0.1 # On calcule le nouveau total de temps
                        j+=1 # O, change l'indice des ressources
                    time.sleep(0.1) # la boucle se repète toutes les 0.1s

                    # Arrete si l'utilisateur a pressé x
                    if cancel[0]:
                        break

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
