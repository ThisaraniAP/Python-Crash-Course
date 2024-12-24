# 10/06/2021
def build_person(first_name, last_name):
	person = {'fisrt' : first_name, 'last' : last_name}
	return person
musician = build_person('jimi', 'hendrix')
print (musician)

def build_person_2(first_name, last_name, age=None):
	person = {'fisrt' : first_name, 'last' : last_name, }
	if age:
		person['age'] = age
	return person
musician = build_person_2('jimi', 'hendrix', age=27)
print (musician)