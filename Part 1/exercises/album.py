# 12/06/2021
def make_album(artist_name, album_name, number_of_songs = None):
	album = {'artist name' : artist_name.title(), 'album name' : album_name, }
	if number_of_songs:
		album['number of songs'] = number_of_songs
	return album

album_1 = make_album('hello', 'How are you?')
print (album_1)
album_2 = make_album('bye', 'See you later')
print (album_2)
album_3 = make_album('library', 'Reading', number_of_songs = 8)
print (album_3)