from numpy.random import choice 
from collections import Counter


class GameState():

	def __init__(self):
		self.weather = ['rain', 'shine']
		self.weather_weights = [.3, .7]
		self.day = 0

class Fisherman():

	def __init__(self):
		self.name = 'Freddy'
		self.gear = None
		self.bait = None
		self.location = 'pond'
		self.inventory = []
		self.history = {}
		self.inventory2 = []

		self.locations = {'pond':['bass', 'carp', 'catfish'],
						'beach':['trout', 'hardhead','redfish']
		}

		self.money = 0

		self.nothing_or_fish = ['nothing', 'fish']
		self.nothing_or_fish_weights = [.6, .4]

	def fish(self):
		fish_or_not = choice(self.nothing_or_fish, p=self.nothing_or_fish_weights)
		if fish_or_not == 'nothing':
			return fish_or_not
		else:
			# Hooked a fish, but what kind!?
			# Based on location - give different types of fish
			self.select_fish
			return 'FISH'


	def select_fish(self):
		fish_to_choose_from = self.locations[self.location]
		print fish_to_choose_from

	def change_gear(newgear):
		pass

	def change_bait(newbait):
		pass

	def travel(destination):
		pass

	def sell_fish(self, fish):
		shop_prices = {'fish': 2, 'redfish': 20}
		return shop_prices[fish]

def day_cycle(game, fisherman):
	man.nothing_or_fish_weights = [.3, .7]
	game.day += 1
	tweather = choice(game.weather, p=game.weather_weights)

	print "Todays weather is {}.".format(tweather)
	print "Today is Day {}".format(game.day)
	if tweather == 'rain':
		fisherman.nothing_or_fish_weights = modify_weights(fisherman.nothing_or_fish_weights, [.3, -.3])
	
	# man fishes 200 times and appends results to l
	l = [man.fish() for _ in range(200)]
	day_results = l
	day = 'Day {}'.format(game.day)
	man.history[day] = day_results
	# this list includes 'nothing' catches so lets filter it out
	filtered_l = filter(lambda x: x != 'nothing', l)

	# Update inventory with filtered list (Taking out nothing)
	man.inventory.append(filtered_l)
	man.inventory2.extend(filtered_l)

	print "Todays Summary: {}".format(Counter(l))

	answer = raw_input('Do you want to sell your fish?')
	if answer.lower() != 'n':
		for fish in man.inventory2[:]:
			man.money += man.sell_fish(fish)
			man.inventory2.remove(fish)
			print 'Money: {}'.format(man.money)



def modify_weights(weights, modified_weights):
	new_weights = []
	for n in zip(weights, modified_weights):
		new_weights.append(sum(n))

	return new_weights

man = Fisherman()
man.fish()
game = GameState()

while True:

	day_cycle(game, man)
	if game.day == 10:
		break







# print Counter(sum(man.inventory, []))
# print man.inventory2
# print len(man.inventory2)
# print Counter(man.inventory2)

print len(man.history['Day 1'])