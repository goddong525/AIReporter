import os.path

import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(3, 5),
    tf.keras.layers.SimpleRNN(3),
    tf.keras.layers.Dense(6),
    tf.keras.layers.Softmax()
])

if not os.path.exists('../models'):
    os.mkdir('../models')

model.save('../models/softmax.h5')
model.save('../models/dense.h5')
model.save('../models/embedding.h5')
model.save('../models/mn.h5')
