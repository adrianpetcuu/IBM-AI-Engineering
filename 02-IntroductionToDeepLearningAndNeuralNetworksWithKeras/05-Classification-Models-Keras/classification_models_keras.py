import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Input
from keras.utils import to_categorical

import matplotlib.pyplot as plt

# Import the data
from keras.datasets import mnist

# Read the data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(X_train.shape)

plt.imshow(X_train[0])
plt.show()

# Flatten images into one-dimensional vector

num_pixels = X_train.shape[1] * X_train.shape[2] # Find size of one-dimensional vector
X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32') # Flatten training images
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32') # Flatten test images

# Normalize input from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255

# One hot encode outputs
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

num_classes = y_test.shape[1]
print(num_classes)

# BUILD A NEURAL NETWORK
def classification_model():
    model = Sequential()
    model.add(Input(shape=(num_pixels, )))
    model.add(Dense(num_pixels, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Train and Test the Network
model = classification_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=2)
# Evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)

print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))

model.save('classification_model.keras')

pretrained_model = keras.saving.load_model('classification_model.keras')

# Exercises - Create a neural network model with 6 dense layers and compare its accuracy
def classification_model_6layers():
    # Create model
    model = Sequential()
    model.add(Input(shape=(num_pixels, )))
    model.add(Dense(num_pixels, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    # Compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Build the model
model_6layers = classification_model_6layers()

# Fit the model
model_6layers.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=2)

# Evaluate the model
scores_6layers = model_6layers.evaluate(X_test, y_test, verbose=0)

print('Accuracy_3_layers: {}% \n Accuracy_6_layers: {}'.format(scores[1], scores_6layers[1]))

# Now, load the the earlier saved model, train it further for 10 more epochs and check the accuracy

# Load the saved model
pretrained_model = keras.saving.load_model('classification_model.keras')
print('Pre-trained model loaded successufully')

# Further train the loaded model
pretrained_model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=2)

# Evaluate the model
scores_20_epochs = pretrained_model.evaluate(X_test, y_test, verbose=0)
print('Accuracy_10_epochs: {}% \n Accuracy_20_epochs: {}'.format(scores[1], scores_20_epochs[1]))