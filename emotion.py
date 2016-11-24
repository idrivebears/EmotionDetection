from keras.models import Sequential
from keras.layers import Dense, Convolution2D, MaxPooling2D, Activation
from load_data import load_images
import numpy

# Create model
def VVG_S(weight_path=None):
    model = Sequential()
    model.add(Convolution2D(96,7,7,input_shape=(1,256,256),border_model='valid')
    model.add(Activation('relu')
    model.add(MaxPooling2D(pool_size=(3, 3), strides=None, border_mode='valid', dim_ordering='default'))
    model.add(Convolution2D(256,5,5,border_model='valid')
    model.add(Activation('relu')
    model.add(MaxPooling2D(pool_size=(2, 2), strides=None, border_mode='valid', dim_ordering='default'))
    model.add(Convolution2D(512,3,3,border_model='valid')
    model.add(Activation('relu')
    model.add(Convolution2D(512,3,3,border_model='valid')
    model.add(Activation('relu')
    model.add(Convolution2D(512,3,3,border_model='valid')
    model.add(Activation('relu')
    model.add(MaxPooling2D(pool_size=(3, 3), strides=None, border_mode='valid', dim_ordering='default'))

    model.add(Flatten())
    model.add(Dense(4048, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(4048, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(6, activation='softmax'))
    
    if weights_path:
        model.load_weights(weight_path)

    return model

seed = 13
numpy.random.seed(seed)

# Load training dataset
X_train, Y_train = load_images('datasets/training_images/')

# Load validation dataset
X_valid, Y_valid = load_images('datasets/validation_images/')

model = VGG_S('vggs_weights.h5')
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Play with epoch value
hist = model.fit(X_train,Y_train, nb_epoch=100, batch_size=10)
print(hist.history)

# scores = model.evaluate(X[validate], Y[validate])
# print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
              
# At the end, use test dataset
# scores = model.evaluate(X[test], Y[test])      
# print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


