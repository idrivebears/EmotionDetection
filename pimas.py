from keras.models import Sequential
from keras.layers import Dense
import numpy

seed = 7
numpy.random.seed(seed)

dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")

print(dataset)
print len(dataset)

X = dataset[:,0:8]
Y = dataset[:,8]

print X.shape
print len(X)
print X[0]
print Y.shape
print Y[0]

# Create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X,Y, nb_epoch=1000, batch_size=10, verbose=0)


x = raw_input()
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


