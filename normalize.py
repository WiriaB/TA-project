# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:33:31 2018

@author: Admin
"""
from c_music_review.review.pattern import get_whitespace_pattern, get_abbreviation_dict, get_contraction_dict
from re import IGNORECASE, DOTALL, sub, compile


def replace_whitespaces(text):
    """Replaces all whitespaces with one space."""

    # If text is empty, return None.
    if not text: return None
    else:
        normalized_text = text
    # Replaces all whitespaces with ' '.
    normalized_text = sub(get_whitespace_pattern(), ' ', normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()

    return normalized_text
#------------------------------------------------------------------------------
def _get_single_match(match):
    """Returns single match of multiple match."""

    word = match.group()
    return word[0]

def replace_multiple_stopwords(text):
    """Replaces multiple stopwords with single stopwords."""

    # If text is empty, return None.
    if not text: return None
    else:
        normalized_text = text
    # Replaces apostrophe pattern with '.
    normalized_text = sub('[.!?]+', _get_single_match, normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    
    # Return normalized text.
    return normalized_text

#------------------------------------------------------------------------------

def expand_abbreviations(text):
    """Expands contractions in text."""

    # If text is empty, return None.
    if not text: return None

    else:
        
        normalized_text = text
    # If last character is not space, add space.
    try:
        if normalized_text[-1] != ' ':
            normalized_text += ' '
    except IndexError:
        print(1)
    # Creates abbreviations pattern.
    abbreviations_pattern = compile('({})'.format(r'\.?\s|'.join(get_abbreviation_dict().keys())),flags=IGNORECASE | DOTALL)


    def expand_match(abbreviation):
        """Expands matched contraction."""

        # Retrieves matched contraction from string.
        match = abbreviation.group(0)
        # If last character is space, remove space.
        if match[-1] == " ":
            match = match[:-1]
            remove_space = True
        else:
            remove_space = False
        # If last character is dot, remove dot.
        if match[-1] == r'.':
            match = match[:-1]
        # Find expanded contraction in dictionary, based on contraction key.
        expanded_contraction = get_abbreviation_dict().get(match.lower())
        if not expanded_contraction:
            return abbreviation.group(0)
        if remove_space:
            expanded_contraction += " "
        # Add first character to expanded contraction.
        return expanded_contraction

    # Replaces contractions with expanded contractions in text.
    normalized_text = abbreviations_pattern.sub(expand_match, normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If text was tokenized, re-tokenize text.
   # if was_tokenized:
   #     normalized_text = word_tokenize(normalized_text)

    # Return expanded text.
    return normalized_text
#------------------------------------------------------------------------------
def expand_contractions(text):
    """Expands contractions in text."""

    # If text is empty, return None.
    if not text: return None
    
    else:
        
        normalized_text = text

    # Creates contractions pattern.
    contractions_pattern = compile('({})'.format('|'.join(get_contraction_dict().keys())), flags=IGNORECASE | DOTALL)

    def expand_match(contraction):
        """Expands matched contraction."""

        # Retrieves matched contraction from string.
        match = contraction.group(0)
        # Stores first character for case sensitivity.
        first_char = match[0]
        # Find expanded contraction in dictionary, based on contraction key.
        expanded_contraction = get_contraction_dict().get(match)
        # If the contraction could not be found, try again with lower case.
        if not expanded_contraction:
            expanded_contraction = get_contraction_dict().get(match.lower())
        # Add first character to expanded contraction.
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    # Replaces contractions with expanded contractions in text.
    normalized_text = contractions_pattern.sub(expand_match, normalized_text)
    # Strip text.
    normalized_text = normalized_text.strip()
    # If text was tokenized, re-tokenize text.
    #if was_tokenized:
     #   normalized_text = word_tokenize(normalized_text)

    # Return expanded text.
    return normalized_text









