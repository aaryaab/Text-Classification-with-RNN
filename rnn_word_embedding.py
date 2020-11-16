# -*- coding: utf-8 -*-
"""RNN_word embedding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dIwU0WZXMiCnttaZnOAbGjMMWDGZ3wNa
"""



from keras.preprocessing.text import one_hot

sentence=['Fast cars are good',
          'Football is a famous sport',
          'Be happy Be positive']

vocab_size=1000

encoded_docs=[one_hot(d,vocab_size) for d in sentence]

from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding

import numpy as np

embedding_length=5
max_length=10

encoded_docs=pad_sequences(encoded_docs,truncating='post',padding='post',maxlen=max_length)
print(encoded_docs)

model=Sequential()
model.add(Embedding(vocab_size,embedding_length,input_length=max_length))
model.compile('rmsprop','mse')
model.summary()
output=model.predict(encoded_docs)
print(output.shape)
print(output)

