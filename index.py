from personnage import Personnage
from Modules import mob, combatJoueur, spell

perso=Personnage("a", ability=[spell.coup_bas, spell.sort_trop_chere])
perso.work()
#combatJoueur(perso,mob.humain)

