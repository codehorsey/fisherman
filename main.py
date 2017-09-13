from random import choice
weather = ['rain', 'shine']
fishies = ['redfish', 'nothing', 'nothing', 'nothing', 'trout', 'perch', 'perch', 'nothing', 'nothing']

choice(weather)

class Fisherman():

	def __init__(self):
		self.name = 'Freddy'
		self.gear = None
		self.bait = None
		self.location = None

	def fish(self):
		print 'Using {} and {}\n{} fishes.'.format(self.gear, self.bait, self.name)
		print '{} catches {}'.format(self.name, choice(fishies))

	def change_gear(newgear):
		pass

	def change_bait(newbait):
		pass

	def travel(destination):
		pass

man = Fisherman()
man.fish()