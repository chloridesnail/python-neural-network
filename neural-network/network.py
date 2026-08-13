from layer import Layer
import json
import numpy as np

class Network:
    def __init__(self):
        self.layers = []
        self.networkShape = [1600,64,10]

        for index in range(1, len(self.networkShape)): #for every layer in the network excluding the first
            n_inputs = self.networkShape[index - 1] #number of inputs are the nodes previous layer
            n_nodes = self.networkShape[index] #number of nodes
            self.layers.append(Layer(n_inputs, n_nodes)) #creates the layer

    def forward(self, inputs):
        currentValues = np.array(inputs)
        for index, layer in enumerate(self.layers): #for every layer in the network
            layer.forward(currentValues)

            if index < len(self.layers) - 1: #if the layer isnt the last one
                layer.activate()
            
            currentValues = layer.nodesArray
        
        return currentValues

    def predict(self, inputs):
        endValues = self.forward(inputs)
        prediction = np.argmax(endValues) #returns the index of the largest value (final number)
        return prediction

    def train(self, inputs, correctNumber):

        outputs = self.forward(inputs)
        learningRate = 0.01

        target = np.zeros(self.networkShape[-1])
        target[correctNumber] = 1

        outputDeltas = outputs - target #numpy makes array subtraction easier
        hiddenLayer = self.layers[0]
        outputLayer = self.layers[1]

        hiddenDeltas = []
        errors = outputLayer.weightsArray.T @ outputDeltas #output delta x connecting weight
        reluDerivative = hiddenLayer.nodesArray > 0 # ReLU activation function
        hiddenDeltas = errors * reluDerivative
        
        #weight change = learning rate × output delta × hidden node value
        outputLayer.weightsArray -= learningRate * np.outer(outputDeltas, hiddenLayer.nodesArray)
        #bias change = learning rate x delta
        outputLayer.biasesArray -= learningRate * outputDeltas
        
        #hidden layer weight change = learning rate x hidden delta x input value
        hiddenLayer.weightsArray -= learningRate * np.outer(hiddenDeltas, inputs)
        #hidden layer bias change = learning rate x hidden delta
        hiddenLayer.biasesArray -= learningRate * hiddenDeltas

        #(output - target)²
        loss = np.sum((outputLayer.nodesArray - target) ** 2) / 2
        return loss, self.predict(inputs)

    def save(self):
        layersData = []

        for layer in self.layers:
            layerData = { 
                "weights": layer.weightsArray.tolist(), #converts numpy array to list for json compatibility
                "biases": layer.biasesArray.tolist()
            }

            layersData.append(layerData)

        data = {
            "networkShape": self.networkShape,
            "layers": layersData
        }

        with open("model.json", "w") as file: #creates "model.json"
            json.dump(data, file) #saves the data in the file

    def load(self):
        with open("model.json", "r") as file: #locates "model.json"
            data = json.load(file) #loads the data from the file

        layersData = data["layers"]

        for index, layerData in enumerate(layersData):
            self.layers[index].weightsArray = np.array(layerData["weights"]) #converts list back to numpy array
            self.layers[index].biasesArray = np.array(layerData["biases"]) #converts list back to numpy array
