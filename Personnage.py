from _typeshed import Self
from Modules import places, Job, Outil
from random import choice

class Personnage:
	def __init__(self, nom, inventaire_pve, vie, attaque, magie, mana, vitesse):
		self.nom = nom 
		#self.inventaire = list(inventaire)

		self.vie = vie
		self.attaque = attaque
		self.magie = magie
		self.mana = mana
		self.vitesse = vitesse
		
		self._jobs = {"Lumberjack":Job("Lumberjack")}
		punch=Outil("Punch")
		self._outils = {"Axe":punch}
		namePlace, objPlace = choice(list(places.items())) # Récupère un lieu random
		self._place = {namePlace, objPlace} # Sauvegarde ce lieu sous forme de dictoinaire
		

	def ajouter_inventaire(self, objet):
		
		self.inventaire.append(objet)

	def	get_inventaire(self):
			items = []
			for objet in self.inventaire:
				items.append((objet.nom, objet.quantité))
			return items

	def contient_objet(self,ustensile):
		for objet in self.inventaire:
			if ustensile == objet.nom:
				return True
			return False

	def jeter_objet(self, ustensile):
		if self.contient_ustensil(ustensile):
			i = 0
			for objet in self.contenu:
				if ustensile == objet.nom:
					self.contenu.pop(i)
				i=+1
					
		else: print("Ustensille non présent")

	def work(self):
		self.jobs[self._place.job].work(self.outils[self._place.outil], self._place)
		#TODO ajouter les ressources collectées

tess = Personnage("tess",[], 100, 15, 40, 400, 30)



print(tess.get_inventaire())