from layer import Layer

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