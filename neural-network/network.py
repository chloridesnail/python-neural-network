from layer import Layer
import json

class Network:
    def __init__(self):
        self.layers = []
        self.networkShape = [1600,64,10]

        for index in range(1, len(self.networkShape)): #for every layer in the network excluding the first
            n_inputs = self.networkShape[index - 1] #number of inputs are the nodes previous layer
            n_nodes = self.networkShape[index] #number of nodes
            self.layers.append(Layer(n_inputs, n_nodes)) #creates the layer

    def forward(self, inputs):
        currentValues = inputs
        for index, layer in enumerate(self.layers): #for every layer in the network
            layer.forward(currentValues)

            if index < len(self.layers) - 1: #if the layer isnt the last one
                layer.activate()
            
            currentValues = layer.nodesArray
        
        return currentValues

    def predict(self, inputs):
        endValues = self.forward(inputs)
        prediction = endValues.index(max(endValues)) #returns the index of the largest value (final number)
        return prediction

    def train(self, inputs, correctNumber):

        outputs = self.forward(inputs)
        learningRate = 0.01

        target = [0] * self.networkShape[-1] 
        target[correctNumber] = 1

        outputDeltas = []
        hiddenLayer = self.layers[0]
        outputLayer = self.layers[1]
        for node in range(len(outputs)):
            outputDeltas.append(outputs[node] - target[node])

        hiddenDeltas = []
        for hiddenNode in range(hiddenLayer.n_nodes): #
            error = 0
            for outputNode in range(outputLayer.n_nodes):   #output delta x connected weight
                error += outputDeltas[outputNode] * outputLayer.weightsArray[outputNode][hiddenNode] 
            if hiddenLayer.nodesArray[hiddenNode] > 0: #ReLU activation function
                reluDerivative = 1
            else:
                reluDerivative = 0 # below 0, = 0
            error = error * reluDerivative
            hiddenDeltas.append(error)
        
        for outputNode in range(outputLayer.n_nodes): #output layer
            for hiddenNode in range(hiddenLayer.n_nodes): #weight change = learning rate × output delta × hidden node value
                change = learningRate * outputDeltas[outputNode] * hiddenLayer.nodesArray[hiddenNode]
                outputLayer.weightsArray[outputNode][hiddenNode] -= change
            biasChange = learningRate * outputDeltas[outputNode] #bias change = learning rate x delta
            outputLayer.biasesArray[outputNode] -= biasChange
        for hiddenNode in range(hiddenLayer.n_nodes): #hidden layer
            for inputIndex in range(hiddenLayer.n_inputs):
                change = learningRate * hiddenDeltas[hiddenNode] * inputs[inputIndex]
                hiddenLayer.weightsArray[hiddenNode][inputIndex] -= change
            biasChange = learningRate * hiddenDeltas[hiddenNode]
            hiddenLayer.biasesArray[hiddenNode] -= biasChange

        loss = 0
        for node in range(outputLayer.n_nodes):
            difference = (outputLayer.nodesArray[node] - target[node]) #(output - target)²
            loss += difference ** 2
        loss = loss / 2
        return loss, self.predict(inputs)

    def save(self):
        layersData = []

        for layer in self.layers:
            layerData = { 
                "weights": layer.weightsArray,
                "biases": layer.biasesArray
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
            self.layers[index].weightsArray = layerData["weights"]
            self.layers[index].biasesArray = layerData["biases"]