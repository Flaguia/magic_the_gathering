
class Classe:

	def __init__(self, name):
		self.name = name

	def __str__(self):
		if self.name == "guerrier":
			return f'{self.name}'
		if self.name == "archer":
			return self.name
		if self.name == "mage":
			return self.name
		if self.name == "prêtre":
			return self.name
		if self.name == "voleur":
			return self.name

guerrier = Classe("guerrier")
archer = Classe("archer")
mage = Classe("mage")
prêtre = Classe("prêtre")
voleur = Classe("voleur")
guerrier = Classe("guerrier")
classe_choice = {"guerrier":guerrier,"archer":archer,"mage":mage, "prêtre":prêtre, "voleur":voleur}

