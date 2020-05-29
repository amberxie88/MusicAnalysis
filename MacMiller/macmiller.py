import sys
sys.path.insert(0, '../')
from main import *

MAC_ALBUMS = ['The Jukebox: Prelude to Class Clown',
              'The High Life',
              'K.I.D.S',
              'Best Day Ever',
              'I Love Life, Thank You',
              'Blue Slide Park',
              'Macadelic',
              'Watching Movies With the Sound Off',
              'Faces',
              'GO:OD AM',
              'The Divine Feminine',
              'Swimming']

NAME = 'Mac Miller'

songs_df = main(NAME, MAC_ALBUMS)

word_frequency(songs_df, NAME, ['Swimming'], ['swim'], extra_words=['swimmin\'', 'swimming'])

