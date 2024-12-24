# 01/06/2021
rome_info = {
	'country': 'italy', 
	'population': '2.9M', 
	'fact': 'It is the capital of Italy.', 
}

delhi_info = {
	'country': 'india', 
	'population': '30M', 
	'fact': 'It is home to all three branches of the Government of India.', 
}

colombo_info = {
	'country': 'sri lanka', 
	'population': '613K', 
	'fact': 'It is the commerial capital of Sri Lanka.', 
}


cities = {
	'rome': rome_info, 
	'delhi': delhi_info, 
	'colombo': colombo_info, 
}



for city, info in cities.items():
	print (f"\nCity: \t\t{city.title()}")
	print (f"Country: \t{info['country'].title()}")
	print (f"Population: {info['population']}")
	print (f"Fact: \t\t{info['fact']}")