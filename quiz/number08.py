import tensorflow as tf
import numpy as np

index_word = ['가', '나', '다', '라']

x = [[0,1,2], [2,1,0]]
y = [[0,0,0,1], [1,0,0,0]]

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(4,5),
    tf.keras.layers.SimpleRNN(6),
    tf.keras.layers.Dense(4),
    tf.keras.layers.Softmax()
])

model.summary()

predict = model.predixt([[0,1,2]])
print(predict)

loss = tf.keras.losses.CategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
