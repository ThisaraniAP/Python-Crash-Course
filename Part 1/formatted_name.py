# 10/06/2021
# return the full formatted name
def get_formatted_name(first_name, last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print (musician)

# you might need a middle name argument
def get_formatted_name_2(first_name_2, middle_name_2, last_name_2):
	full_name_2 = f"{first_name_2} {middle_name_2} {last_name_2}"
	return full_name_2.title()

musician_2 = get_formatted_name_2('jimi', 'lee', 'hendrix')
print (musician_2)

# but the middle name should be optional
def get_formatted_name_3(first_name_3, last_name_3, middle_name_3=''):
	if middle_name_3:
		full_name_3 = f"{first_name_3} {middle_name_3} {last_name_3}"
	else:
		full_name_3 = f"{first_name_3} {last_name_3}"
	return full_name_3.title()

musician_3 = get_formatted_name('jimi', 'hendrix')
print (musician_3)

musician_3 = get_formatted_name_3('jimi', 'hendrix', middle_name_3='lee')
print (musician_3)
