# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 09:54:00 2018

@author: Admin
"""
from utils.normalize import replace_whitespaces, replace_multiple_stopwords, expand_abbreviations, expand_contractions

def clean_text(text):
    clean_dict = {}
    # Replace whitespaces.
    clean_dict['replace_whitespaces'] = replace_whitespaces(text)
    # Replace multiple stopwords.
    clean_dict['replace_multiple_stopwords'] = replace_multiple_stopwords(clean_dict['replace_whitespaces'])
    # Replace apostrophes.
    ##clean_dict['replace_apostrophes'] = replace_apostrophes(clean_dict['replace_multiple_stopwords'])
    # Expand contractions.
    clean_dict['expand_contractions'] = expand_contractions(clean_dict['replace_apostrophes'])
    # Remove hyperlinks.
    ##clean_dict['remove_hyperlinks'] = remove_hyperlinks(clean_dict['expand_contractions'])
    # Remove special characters.
    ##clean_dict['remove_special_characters'] = remove_special_characters(clean_dict['remove_hyperlinks'])
    # Remove numbers.
    ##clean_dict['remove_numbers'] = remove_numbers(clean_dict['remove_special_characters'])
    # Convert to lower case.
    ##clean_dict['convert_case'] = convert_case(clean_dict['remove_numbers'])
    # Expand abbreviations.
    clean_dict['expand_abbreviations'] = expand_abbreviations(clean_dict['convert_case'])
    # Tokenize sentences.
    ##clean_dict['sentence_tokenize'] = sentence_tokenize(clean_dict['expand_abbreviations'])
    return clean_dict
