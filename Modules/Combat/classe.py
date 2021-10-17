class Classe_joueur:

	def __init__(self, classe_choisi):
		self.classe = ["guerrier","archer","mage", "prêtre", "voleur"]
		x = 0

		for item in self.classe:

			if item == classe_choisi:

				return self.classe_choisi = item				
			x+=1
		self.x = x
		self.multiplier = 2 