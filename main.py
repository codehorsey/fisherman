from numpy.random import choice 
import random
import sys
import time
from collections import Counter
from readtext import fishie_value_list as fish_values, fish_and_locations as fish_locations 
import logging

logging.basicConfig(level=50)
logger = logging.getLogger(__name__)
logger.setLevel(10)
# use diable to toggle debug mode
logging.disable(50)

class GameState():

	def __init__(self):
		self.weather = ['rain', 'shine']
		self.weather_weights = [.3, .7]
		self.day = 0
		self.history = {}

class Fisherman():

	def __init__(self):
		self.name = 'Freddy'
		self.gear = None
		self.bait = None
		self.location = 'Pond'
		self.inventory = []

		self.locations = fish_locations

		self.money = 0

		self.nothing_or_fish = ['nothing', 'fish']
		self.nothing_or_fish_weights = [.6, .4]

	def fish(self):
		fish = ''
		print "-" * 42
		print "Fisherman Casts..."
		ones_place = random.randrange(5)
		tenth_place = random.randrange(0,10)
		time_next_cast = str(ones_place) + '.' + str(tenth_place)
		time_next_cast = float(time_next_cast)
		logger.debug('Next cast in: {}'.format(time_next_cast/10))
		time.sleep(time_next_cast/100)
		fish_or_not = choice(self.nothing_or_fish, p=self.nothing_or_fish_weights)
		if fish_or_not == 'nothing':
			print "Nothing!"
			return fish_or_not
		else:
			fish = self.select_fish()
			print "Caught a {}".format(fish) 
			return fish

	def select_fish(self):
		fish_to_choose_from = self.locations[self.location]
		return random.choice(fish_to_choose_from)

	def change_gear(newgear):
		pass

	def change_bait(newbait):
		pass

	def travel(self, destination):
		if destination in self.locations.keys():
			print "Traveling to the {}".format(destination)
			self.location = destination
		else:
			print "Invalid desintation"

	def sell_fish(self, fish):
		return fish_values[fish]

def day_cycle(game, fisherman):
	man.nothing_or_fish_weights = [.3, .7]
	game.day += 1
	todays_weather = choice(game.weather, p=game.weather_weights)

	print "-" * 42
	print "Todays weather is {}.".format(todays_weather)
	print "Today is Day {}".format(game.day)
	print "Location: {}".format(man.location)
	
	if todays_weather == 'rain':
		fisherman.nothing_or_fish_weights = modify_weights(fisherman.nothing_or_fish_weights, [.3, -.3])
	
	# man fishes 200 times and appends results to fish_list
	fish_list = [man.fish() for _ in range(10)]
	logger.debug("Todays Catches: {}".format(Counter(fish_list)))
	day = 'Day {}'.format(game.day)
	game.history[day] = fish_list

	# this list includes 'nothing' catches so lets filter it out
	filtered_fish_list = filter(lambda x: x != 'nothing', fish_list)

	# Update inventory with filtered list (Taking out nothing)
	man.inventory.extend(filtered_fish_list)

	print "*" * 42
	print "Today's Catches! ({})".format(len(filtered_fish_list))
	print "*" * 42
	for k, v in (Counter(fish_list).items()):
		if k == 'nothing':
			continue
		else:
			print k, v
	print "*" * 42

	answer = raw_input('Do you want to sell your fish? ("y")')
	# answer = 'n'

	if answer.lower() == 'y':
		total = 0
		for fish in man.inventory[:]:
			total += man.sell_fish(fish)
			# man.money += man.sell_fish(fish)
			man.inventory.remove(fish)
		man.money += total
		print "Made {}".format(total)
		print 'Money: {}'.format(man.money)
	print "_" * 42

	# count inventory into dict.
	counted = Counter(man.inventory)
	
	print "Fish in inventory ({})".format(len(man.inventory))
	print "-" * 42
	for k,v in counted.items():
		print k, v
	print "-" * 42
	
	man.travel(random.choice(man.locations.keys()))

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
	if game.day == 5:
		break
	print "~" * 42
	raw_input('Next Day')
	print(chr(27) + "[2J")
