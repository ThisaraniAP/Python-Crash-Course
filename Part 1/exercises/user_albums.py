# 12/06/2021
def make_album(artist_name, album_name, number_of_songs = None):
	album = {'artist name' : artist_name.title(), 'album name' : album_name, }
	if number_of_songs:
		album['number of songs'] = number_of_songs
	return album

prompt = "If you answer the following questions, "
prompt += "I will make a dictionary for you!"
prompt += "\n(Enter 'q' anytime to quit)"
print (prompt)
while True:
        artist_name = input("\nWhat is the artist's name? ")
        if artist_name == 'q':
                break
        album_name = input("What is the album's name? ")
        if album_name == 'q':
                break
        album = make_album(artist_name, album_name)
        print (album)
