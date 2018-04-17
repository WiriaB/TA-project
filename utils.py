# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:11:09 2018

@author: Admin
"""
from os import pardir
from os.path import join, dirname, realpath
from pickle import load
# Relative path to data folder.
_DATA_FOLDER_PATH = join(dirname(realpath('__ file __')),"Dataset")

def get_data_path(sub_path):
    """Returns path to file in data folder."""
    return join(_DATA_FOLDER_PATH, sub_path)


def data_from_pickle(sub_path):
    file_path_ext = get_data_path(sub_path)

    if exists(file_path_ext):
        with open(file_path_ext, 'rb') as f:
            return load(f)

