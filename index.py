from personnage import Personnage
from Modules import mob, combatJoueur, spell, Interface


perso=Personnage("a", ability=[spell.coup_bas, spell.sort_trop_chere])

#combatJoueur(perso,mob.humain)
while True:
    action = Interface.questionary.select( # Affiche les choix
    "Que veut-tu faire ?",
        choices=[
            "craft",
            "moove",
            "work",
            "showInventaire"
        ]
    ).ask()
    eval("perso."+action+"()")
