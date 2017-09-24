"""Summary

Attributes:
    data (TYPE): Description
    fish_and_locations (TYPE): Description
    logger (TYPE): Description
"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_data(filename='locations.txt'):
	"""Gets locations, and fish with values
	
	Args:
	    filename (str, optional): File where location/fish are stored
	
	Returns:
	    DICT: Dictionary with this format {location: ['fish | value', 'fish....']}
	"""
	temp = {}
	catagorey = None
	with open(filename, 'r') as file:
		for line in file:
			logger.debug('Current Line: {}'.format(line))
			if line.startswith('!'):
				catagorey = line.strip().split('! ')[1]
				temp[catagorey] = []
			elif line.isspace():
				# line.startswith(' '): This did not work!?!?!?! Used isspace() instead
				catagorey = None
			else:
				if catagorey: 
					temp[catagorey].append(line.strip())
			logger.debug('Current Dict/Temp: {}'.format(temp))

	return temp

def get_fish_value(fish):
	"""Clean .txt data by stripping and separating fishname and value
	
	Args:
	    fish (data): Data from .txt in format fishname | fishvalue
	
	Returns:
	    str/int: Fishy, 20
	"""
	logger.debug('get_fish_value: {}'.format(fish))
	if fish:
		temp =  fish.split('|')
	
		fishname = temp[0].strip()
		fishvalue = temp[1].strip()
		return fishname, fishvalue
	else:
		pass

def get_list_of_fish_prices(data):
	"""Cleans data and gives values for all fishies
	
	Args:
	    data (DICT): Takes dictionary of fish lines and cleans data
	
	Returns:
	    DICT: A dictionary with fishname as lookup for values
	"""
	fish_values = {}

	for location, fishlist in data.items():
		for fish in fishlist:
			logger.info('Current Fish: {}'.format(fish.split('|')[0]))
			fishname, fishvalue = get_fish_value(fish)
			fish_values[fishname] = fish_values.get(fishname, int(fishvalue))

	return fish_values

def get_location_and_fishes(data):
	"""Take away value (Redundant, need to combine this and other function)
	
	Args:
	    data (TYPE): Description
	
	Returns:
	    TYPE: CLeaned diction with fish name and location
	"""
	cleaned_data = {}

	for location, fishlist in data.items():
		for fish in fishlist:
			cleaned_data[location] = cleaned_data.get(location, [])
			cleaned_data[location].append(fish.split('|')[0].strip())

	return cleaned_data

data = read_data()

fish_and_locations = get_location_and_fishes(data)
fishie_value_list = get_list_of_fish_prices(data)