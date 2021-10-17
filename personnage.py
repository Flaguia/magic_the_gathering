from Modules import places, Job, Tool, Interface
from random import choice

# places = {"nom":obj, "nom":obj,...}

class Personnage:
	def __init__(self, nom):
		self.nom = nom 

		self.vie = 100
		self.attaque = 15
		self.magie = 40
		self.mana = 400
		self.vitesse = 30

		namePlace, objPlace = choice(list(places.items())) # Récupère un lieu random
		self._place = (namePlace, objPlace) # Sauvegarde ce lieu sous forme de dictoinaire
		self._inventaire={"iRessouces":{}, "iWeapons":[], "iArmors":[],"iSpells":[], "iTools":{"Punch":Tool("Punch", 1)}}
		self.jobs={"Lumberjack":Job("Lumberjack"),
				"Mineur":Job("Mineur"),
				"Hunter":Job("Hunter"),
				"Fisherman":Job("Fisherman")
		}

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


test=Personnage("prout")
test.showInventaire()
test.moove()
test.work()

