# Assignment 8-7; Album
# Write a function called make_album() that builds a dictionary

def make_album(name, album, num_of_songs = None):
    """Builds a dictionary of musician and their album with number of songs as an optional argument

    Args:
        name (string): Name of musician
        album (string): The album they wrote
        num_of_songs (int, optional): The number of songs on said album. Defaults to None.
    """
    album_dic = {'Musicians name': name.title(), 'Their Album': album.title() }
    
    if num_of_songs:
        album_dic['Songs in album'] = num_of_songs
        
    return album_dic

album_one = make_album('Eric holland', 'Jack the riper of cords')
print(album_one)

album_two = make_album('Eric holland', 'My songs rule XOXO', 69)
print(album_two)

album_three = make_album('Jack daniels', 'best shot you ever took', 69)
print(album_three)

album_x = make_album('Eric holland', 'I am a legend', 69)
print(album_x)