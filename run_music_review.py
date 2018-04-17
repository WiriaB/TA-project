# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:41:22 2018

@author: Admin
"""
from c_music_review.data.io import make_music_review_set, data_set_call, pull_out_reviewtext
from c_music_review.review.clean import clean_text


# Upload Data set
rw=make_music_review_set()


# extract maxdocs with 100K records, testdocs with 30K records, traindocs 70K records
dt=data_set_call(rw)
maxdocs=pull_out_reviewtext(dt['maxdocs'])
testdocs=pull_out_reviewtext(dt['testdocs'])
traindocs=pull_out_reviewtext(dt['traindocs'])


traindocs_clean=[]

for rwe in traindocs:
    
    traindocs_clean.append(clean_text(rwe))


del rwe
#def main():
    
#   rw=make_music_review_set()
#  return rw

    
#if __name__ == '__main__':
#    main()

