# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:25:50 2018

@author: Admin
"""

def create_review_from_dict(review_dict):
    """
    Creates a week_3.tweet object from dictionary.

    Extracts tweet_id, created_at, text, is_retweet,
    retweet_count and favorite_count from dictionary.

    Args:
        tweet_dict: A dictionary, containing week_3.tweet information.

    Returns:
        A week_3.tweet object.
    """
    # Extract parameters from dictionary
    asin = review_dict.get('asin')
    helpful = review_dict.get('helpful')
    overall = review_dict.get('overall')
    reviewText = review_dict.get('reviewText')
    reviewTime = review_dict.get('reviewTime')
    reviewerID = review_dict.get('reviewerID')
    reviewerName = review_dict.get('reviewerName')
    summary = review_dict.get('summary')
    unixReviewTime = review_dict.get('unixReviewTime')


    # Create review object
    review={}
    review = {'asin':asin, 'reviewerID':reviewerID, 'reviewerName':reviewerName, 'reviewTime':reviewTime, 'helpful':helpful, 'overall':overall, 'reviewText':reviewText, 'summary':summary, 'unixReviewTime':unixReviewTime}

    return review