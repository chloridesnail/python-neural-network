import random

class Layer:
    def __init__(self, n_inputs, n_nodes):
        self.n_inputs = n_inputs
        self.n_nodes = n_nodes

        # Creates the corresponding weights for the inputs using a 2D matrix
        self.weightsArray = np.random.randn(n_nodes, n_inputs) * 0.01 
        self.biasesArray = np.zeros(n_nodes)
        self.nodesArray = np.zeros(n_nodes)

    def forward(self, inputs): #calculates all the values for the layer
        self.nodesArray = (self.weightsArray @ inputs) + self.biasesArray  #adds the bias

    def activate(self):
        self.nodesArray = np.maximum(0, self.nodesArray)