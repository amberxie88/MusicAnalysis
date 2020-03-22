import sys
sys.path.insert(0, '../')
from main import *

ABSTRACT_ALBUMS = ['American Boyfriend: A Suburban Love Story']

NAME = 'Kevin Abstract'

songs_df = main(NAME, ABSTRACT_ALBUMS)

word_frequency(songs_df, NAME, ['American Boyfriend: A Suburban Love Story'], ['football'])