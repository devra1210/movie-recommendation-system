import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

movies_df = pd.read_csv('data/tmdb_5000_movies.csv')
credits_df = pd.read_csv('data/tmdb_5000_credits.csv')

print(movies_df.head(2))
print(credits_df.head(2))

print(movies_df.shape)
print(credits_df.shape)

movies_df = pd.merge(movies_df, credits_df, on='title', how='outer')
print(movies_df)


