import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['tittle'].values

print(titles)

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)
word_count = len(tokenizer.word_index)  + 1

print(tokenizer.word_index)
print(word_count)

