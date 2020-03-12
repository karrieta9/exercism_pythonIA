import re

def abbreviate(words):
    acronym = ''
    for word in words.replace('-',' ').replace('_',' ').replace(',',' ').replace('.',' ').split():
        acronym+= word[0]
    
    return acronym.upper()


