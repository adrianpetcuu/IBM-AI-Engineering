import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Input

import warnings
warnings.simplefilter('ignore', FutureWarning)

filepath = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0101EN/labs/data/concrete_data.csv'
concrete_data = pd.read_csv(filepath)
print(concrete_data.head())

print(concrete_data.shape)

print(concrete_data.isnull().sum())

# Split data into predictors and target
concrete_data_columns = concrete_data.columns
predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']] # All columns except Strength
target = concrete_data['Strength'] # Strength column

print(predictors.head())
print(target.head())

# Normalize the data by substracting the mean and dividing by the standard deviation
predictors_norm = (predictors - predictors.mean()) / predictors.std()
print(predictors_norm.head())

n_cols = predictors_norm.shape[1] # number of predictors

# Build a Neural Network
# Define regression model
def regression_model():
    # Create model
    model = Sequential()
    model.add(Input(shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))

    # Compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Train the test the Network
model = regression_model()

# Fit the model
model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)

# Exercises 1 : Recreate regression model featuring five hidden layers, each with 50 nodes and ReLU
# activation functions, a single output layer, optimized using the Adam optimizer
def regression_model2():
    input_colm = predictors_norm.shape[1] # Number of input features
    # Create model
    model = Sequential()
    model.add(Input(shape=(input_colm,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1)) # Output layer
    # Compile
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

model = regression_model2()
model.fit(predictors_norm, target, validation_split=0.1, epochs=100, verbose=2)