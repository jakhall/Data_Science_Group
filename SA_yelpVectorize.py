import pandas as pd
import numpy as np
import time
import feather as ft
from keras.preprocessing.text import text_to_word_sequence, one_hot, hashing_trick, Tokenizer



print("1")
review1 = ft.read_dataframe("D:/reviews1.feather")
#review2 = ft.read_dataframe("D:/reviews2.feather")
#reviews_split = review1.append(review2)

(reviews_split, chunk2) = np.array_split(review1, 2)
#reviews_split = ft.read_dataframe("D:/test.feather")
print("2")
reviews_split['seq_text'] = reviews_split['text'].apply(text_to_word_sequence)
print("3")
temp = reviews_split['seq_text'].apply(pd.Series).stack().unique()
#vocab_size = len(reviews_split['seq_text'].apply(pd.Series).stack().unique())
vocab_size = len(temp)
print(vocab_size)
print("4")
reviews_split['vectorised'] = reviews_split['text'].apply(lambda x : hashing_trick(x, round(vocab_size*1.5), hash_function= 'md5'))
print("5")
reviews_split.to_csv('D:/review_test.csv') # writing to csv to save re-splitting


print(reviews_split.head(20))
