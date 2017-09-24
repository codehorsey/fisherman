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

def get_fish_value_or_location(data, values=True):
	''' returns {fish: int(value)} by default, {location: [fish]} with optional arg'''
	fishies = {}


	for location, fishlist in data.items():
		for fish in fishlist:
			logger.info('Current Fish: {}'.format(fish.split('|')[0]))
			if values: 
				print "Yes"
				fishname, fishvalue = get_fish_value(fish)
				fishies[fishname] = fishies.get(fishname, int(fishvalue))
			else: # return locations
				fishies[location] = fishies.get(location, [])
				fishies[location].append(fish.split('|')[0].strip())

	return fishies

data = read_data()

fishie_value_list = get_fish_value_or_location(data, True)
fish_and_locations = get_fish_value_or_location(data, False)
