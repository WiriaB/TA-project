# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:53:18 2018

@author: Admin
"""
import random as rd

import json 
from os.path import join, exists
from os import makedirs
from utils.utils import get_data_path
from pickle import dump
#from c_music_review.review.review import create_review_from_dict 
#import ast

def make_music_review_set():
    """
    Creates set of review.
    Returns:
        Set of review objects.
    """

    # Create relative file path to 01_raw file.
    file_path = get_data_path('raw_data\\reviews_Digital_Music.json')
    # Open connection and read .json file.
    
    with open(file_path, encoding="utf8") as music_review_dict_list:
        vd_review_set=[]
        for review_dict in music_review_dict_list:
            #review = create_review_from_dict(ast.literal_eval(review_dict))
            vd_review_set.append(json.loads(review_dict))
    # Return tweet set.
    del review_dict
    
    return vd_review_set




# Generating main_set, train_set and test_set
def data_set_call(rw):
    max_docs_per_category=rd.sample(rw,100000)

    # max_docs_per_category=100000
    max_train_size = 70000
    max_test_size = 30000
    train_index = set()
    test_index = set()
    
    # Get random number in range 0 through max_docs_per_category
    while len(train_index) < max_train_size:
        n = rd.randint(0, 99999)
        if not n in train_index:
            train_index.add(n)
    
    for i in range(100000):
        if not i in train_index:
            test_index.add(i)
    
    
    # now you should randomize the keys of your test set
    temp_test = list(test_index)
    rd.shuffle(temp_test)
    temp_train=list(train_index)
    rd.shuffle(temp_train)
    
    train_list=[]
    test_list=[]
    
    for line in range(len(temp_test)):
        test_list.append(max_docs_per_category[temp_test[line]])
    
    for line in range(len(temp_train)):
        train_list.append(max_docs_per_category[temp_train[line]])

    #test_list[0]
    # Normalization 
    
    # 1. Load 'reviewText' in lower Case value    
    #reviewText=[]
    #for i in range(len(train_list)):
    #    reviewText.append(train_list[i]['reviewText'].lower())
        
    return {
            "maxdocs": max_docs_per_category,
            "testdocs":test_list,
            "traindocs": train_list}

# pull out review text

def pull_out_reviewtext(dt):
    
    reviewText=[]
    for i in range(len(dt)):
        reviewText.append(dt[i]['reviewText'])
        
    return reviewText

        
        
        
        
        
