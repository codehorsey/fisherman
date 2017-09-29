class Fish():
	def __init__(self, name, value, rarity='common'):
		self.name = name
		self.value = value
		self.rarity = rarity

class Location():

	def __init__(self, name):
		self.name = name
		self.fishlist = []

class Weather():

	def __init__(self, name, values):
		self.name = name
		self.values = values

class Fisherman():
	def __init__(self, name):
		self.name = "Freddy"
		self.gear = None
		self.bait = None
		self.inventory = []
		self.money = 0


def fish_today(location, weather, fishies, fisherman):
	random.choice(location.fishies)



from readtext import fish_and_locations, fishie_value_list


def main():
	locations = []
	for location, fishes in fish_and_locations.items():
		'''Create location object with fishies stored as a list'''
		new_location = Location(location)

		for fish in fishes:
			'''Add a new fish object with name, value, rarity'''
			new_location.fishlist.append(Fish(fish, fishie_value_list[fish][0], fishie_value_list[fish][1]))

		locations.append(new_location)

	import random

	perfect = Weather('Perfect', [.9, .1])
	sunny = Weather('Sunny', [.7, .3])
	rainy = Weather('Rainy', [.3, .7])
	cloudy = Weather('Cloudy', [.5, .5])
	windy = Weather('Windy', [.4, .6])

	from numpy.random import choice 

	def gofishing(location, weather):
		fish_or_not = [True, False]
		fish_or_not_weights = weather.values
		rarity = ['common', 'uncommon', 'rare']
		rarity_weights = [.7, .2, .1]

		if choice(fish_or_not, p=fish_or_not_weights):
			rare_roll = choice(rarity, p=rarity_weights)
			fish_in_location_with_rare_roll =  filter(lambda x: x.rarity == rare_roll, location.fishlist)
			
			# caught_fish = random.choice(location.fishlist) # random fish in location
			caught_fish = random.choice(fish_in_location_with_rare_roll) # random fish of rarity

			# print location.name
			print caught_fish.name, caught_fish.value, caught_fish.rarity
		else:
			print 'no fish'

	todays_weather = perfect

	for _ in range(10):
		gofishing(locations[0], todays_weather)

	# import random
	# a = random.choice(locations)
	# go(a)

if __name__ == "__main__":
	main()
