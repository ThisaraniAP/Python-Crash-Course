# 10/07/2021
def city_country(city, country):
	"""Generate a neatly formatted location name."""
	formatted_location = f"{city}, {country}"
	return formatted_location

# 10/07/2021
def city_country_population(city, country, population=''):
	"""Generate a neatly formatted location name and population."""
	if population:
		formatted_location = f"{city}, {country} - population {population}"
	else:
		formatted_location = f"{city}, {country}"
	return formatted_location