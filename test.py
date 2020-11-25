import tensorflow as tf

from tensorflow import keras

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences
### **The Corpus**
sentences = [

             'I love my dog',

             'I love my cat',

             'You love my dog!',

             'Do you think my dog is amazing?'

]
# Only the most common `num_words - 1` words will be kept

tokenizer = Tokenizer(num_words=3)

tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
# help(Tokenizer)
print(word_index)

sequences = tokenizer.texts_to_sequences(sentences)
print(sequences)
test_data = [

             'i really love my dog',

             'my dog loves my manatee'

]



test_seq = tokenizer.texts_to_sequences(test_data)

print(test_seq)
padded = pad_sequences(sequences, padding='post', truncating='post', maxlen=5)

print(padded)

 
