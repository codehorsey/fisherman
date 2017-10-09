import random
from numpy.random import choice 
from collections import Counter
from readtext import fish_and_locations, fishie_value_list
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logging.disable(0)

class Game():
	def __init__(self):
		self.day = 0
		self.fish_history = {}
		self.weather_history = {}
		self.location_history = {}

class Fish():
	def __init__(self, name, value, rarity='common'):
		self.name = name
		self.value = value
		self.rarity = rarity

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

class Location():
	def __init__(self, name):
		self.name = name
		self.fishlist = []

class Weather():
	def __init__(self, name, values):
		self.name = name
		self.values = values

class Fisherman():
	def __init__(self, name='Freddy'):
		self.name = name
		self.gear = None
		self.bait = None
		self.todays_catches = []
		self.inventory = []
		self.money = 0

def populate_location_objects():
	'''return a list that contains location objects that contain fish objects'''
	locations = []
	logging.info('Populating location objects')
	for location, fishes in fish_and_locations.items():
		'''Create location object with fishies stored as a list'''
		logging.debug('Location: {}\nFishies: {}'.format(location, fishes))
		new_location = Location(location)

		for fish in fishes:
			'''Add a new fish object with name, value, rarity'''
			new_location.fishlist.append(Fish(fish, fishie_value_list[fish][0], fishie_value_list[fish][1]))

		locations.append(new_location)

	return locations

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
		logger.debug('\n\tRarity Roll: {}\n\tFish Name: {}\n\tFish Value: {}\n\tFish Rarity: {}'.format(rare_roll, caught_fish.name, caught_fish.value, caught_fish.rarity))

		# print caught_fish.name, caught_fish.value, caught_fish.rarity
		return caught_fish
	else:
		# caught_nothing = Fish('nothing', 0, None)
		caught_nothing = None
		return caught_nothing

def populate_weather_objects(filename):
	'''return object of weathers'''
	logging.info('Populating weather objects')
	weather_list = []
	with open('weathers.txt', 'r') as f:
		for line in f:
			weather_name, weather_weights = line.split('|')
			# clean white space
			weather_name = weather_name.strip()
			weather_weights = weather_weights.strip()
			# format weights for python. Add []'s and , for [#, #] format'
			# do this by splitting! :) :)
			weather_weights = weather_weights.split(' ')
			weather_weights = [float(weight) for weight in weather_weights]
			logging.debug('Weather Type: {}\tWeather Weights: {}'.format(weather_name, weather_weights))
			weather_list.append(Weather(weather_name, weather_weights))

	return weather_list


def fishing_simulation(weather, location):
	todays_catches = []
	# Fish 10 times
	logging.info('Fishing Simulation Started')
	logger.info('Fishing at {} in {} weather.'.format(location.name, weather.name))
	for _ in range(10):
		todays_catches.append(gofishing(location, weather))
	logger.info('Fishing Done.')

	return todays_catches


def main():
	# Using game to store history of daily catches for data tracking and graphing later
	game = Game()
	fisher = Fisherman()
	locations = populate_location_objects()
	weathers = populate_weather_objects('weathers.txt')

	todays_weather = random.choice(weathers)
	todays_location = random.choice(locations)
	todays_catches = fishing_simulation(todays_weather, todays_location)

	# redundant but will be used later to maybe graph toays catches or display
	fisher.todays_catches = filter(None, todays_catches)
	for fish in fisher.todays_catches:
		fisher.inventory.append(fish)

	logger.debug("Todays Catches: {}".format(Counter(fisher.todays_catches)))
	day = 'Day {}'.format(game.day)
	game.fish_history[day] = todays_catches
	game.weather_history[day] = todays_weather 
	game.location_history[day] = todays_location 


if __name__ == "__main__":
	main()
