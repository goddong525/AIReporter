import tensorflow as tf
import pandas as pd

data = pd.read_csv('../data/titles.csv')
titles = data['title'].values

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(titles)

sequences = []
max_len = 0

sequence = tokenizer.texts_to_sequences([titles[0]])[0]

sequences.append(sequence)
max_len = max(max_len, len(sequence))
print(titles[0])
print(sequence)
print(max_len)
#----
pad_sequences = tf.keras.preprocessing.sequencepad_sequences.pad_sequences(sequences, maxlen=max_len)
#----
print(pad_sequences)