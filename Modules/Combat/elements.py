from ./Personnage.py import Personnage

class elements:
	def __init__(self, elem):
		#on definie l'elelement du l'entité ou de l'attaque
		self.color = ["rouge","vert","bleu", "blanc", "noir"]
		x = 0

		for item in self.color:

			if item == elem:

				return self.elem = elem				
			x+=1
		self.x = x
		self.multiplier = 2 


	def chartre_dégat(self,other):
		#on vérifie si le defenseur est faible a l'element de l'attaque 
		if other.x < 4:
			if other.elem == color[1] and self.color==color[3]:
				return self.multiplier
			elif other.elem == color[x-1]:
				return self.multiplier
			else: return 1
		else:
			if other.elem == color[x]:
				return: 1
			else: return self.multiplier







