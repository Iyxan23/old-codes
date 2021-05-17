import turtle
import math
import random


class Connection:
    weight = float()

    def __init__(self, weight):
        self.weight = weight


class Neuron:
    value = float()
    connections = list()

    def __init__(self, val, connections):
        self.value = val
        self.connections = connections

    def setvalue(self, val):
        self.value = val

    def setconnection(self, connections):
        self.connections = connections

    def addconnection(self, connection):
        self.connections.append(connection)

    def delconnection(self, index):
        self.connections.pop(index)

    def randomconnections(self, index):
        for a in range(0, index):
            self.connections.append(float(random.randint(-1, 1)) + float(0.1 * random.randint(0, 10)))

    def startconnecting(self, layer):
        for l in range(0, len(layer.neurons)):
            # l = int index neuron dan connection
            layer.neurons[l].setvalue(self.value * self.connections[l])


class Layer:
    neurons = list()
    bias = float()

    def __init__(self, bias):
        self.bias = bias

    def setneurons(self, neurons):
        self.neurons = neurons

    def addneuron(self, neuron):
        self.neurons.append(neuron)

    def makeneurons(self, index):
        for a in range(0, index):
            self.neurons.append(Neuron(0, list()).randomconnections(index))

    def delneuron(self, index):
        self.neurons.pop(index)


# LET'S START BOISS
# only 2 layers
# each layer contains 10 neurons

layers = list()

for a in range(0, 4):  # 1st the input, 2nd blank layer, 3rd blank layer
    print("AHAH")
    layers.append(Layer(1).makeneurons(10))

print(layers)

for l in range(0, len(layers[0])):
    layers[0].neurons[l].setvalue(float(random.randint(-1, 1)) + float(0.1 * random.randint(0, 10)))

for a in range(0, len(layers)):
    for b in layers[a].neurons:
        try:
            b.startconnecting(layers[a+1])
        except Exception:
            pass

print(layers)
