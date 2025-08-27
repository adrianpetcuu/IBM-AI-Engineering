import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Input
from keras.utils import to_categorical
# Convolutional neural network
from keras.layers import Conv2D # to add convolutional layers
from keras.layers import MaxPooling2D # to add pooling layers
from keras.layers import Flatten # to flatter data for fully connected layers

# Convolutional Neural Network with One Set of Convolutional and Pooling Layers
# Import data
from keras.datasets import mnist
# Load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# Reshape to be [samples][pixels][width][height]
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')

X_train = X_train / 255 # normalize training data
X_test = X_test / 255 # normalize test data

# Convert the target variable into binary categories
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

num_classes = y_test.shape[1] # number of categories

# Define a function that creates our model. Let's start with one set of convolutional and pooling layers
def convolutional_model():
    # Create model
    model = Sequential()
    model.add(Input(shape=(28, 28, 1)))
    model.add(Conv2D(16, (5, 5), strides=(1, 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    # Compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Build the model
model = convolutional_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)
# Evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: {} \n Error: {}".format(scores[1], 100 - scores[1] * 100))

# Convolutional Neural Network with Two Sets of Convolutional and Pooling Layers
def convolutional_model2():
    model = Sequential()
    model.add(Input(shape=(28, 28, 1)))
    model.add(Conv2D(16, (5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(Conv2D(8, (2, 2), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    # Compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Build the model
model = convolutional_model2()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)
# Evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: {} \n Error: {}".format(scores[1], 100 - scores[1] * 100))

# How batch size affects the time required and accuracy of the model training
# Change batch_size to 1024 and check it's effect on accuracy
model = convolutional_model2()
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=1024, verbose=2)
scores = model.evaluate(X_test, y_test, verbose=0)
print('Accuracy: {} \n Error: {}'.format(scores[1], 100 - scores[1] * 100))

# Let's see how number of epochs affect the time required and accuracy of the model training
# You can keep the batch_size=1024 and epochs=25 and check it's effect on accuracy
model = convolutional_model2()
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=25, batch_size=1024, verbose=2)
scores = model.evaluate(X_test, y_test, verbose=0)
print('Accuracy: {} \n Error: {}'.format(scores[1], 100 - scores[1] * 100))

