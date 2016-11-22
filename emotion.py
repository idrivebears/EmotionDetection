from keras.models import Sequential
from keras.layers import Dense
import numpy

seed = 13
numpy.random.seed(seed)

# Load dataset


# Create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
#model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#model.fit(X,Y, nb_epoch=1000, batch_size=10)

#scores = model.evaluate(X, Y)
#print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


