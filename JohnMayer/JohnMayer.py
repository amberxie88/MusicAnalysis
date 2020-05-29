import sys
sys.path.insert(0, '../')
from main import *

MAYER_ALBUMS = ['Room for Squares',
              'Heavier Things',
              'Continuum',
              'Battle Studies',
              'Born and Raised',
              'Paradise Valley',
              'The Search for Everything']

NAME = 'John Mayer'

songs_df = main(NAME, MAYER_ALBUMS)

#Specific Methods for this particular artist
word_frequency(songs_df, NAME, MAYER_ALBUMS, ['love'])
