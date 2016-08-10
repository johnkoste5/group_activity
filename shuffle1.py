class player(object):
	"""docstring for ClassName"""
	def __init__(self, name, hand):
		self.name = name
		self.hand = 5
class cards(object):
	def __init__(self, card, suits):
		self.card = [1,2,3,4,5,6,7,8,9,10,"J", "Q", "K", "A"]
		self.suits = ["H", "D", "C", "S"]

		