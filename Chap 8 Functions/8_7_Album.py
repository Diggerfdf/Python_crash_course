def make_album(artist_name, album_title):
	"""Build a dictionary containing information about an album."""
	album_dict = {"Artist": artist_name.title(), "album": album_title.title()}
	return album_dict
	
album = make_album('MegAdeTh', 'Rust IN PeAce')
print(album)

album = make_album('Iron MaIDEn', 'PieCE of Mind')
print(album)

album = make_album('ELP', 'TARkUS')
print(album)

# With Track option on.

print("\n\n\n")

def make_album(artist_name, album_title, tracks = 0):
	"""Build a dictionary containing information about an album."""
	album_dict = {"Artist": artist_name.title(), "album": album_title.title()}
	
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict
	
album = make_album('MegAdeTh', 'Rust IN PeAce')
print(album)

album = make_album('Iron MaIDEn', 'PieCE of Mind')
print(album)

album = make_album('ELP', 'TARkUS')
print(album)

album = make_album('ELP', 'ELP', tracks=5)
print(album)
