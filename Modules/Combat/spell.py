class Spell:

	def __init__(self, name,classe, damage, element, magic_penetration, boost_m, boost_a, boost_v, heal, pa):
		self.name = name
		self.damage = damage
		self.element = element
		self. magic_penetration = magic_penetration
		self.boost_m = boost_m
		self.boost_a = boost_a
		self.heal = heal
		self.boost_v = boost_v
		self.pa = pa

	def send(self):
		return self

	def __str__(self):
		return f'{self.name}, {self.damage}, {self.element}, {self.magic_penetration}, {self.boost_m}, {self.boost_a}, {self.boost_v}, {self.heal}, {self.pa}'


#spell voleur
poing = Spell("poing","", 10, "",0,0,0,0,0,1 )
coup_bas = Spell("coup bas ","voleur", 30, "ténebre",0,0,0,0,0, 5)
sort_trop_chere = Spell("sort_trop_chere", "voleur","lumière",0,0,0,0,0,0, 100000000)
