# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:48:54 2019

@author: Luis Rodriguez
"""

# ANÁLISIS DE SENTIMIENTOS EN COMENTARIOS

import pandas as pd
from textblob import TextBlob


df = pd.read_csv('your_file_name.csv')

df['polarity'] = df['content'].apply(lambda x: TextBlob(x).sentiment.polarity)

df['SubjectObject'] = df['content'].apply(lambda x: TextBlob(x).sentiment.subjectivity)



print(df['polarity'])

print ('Min Polarity', df['polarity'].min())

print ('Average Polarity', df['polarity'].mean())

column_number=len(df.columns)

n=0

while n<column_number:
    df['P ' + str(n)] = df['content'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['S ' + str(n)] = df['content'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    n += 1

# Export results to CSV

df.to_csv('exported_results_file_name.csv')
