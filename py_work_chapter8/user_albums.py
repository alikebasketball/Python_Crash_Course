# Assignment 8-8; User Albums
# Assignment 8-7.. BUT WITH A TWIST

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

active = True
while active:
    print('Please enter a musicians name, album, and if you want\n'
          'the number of songs on that album.')
    print('''Enter 'q' to stop at anytime. \n''')
    
    
    
    artist_name = input('Name: ')
    
    if artist_name.isprintable():
        
        if artist_name.lower() =='q':
            break
    else:
        print('Please enter a name..')
        continue
    
    
        
    artist_album = input('\nName of Album: ')
    
    if artist_album.isprintable():
        
        if artist_album.lower() =='q':
            break
    else:
        print('Please enter an album..')
        continue
    
    
    
    songs_on_album = input('\nNumber of songs on album, remember this is not needed: ')
    
    if songs_on_album == '' or songs_on_album == None:
        album_formatted = make_album(artist_name,artist_album, songs_on_album)
        print(f'\n{album_formatted}\n')
        continue
        
    
    if songs_on_album == 'q':
        break
        
    else:
        print('Thanks for the optional data!\n\n')
        
    
    album_formatted = make_album(artist_name,artist_album, songs_on_album)
    print(album_formatted)
    
    