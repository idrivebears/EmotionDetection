from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer
import random

dataModel = [
    [(0,0), (0,)],
    [(0,1), (1,)],
    [(1,0), (1,)],
    [(1,1), (0,)],
]

#Un set de datos supervisados con dos entradas y una salida
xorData = SupervisedDataSet(2,1)

#Añadimos los inputs y valores esperados
xorData.addSample((0,0),(0,))
xorData.addSample((0,1),(1,))
xorData.addSample((1,0),(1,))
xorData.addSample((1,1),(0,))

random.seed()
trainingSet = SupervisedDataSet(2,1)
for ri in range(0,1000):
    input,target = dataModel[random.getrandbits(2)];
    trainingSet.addSample(input,target)

print("Dataset usado:")
for inpt, out in xorData:
    print (inpt, out)

xorNetwork = buildNetwork(2,2,1,bias=True)
trainer = BackpropTrainer(xorNetwork, xorData, learningrate=0.5, momentum=0.9)
trainer.trainUntilConvergence(verbose=True, trainingData=trainingSet, validationData=xorData, maxEpochs=10)

print(xorNetwork.activate([0,0]))
print(xorNetwork.activate([0,1]))
print(xorNetwork.activate([1,0]))
print(xorNetwork.activate([1,1]))



