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
		self._inventaire={"iRessouces":[], "iWeapons":[], "iArmors":[],"iSpells":[], "iTools":{"Punch":Tool("Punch", 1)}}
		self.jobs={"Lumberjack":Job("Lumberjack"),
				"Mineur":Job("Mineur"),
				"Hunter":Job("Hunter"),
				"Fisherman":Job("Fisherman")
		}

	def work(self):
		job=self.jobs[self._place[1].job]

		try:
			tool=self._inventaire["iTools"][self._place[1].tool] # Essaye de récuperer l'outil
		except: # Si l'outil n'est pas trouvé
			try:
				tool=self._inventaire["iWeapons"][self._place[1].tool] # On le cherche dans les armes
			except:
				tool=self._inventaire["iTools"]["Punch"] # On uttilise le poing

		ressources=job.work(tool, self._place[1])
		print(ressources)
		self._inventaire["iRessouces"].append(ressources)

	def moove(self):
		choicesPlaces=self._place[1].moovePossibles # Récup les mouvements possibles a partir de ce lieu
		answers = Interface.prompt({ # Pose la questions
			'type': 'list',
			'name': 'user_option',
			'message': 'Ou voulez-vous aller ?',
			'choices': list(map(str, choicesPlaces)) # Convertis mes objects en chaine de charactère
    	})
		resKey=answers.get("user_option") # Récupère la réponse de la question spécifique
		self._place=(resKey,places[resKey]) # Sauvegarde la nouvelle place ("nom", obj)
		print("Vous vennez de bouger vers :", resKey)

test=Personnage("coucou")

test.work()
