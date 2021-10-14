from Modules import places, Job, Outil
from random import randint

class Personnage:
	def __init__(self, nom, inventaire_pve, vie, attaque, magie, mana, vitesse):
		self.nom = nom 
		self.inventaire = list(inventaire)

		self.vie = vie
		self.attaque = attaque
		self.magie = magie
		self.mana = mana
		self.vitesse = vitesse

		self._place=places[randint(0,len(places-1))] # Un object place #TODO (Faire spawn dans un lieu random)
        self._jobs={"Lumberjack":Job("Lumberjack")}
        self._outils={"Axe":Outil("Axe")}
    

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
        ressourcesCollected=self.addRessources()
        print(ressourcesCollected)

tess = Personnage("tess",[], 100, 15, 40, 400, 30)



print(tess.get_inventaire())