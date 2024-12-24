# 20/05/2021
favorite_languages = {
	'jen' : 'python',
	'sarah' :'c',
	'edward' : 'ruby',
	'phil' : 'python',
	}
language = favorite_languages['sarah'].title()
print (f"Sarah's favorite language is {language}.\n")


# 23/05/2021
for name, language in favorite_languages.items():
	print (f"{name.title()}'s favorite language is {language.title()}.")


print ("\nNames")
for name in favorite_languages.keys():
	print (name.title())

print ("\nNames")
for name in favorite_languages:
	print (name.title())


print ("\n")
friends = ['phil', 'sarah']
for name in favorite_languages:
	print (f"Hi {name.title()}!")
	if name in friends:
		language = favorite_languages[name].title()
		print (f"\t{name.title()}, I see you love {language}!")


if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!\n")

for name in sorted(favorite_languages.keys()):
	print (f"{name.title()}, thank you for taking the poll.")


print ("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print (language.title())

print ("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print (language.title())


languages = {'python', 'ruby', 'python', 'c'}
# This is a set, it dosen't have key-value pairs.
print ("\n", set(languages), "\n")
# Sets do not retain items in any specific order.


names = ['edward', 'john', 'maya', 'sarah', 'percy']
for name in names:
	if name in favorite_languages:
		print (f"{name.title()}, thank you for taking the poll!")
	else:
		print (f"{name.title()}, please take our poll.")