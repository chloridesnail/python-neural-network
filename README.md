# Neural Network Digit Recogniser

A neural network built from scratch in Python that learns to recognise handwritten digits drawn in a browser.

This project was originally built in **Luau**. After getting the Luau version working, I decided to rebuild it in **Python** to improve my Python skills and make sure I properly understood how the neural network worked rather than just copying my original code.

## How It Works

The browser contains a **40 × 40 drawing grid**.

Each cell is converted into:

* `0` if the cell is empty
* `1` if the cell is filled

This produces **1600 input values**, which are passed into the neural network.

### Network Structure

```text
1600 inputs → 64 hidden nodes → 10 output nodes
```

The 10 output nodes represent the digits `0` to `9`.

The hidden layer uses **ReLU activation**.

During training, the network makes a prediction, calculates how wrong it was using backpropagation, then adjusts its weights and biases using gradient descent.

For prediction, the output node with the highest value is chosen as the predicted digit.

## What I Built

The neural network itself was built from scratch without using machine learning libraries such as TensorFlow or PyTorch.

I implemented things including:

* Layers
* Weights and biases
* Forward propagation
* ReLU activation
* Backpropagation
* Gradient descent
* Training
* Prediction
* Saving and loading the network

## Technologies

* Python
* Flask
* JavaScript
* HTML
* CSS
* JSON

### `layer.py`

Contains the code for each neural network layer, including its weights, biases, nodes, forward calculations and activation.

### `network.py`

Creates the full neural network and handles forward propagation, training, prediction, and saving or loading the model.

### `server.py`

`server.py` was mostly generated with AI.

The purpose of this project was to teach myself how **neural networks** work, not how to build a Flask backend, so I chose to outsource this part rather than getting sidetracked.

It connects the browser to the Python neural network using Flask. It receives data from the JavaScript as JSON, passes it to the network for training or prediction, and sends the result back to the browser.

## Why I Made It

I wanted to understand what was actually happening inside a neural network instead of importing a machine learning library and letting it handle everything for me.

Building the network myself helped me understand how inputs move through layers, what weights and biases actually do, how activation functions affect the network, and how backpropagation allows the network to learn from mistakes.

Rebuilding my original Luau version in Python also gave me a chance to test whether I understood the concepts well enough to recreate them in another language.

## Running the Project

Install Flask:

```bash
pip install flask
```

Run the server:

```bash
python neural-network/server.py
```

Then open the address shown by Flask in your browser, usually:

```text
http://127.0.0.1:5000
```

## Current Status

The project is still being developed.

I plan to experiment with:

* Different network structures
* Different learning rates
* Training speed
* Prediction accuracy
* Different hidden layer sizes
* Comparing the Python and Luau versions
