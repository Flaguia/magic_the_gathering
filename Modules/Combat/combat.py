import os
from Modules import Interface
from math import ceil

def clear_screen(): 
    _ = os.system("cls" if os.name == "nt" else "clear") 

def strVie(init_vie):
    vie = "["
    r = ceil((100* (init_vie[0]/init_vie[1]))/5)
    for i in range(r):
        vie += "I"
    for i in range(20 - (len(vie)-1)):
        vie += "."
    vie += "]"
    return vie

def update_vie(init_vie_self, init_vie_mob):
    return [strVie(init_vie_self), strVie(init_vie_mob)]

def combatJoueur(joueur,mob):    
    clear_screen()
    print("un {} vous attaque".format(mob.nom))
    print("")
    
    init_vie_joueur = [joueur.vie, joueur.vie]
    init_vie_mob = [mob.vie, mob.vie]
    x=0
        
    while joueur.vie > 0 and mob.vie >0: #on effectue le combatr ju:squ'a que l'un des participants n'as plus de vie
            
        etat_précédent= {}
        liste_action = [joueur.arme]            #on selectionne toutes les actions pouvant êtres    entreprise 
        action_affichage = [joueur.arme.name]
        not_enough_mana = []
        for compétence in joueur.ability:
            if compétence.mana > joueur.mana:
                not_enough_mana.append(compétence)
            else:
                liste_action.append(compétence)
                action_affichage.append(compétence.name)

        for spell_trop_couteux in not_enough_mana:
            action_affichage.append(Interface.Choice(spell_trop_couteux.name, disabled= "sort trop couteux"))

        resKey = Interface.questionary.select( # Pose une question
            "qu'elle attaque voulez vous utiliser ?",
            choices=action_affichage    # Convertis mes objects en chaine de charactère
        ).ask()

        choix_attaque = resKey
        if x ==0:
            etat_précédent[1] =f'<b><white>dernière action :</white><yellow> {choix_attaque} </yellow></b>'
        
        compétence = {}     # On associe les réponse en string a nos objet respectuelle gràce à un dictionnaire
        for i in range(len(liste_action)):
            compétence['{}'.format(action_affichage[i])] = liste_action[i]

        choix_attaque= compétence[choix_attaque]

        if joueur.vitesse>mob.vitesse:
            mob.vie -= choix_attaque.damage

            init_vie_mob[0] = mob.vie
                       
            vie_mob = strVie(init_vie_mob)
            Interface.print_formatted_text(Interface.HTML(f'<b><green>{joueur.nom} inflige {choix_attaque.damage} dégat à {mob.nom}</green></b>'))
            Interface.print_formatted_text(Interface.HTML(f'<i><red>{mob.nom} pv restant : {vie_mob}</red></i>'))
            
            if x == 0:
                
                etat_précédent[2] =f'<b><green>{joueur.nom} inflige {choix_attaque.damage} dégat à {mob.nom}</green></b>'
                etat_précédent[3] =f'<i><red>{mob.nom} pv restant : {vie_mob} {mob.vie}</red></i>'
            

            if mob.vie <= 0:
                print("")
                Interface.print_formatted_text(Interface.HTML(f'<b><green>GG vous avez gagnée</green></b>'))
                break

            print("")

            joueur.vie -= mob.damage
            init_vie_joueur[0] = joueur.vie
            
            vie_personnage = strVie(init_vie_joueur)

            Interface.print_formatted_text(Interface.HTML(f'<b><red>{mob.nom} vous inflige {mob.damage} dégat à {joueur.nom}</red></b>'))
            Interface.print_formatted_text(Interface.HTML(f'<b><green>{joueur.nom} pv restant : {joueur.vie}</green></b>'))

            if x==0:
                etat_précédent[4] =f'<b><red>{mob.nom} vous inflige {mob.damage} dégat à {joueur.nom}</red></b>'
                etat_précédent[5] =f'<b><green>{joueur.nom} pv restant : {vie_personnage} {joueur.vie}</green></b>'
            
            if joueur.vie <= 0:
                print("")
                Interface.print_formatted_text(Interface.HTML(f'<b><purple>Domage vous avez perdu</purple></b>'))
                break 

        else: 
            joueur.vie -= mob.damage

            init_vie_joueur[0] = joueur.vie
            
            vie_mob = strVie(init_vie_mob)

            Interface.print_formatted_text(Interface.HTML(f'<b><red>{mob.nom} vous inflige {mob.damage} dégat à {joueur.nom}</red></b>'))
            Interface.print_formatted_text(Interface.HTML(f'<b><green>{joueur.nom} pv restant : {joueur.vie}</green></b>'))
            
            if x==0:
                etat_précédent[2] =f'<b><red>{mob.nom} vous inflige {mob.damage} dégat à {joueur.nom}</red></b>'
                etat_précédent[3] =f'<b><green>{joueur.nom} pv restant : {vie_personnage} {joueur.vie}</green></b>'
            
            if joueur.vie <= 0:
                print("")
                Interface.print_formatted_text(Interface.HTML(f'<b><purple>Domage vous avez perdu</purple></b>'))
                break 

            print("")
            mob.vie -= choix_attaque.damage

            init_vie_mob[0] = mob.vie           
            vie_mob = strVie(init_vie_mob)

            Interface.print_formatted_text(Interface.HTML(f'<b><green>{joueur.nom} inflige {choix_attaque.damage} dégat à {mob.nom}</green></b>'))
            Interface.print_formatted_text(Interface.HTML(f'<b><red>{mob.nom} pv restant : {vie_mob} {mob.vie}</red></b>'))

            if x==0:
                etat_précédent[4] = f'<b><red>{mob.nom} vous inflige {mob.damage} dégat à {joueur.nom}</red></b>'
                etat_précédent[5] =f'<b><green>{joueur.nom} pv restant : {vie_personnage} {joueur.vie}</green></b>'
                        
            if mob.vie <= 0:
                print("")
                Interface.print_formatted_text(Interface.HTML(f'<b><green>GG vous avez gagnée</green></b>'))
                break 
        clear_screen()
        
        for element in range(len(etat_précédent)):
            Interface.print_formatted_text(Interface.HTML(etat_précédent[element+1]))