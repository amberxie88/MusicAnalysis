import sys
sys.path.insert(0, '../')
from main import *

OCEAN_ALBUMS = ['nostalgia,ULTRA.',
              'channel ORANGE',
              'Blonde']

NAME = 'Frank Ocean'

songs_df = main(NAME, OCEAN_ALBUMS)

word_frequency(songs_df, NAME, ['Blonde'], ['solo'])

