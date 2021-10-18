class Mob:

	def __init__(self, nom, éléments, vie, damage, magie, mana, vitesse, ability = []):
		self.nom = nom 
		self.éléments = éléments
		self.ability = ability
		self.vie = vie
		self.damage = damage
		self.magie = magie
		self.mana = mana
		self.vitesse = vitesse

	def __str__(self):
		return f'{self.nom}, élément: {self.éléments}, vie: {self.vie}, damage: {self.damage}, magie: {self.magie}, mana: {self.mana}, vitesse: {self.vitesse}, compétence: {self.ability}'

humain = Mob("humain", "lumière", 100000, 2, 0, 50, 15, [])
ange = Mob("ange", "lumière", 150, 15, 25, 100, 30, [])
squelette = Mob("squelette", "ténebre", 100, 15, 10, 30, 10, [])
zombie = Mob("zombie", "ténebre", 120, 20 ,0, 0, 10, [])
esprit = Mob("esprit", "eau", 50, 30, 50, 100, [])
Loutre_géante = Mob("Loutre Géante", "eau", 100, 75, 0, 0, 75, [])
blood_elf = Mob("elfe de sang", "plante", 50, 25, 100, 70, 70, [])
loup = Mob("loup", "plante", 100, 50, 0, 0, 50, [])
gobelin = Mob("gobelin", "feu", 25, 70, 0, 0, 100, [])
nain = Mob("nain", "feu", 50, 25, 30, 0, 20, [])


	