from Modules import places, Job, Tool, Interface
from random import choice

# places = {"nom":obj, "nom":obj,...}


class Personnage:
	def __init__(self, nom, inventaire, vie, attaque, magie, mana, vitesse):
		self.nom = nom 

		self.vie = vie
		self.attaque = attaque
		self.magie = magie
		self.mana = mana
		self.vitesse = vitesse

		namePlace, objPlace = choice(list(places.items())) # Récupère un lieu random
		self._place = (namePlace, objPlace) # Sauvegarde ce lieu sous forme de dictoinaire
		self._inventaire={"iRessouces":[], "iWeapon":[], "iArmor":[],"iSpell":[]}
		self.jobs={"Lumberjack":Job("Lumberjack"),
				"Mineur":Job("Mineur"),
				"Hunter":Job("Hunter"),
				"Fisherman":Job("Fisherman")
		}
		self.tools={"Punch":Tool("Punch")}

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

