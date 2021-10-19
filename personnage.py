import os, sys, random
sys.path.insert(0, "./Modules/Interface")

from Modules import places, Job, Tool, Interface, classe_Joueur, mob, spell

def clear_screen(): 
	_ = os.system("cls" if os.name == "nt" else "clear") 


class Personnage:
	def __init__(self, nom, classe="",arme=spell.poing, ability = []):
		self.nom = nom 
		self.classe = classe
		self.arme = arme
		self.vie = 100
		self.attaque = 15
		self.magie = 40
		self.mana = 400
		self.vitesse = 30
		self.ability = ability

		namePlace, objPlace = random.choice(list(places.items())) # Récupère un lieu random
		self._place = (namePlace, objPlace) # Sauvegarde ce lieu sous forme de dictoinaire
		self._inventaire={"iRessouces":{}, "iWeapons":[], "iArmors":[],"iSpells":[], "iTools":{"Punch":Tool("Punch", 1)}}
		self.jobs={"Lumberjack":Job("Lumberjack"),
				"Mineur":Job("Mineur"),
				"Hunter":Job("Hunter"),
				"Fisherman":Job("Fisherman")
		}
	def class_choice(self):
		liste_classe = []
		for key in classe_Joueur.classe_choice:
			 liste_classe.append(key)

		resKey = Interface.questionary.select( # Pose une question
			"qu'elle classe choisissez vous ?",
			choices=list(map(str,liste_classe )) # Convertis mes objects en chaine de charactère
		).ask()
		self.classe = resKey
		
	def __str__(self):
		capacité = []
		for comp in self.ability:
			capacité.append(comp.name)
		return f'{self.nom}, classe: {self.classe}, vie: {self.vie}, attaque: {self.attaque}, dégat magique: {self.magie}, mana: {self.mana}, vitesse: {self.vitesse}, liste des compétences: {capacité}'
	def work(self):

		#TODO Fix le bug de l'xp de l'outil
		job=self.jobs[self._place[1].job]

		try:
			tool=self._inventaire["iTools"][self._place[1].tool] # Essaye de récuperer l'outil
		except: # Si l'outil n'est pas trouvé
			try:
				tool=self._inventaire["iWeapons"][self._place[1].tool] # On le cherche dans les armes
			except:
				tool=self._inventaire["iTools"]["Punch"] # On uttilise le poing

		ressources=job.work(tool, self._place[1]) # Récupère les ressources 

		# Rajout des ressources dans l'inventaire
		for key in ressources.keys():
			try: self._inventaire["iRessouces"][key]+=ressources[key] # On esssaye d'ajouter le nombre d'elements recupéré dans la ressource deja existante
			except: self._inventaire["iRessouces"][key]=ressources[key] # On creer la ressource dans l'inventaire avec son nombre d'element
		 
		# Affiche les ressources collectées
		invRessources=""
		if ressources:
			for key, value in ressources.items():
				invRessources+=f"<i>{key}</i>: <orange>{value}</orange>\n"
		else: invRessources="<red>Vous n'avez rien récupéré durant votre travail !</red>"
		Interface.print_formatted_text(Interface.HTML(
			f'<b><green>--- Ressources Récoltées ---</green></b>\n{invRessources}'
		))
		

	def moove(self):
		choicesPlaces=self._place[1].moovePossibles # Récup les mouvements possibles a partir de ce lieu
		resKey = Interface.questionary.select( # Pose une question
			"Ou voulez-vous aller ?",
			choices=list(map(str, choicesPlaces)) # Convertis mes objects en chaine de charactère
		).ask()

		self._place=(resKey,places[resKey]) # Sauvegarde la nouvelle place ("nom", obj)
		Interface.print_formatted_text(Interface.HTML(f'Vous vennez de bouger vers : <b>{resKey}</b>'))


	def showInventaire(self):
		invRessources=""
		if self._inventaire["iRessouces"]:
			for key, value in self._inventaire["iRessouces"].items():
				invRessources+=f"<i>{key}</i>: <orange>{value}</orange>\n"
		else: invRessources="<red>Vous n'avez aucunes ressources pour le moment !</red>"

		invTools=""
		for key, value in self._inventaire["iTools"].items():
			invTools+=f"<i>{key}</i>: <orange>{str(value)}</orange>\n"

		Interface.print_formatted_text(Interface.HTML(f'<b><green>--- Ressources ---</green></b>\n{invRessources}\n<b><green>--- Outils ---</green></b>\n{invTools}\n'))
	def update_vie(self, init_vie_self, init_vie_mob):
		len_barre_vie = 20
		
		vie_perso = "["

		r = ((100* round(init_vie_self[0]/init_vie_self[1]))/5)
		for i in range(r):
			vie_perso += "I"
		for i in range(len_barre_vie - (len(vie_perso)-1)):
			vie_perso += "."
		vie_perso += "]"

		vie_mob = "["

		r= (100* round(init_vie_mob[0]/init_vie_mob[1])/5)
		for i in range(r):
			vie_mob += "I"
		for i in range(len_barre_vie - (len(vie_mob)-1)):
			vie_mob += "."
		vie_mob += "]"
		liste_vie = [vie_perso, vie_mob]
		return liste_vie

	def combat_Joueur(self, Mob):
		clear_screen()
		print("un {} vous attaque".format(mob.humain.nom))
		print("")
		

		init_vie_self = [self.vie, self.vie]
		init_vie_mob = [Mob.vie, Mob.vie]
		

		



		x=0
		
		while self.vie > 0 and Mob.vie >0: #on effectue le combatr ju:squ'a que l'un des participants n'as plus de vie
			
			etat_précédent= {}
			liste_action = [self.arme]      #on selectionne toutes les actions pouvant êtres  entreprise 
			action_affichage = [self.arme.name]
			not_enough_mana = []
			for compétence in self.ability:

				if compétence.mana > self.mana:
					not_enough_mana.append(compétence)
				else:
					liste_action.append(compétence)
					action_affichage.append(compétence.name)
			for spell_trop_couteux in not_enough_mana:
				action_affichage.append(Interface.Choice(spell_trop_couteux.name, disabled= "sort trop couteux"))
			resKey = Interface.questionary.select( # Pose une question
				"qu'elle attaque voulez vous utiliser ?",
				choices=action_affichage  # Convertis mes objects en chaine de charactère
			).ask()
			choix_attaque = resKey
			if x ==0:
				etat_précédent[1] =f'<b><white>dernière action :</white><yellow> {choix_attaque} </yellow></b>'
			


			compétence = {}   #on associe les réponse en string a nos objet respectuelle gràce à un dictionnaire
			for i in range(len(liste_action)):
				compétence['{}'.format(action_affichage[i])] = liste_action[i]

			choix_attaque= compétence[choix_attaque]

			if self.vitesse>Mob.vitesse:
				Mob.vie -= choix_attaque.damage

				init_vie_mob[0] = Mob.vie
				
				vie_mob = self.update_vie(init_vie_self, init_vie_mob)
				
				vie_mob = vie_mob[1]

				Interface.print_formatted_text(Interface.HTML(f'<b><green>{self.nom} inflige {choix_attaque.damage} dégat à {Mob.nom}</green></b>'))
				Interface.print_formatted_text(Interface.HTML(f'<i><red>{Mob.nom} pv restant : {vie_mob}</red></i>'))
				
				if x == 0:
					
					etat_précédent[2] =f'<b><green>{self.nom} inflige {choix_attaque.damage} dégat à {Mob.nom}</green></b>'
					etat_précédent[3] =f'<i><red>{Mob.nom} pv restant : {vie_mob} {Mob.vie}</red></i>'
				

				if Mob.vie <= 0:
					print("")
					Interface.print_formatted_text(Interface.HTML(f'<b><green>GG vous avez gagnée</green></b>'))
					break 

				
				print("")

				self.vie -= Mob.damage
				init_vie_self[0] = self.vie
				vie_personnage = self.update_vie(init_vie_self, init_vie_mob)
				
				vie_personnage = vie_personnage[0]

				Interface.print_formatted_text(Interface.HTML(f'<b><red>{Mob.nom} vous inflige {Mob.damage} dégat à {self.nom}</red></b>'))
				Interface.print_formatted_text(Interface.HTML(f'<b><green>{self.nom} pv restant : {self.vie}</green></b>'))

				if x==0:
					etat_précédent[4] =f'<b><red>{Mob.nom} vous inflige {Mob.damage} dégat à {self.nom}</red></b>'
					etat_précédent[5] =f'<b><green>{self.nom} pv restant : {vie_personnage} {self.vie}</green></b>'
				


				if self.vie <= 0:
					print("")
					Interface.print_formatted_text(Interface.HTML(f'<b><purple>Domage vous avez perdu</purple></b>'))
					break 
			else : 
				self.vie -= Mob.damage

				init_vie_self[0] = self.vie
				vie_mob = self.update_vie(init_vie_self, init_vie_mob)
				
				vie_mob = vie_mob[1]

				Interface.print_formatted_text(Interface.HTML(f'<b><red>{Mob.nom} vous inflige {Mob.damage} dégat à {self.nom}</red></b>'))
				Interface.print_formatted_text(Interface.HTML(f'<b><green>{self.nom} pv restant : {self.vie}</green></b>'))
				

				if x==0:
					etat_précédent[2] =f'<b><red>{Mob.nom} vous inflige {Mob.damage} dégat à {self.nom}</red></b>'
					etat_précédent[3] =f'<b><green>{self.nom} pv restant : {vie_personnage} {self.vie}</green></b>'
				

				if self.vie <= 0:
					print("")
					Interface.print_formatted_text(Interface.HTML(f'<b><purple>Domage vous avez perdu</purple></b>'))
					break 

				print("")
				Mob.vie -= choix_attaque.damage

				init_vie_mob[0] = Mob.vie
				
				vie_mob = self.update_vie(init_vie_self, init_vie_mob)
				
				vie_mob = vie_mob[1]

				Interface.print_formatted_text(Interface.HTML(f'<b><green>{self.nom} inflige {choix_attaque.damage} dégat à {Mob.nom}</green></b>'))
				Interface.print_formatted_text(Interface.HTML(f'<b><red>{Mob.nom} pv restant : {vie_mob} {Mob.vie}</red></b>'))

				if x==0:
					etat_précédent[4] = f'<b><red>{Mob.nom} vous inflige {Mob.damage} dégat à {self.nom}</red></b>'
					etat_précédent[5] =f'<b><green>{self.nom} pv restant : {vie_personnage} {self.vie}</green></b>'
				
			
				if Mob.vie <= 0:
					print("")
					Interface.print_formatted_text(Interface.HTML(f'<b><green>GG vous avez gagnée</green></b>'))
					break 
			clear_screen()
			
			for element in range(len(etat_précédent)):
				Interface.print_formatted_text(Interface.HTML(etat_précédent[element+1]))
				
