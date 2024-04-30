
'''
    DS2500
    Spring 2022
    Lab 6 starter code
'''

import re
import random

HAM = "hamilton_lyrics.txt"


#### TODO ####
# Update the read_lyrics function so it ignores everything in square brackets
# e.g., [HAMILTON], [ELIZA], [WHOLE COMPANY], etc.
#
# We also strongly suggest getting rid of punctuation!
def read_lyrics(filename):
    ''' Function: read_lyrics
        Parameters: filename, a string
        Returns: a list of strings, one string per line
                (removes empty lines and linebreaks, 
                 and makes everything lowercase)
    '''
    all_lines = []
    with open(filename) as infile:
        while True:
            line = infile.readline()
            if not line:
                break
            if line.strip() == "":
                continue
            all_lines.append(line.strip().lower())
    return all_lines



def generate_lyric(begin, ending, ngrams):
    ''' Function: generate_lyric
        Parameters: list of begin-words, list of end-words,
                    dictionary of key = word, value = list of followed-by
        Returns: one line of Hamilton lyric
    '''
    sentence = ""
    curr_word = random.choice(begin)
    while True:
        sentence += " " + curr_word
        if curr_word in ending:
            break
        curr_word = random.choice(ngrams[curr_word])
    return sentence
