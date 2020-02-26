countries = {
	'argentina': 43,
	'mexico': 122,
    'colombia': 49,
    'chile': 18,
    'peru': 31
}

while True:
	country = str(input('Put a country: ')).lower()

	try:
		print('The population in {} is: {}'.format(country, countries[country]))
	except KeyError:
		print("We don't have the population of {}".format(country))