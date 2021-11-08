from personnage import Personnage
from Modules import mob, combatJoueur, spell, Interface
from random import randint

perso=Personnage("a", ability=[spell.coup_bas, spell.sort_trop_chere])

#combatJoueur(perso,mob.humain)
while True:
    action = Interface.questionary.select( # Affiche les choix
    "Que veut-tu faire ?",
        choices=[
            "craft",
            "moove",
            "work",
            "showInventaire",
            "fight",
        ]
    ).ask()
    if action == "fight": #si l'action choisit est le combat 
        pla = perso.returnPlace() 
        mobpla = eval("mob.mob"+pla.name) #on récupère la liste des mob pouvant apparaitre dans un lieux donnné 
        mobToFight = randint(0,len(mobpla)-1)  #selection d'un mob aléatoire parmis la liste 
        combatJoueur(perso, mobpla[mobToFight]) #on lance le combat 
        continue 
        

    eval("perso."+action+"()") #pour une action différente nous utilisons par défaut cet option
