class Spell:

	def __init__(self, name, damage, element,priorité, magic_penetration, boost_m, boost_a, boost_v, heal ):
		self.name = name
		self.damage = damage
		self.element = element
		self. magic_penetration = magic_penetration
		self.boost_m = boost_m
		self.boost_a = boost_a
		self.heal = heal
		self.boost_v = boost_v

	def send(self):
		output = (self.name, self.damage, self.element, self.magic_penetration, self.boost_m, self.boost_a, self.boost_v, self.heal) 
		return output

	def __str__(self):
		return f'{self.name}, {self.damage}, {self.element}, {self.magic_penetration}, {self.boost_m}, {self.boost_a}, {self.boost_v}, {self.heal}'


