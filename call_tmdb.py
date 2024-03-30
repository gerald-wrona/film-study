# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:35:15 2024

@author: wrona
"""
import os
import pandas as pd

# Get ratings
ratings = pd.read_csv('~\\Documents\\upskill\\film-study\\letterboxd_data\\ratings.csv')

ratings.columns.values.tolist()


#%% Example call


import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "removed for security"

response = requests.get(url, headers=headers)

print(response.text)