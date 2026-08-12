from network import Network

network = Network()

trainingData = []
epochs = 1 #How many times the network should train on the full dataset

for epoch in range(epochs):

    # Goes through every training example
    for example in trainingData:
        inputs = example["inputs"]
        correctNumber = example["correctNumber"]

        network.train(inputs, correctNumber)
