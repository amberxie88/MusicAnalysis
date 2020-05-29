import sys
sys.path.insert(0, '../')
from main import *

OCEAN_ALBUMS = ['nostalgia,ULTRA.',
              'channel ORANGE',
              'Blonde']

#OCEAN_ALBUMS = ['Blonde']

NAME = 'Frank Ocean'

songs_df = main(NAME, OCEAN_ALBUMS)

#Specific Methods for this particular artist
word_frequency(songs_df, NAME, OCEAN_ALBUMS, ['solo'])

