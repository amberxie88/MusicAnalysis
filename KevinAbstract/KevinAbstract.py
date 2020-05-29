import sys
sys.path.insert(0, '../')
from main import *

ABSTRACT_ALBUMS = ['American Boyfriend: A Suburban Love Story']

NAME = 'Kevin Abstract'

songs_df = main(NAME, ABSTRACT_ALBUMS)

#word_frequency(songs_df, NAME, ['American Boyfriend: A Suburban Love Story'], ['American'], extra_words = ['football', 'suburban', 'suburbs', 'America', 'school'])
#word_frequency(songs_df, NAME, ['American Boyfriend: A Suburban Love Story'], ['love'])
#word_frequency(songs_df, NAME, ABSTRACT_ALBUMS, ['hate'])
word_frequency(songs_df, NAME, ABSTRACT_ALBUMS, ['boyfriend'])