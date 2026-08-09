class Layer:
    def __init__(self, n_inputs, n_nodes): #creates the layer and sets up all the nodes
        self.n_inputs = n_inputs
        self.n_nodes = n_nodes
        self.weightsArray = []
        self.biasesArray = [0]*n_nodes
        self.nodesArray = [0]*n_nodes

        for node in range(self.n_nodes):
            self.weightsArray[node] = [0]*n_inputs #creates the weights table for each node

    def forward(self, inputs): #calculates all the values for the layer
        for node in range(self.n_nodes):
            self.nodesArray[node] = 0
        
        for node in range(self.n_nodes): #calculates the value for each node
            #sum of weights times their corresponding inputs
            for inputIndex in range(self.n_inputs):
                self.nodesArray[node] += self.weightsArray[node][inputIndex] * inputs[inputIndex]
            self.nodesArray[node] += self.biasesArray[node] #adds the bias

    def activate(self):
        for node in range(self.n_nodes):
            if self.nodesArray[node] < 0:
                self.nodesArray[node] = 0