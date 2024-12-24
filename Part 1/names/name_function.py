# 08/07/2021
def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = f"{first} {last}"
	return full_name.title()

# 09/07/2021
def get_formatted_name_1(first, middle, last):
	"""Generate a neatly formatted full name."""
	full_name = f"{first} {middle} {last}"
	return full_name.title()


# 10/07/2021
# An improved version of the previous function.
def get_formatted_name_2(first, last, middle=''):
	"""Generate a neatly formatted full name."""
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()