### Neural Network

- Neuron
  - input = a vector $x \in \R^n$ of numeric input
  - output = a scalar $a_i \in \R$
  - hyper-parameter: an activation function f
  - parameter: a vector of weights $w =\ <b,w_1,w_2,…w=,w_n>\ \in \R ^{n+1}$, one for each input plus a bias term
  - mathematically
    - $a_i=f(\textbf{w}\cdot x_i+b)$
  - Update rule
    - $w_j \leftarrow w_j + \lambda(y_i - \hat{y}_i^k)x_{ij}$
    - $i$ is the ith value for weight $j$
  - Properties
    - Only guaranteed to converge for linearly-separable data
      - But depend on the initial point and learning rate
    - No guaranteed of convergence over non-linearly separable data
    - Possible to extend to multiclass classification problems in a similar manner to logistic regression
      - NN with single neuron and a sigmoid activation is equivalent to logistic regression
- Activation Function
  - Sigmoid
    - $f(x)=\frac1{1+e^{-x}}$
    - Range = [0,1]
  - Tanh
    - $f(x)=\frac{e^{2x}-1}{e^{2x}+1}$
    - Range = [-1,1]
  - Rectified linear unit (ReLU)
    - $f(x) = max(0, x)$
    - Not differentiable at x = 0

- Multi-layer Perceptrons (MLP)
  - AKA fully-connected feed-forward neural network
  - input layer is made up of the individual features
  - hidden layer is made up an arbitrary number of neurons, each of which is connected to all neurons in the preceding layer, and all neurons in the following layer
  - output layer combines the inputs from the preceding layer into the output
  - Common Output Layer Activation Functions 
    - two-class classification: one neuron with step function
    - multiclass classification: multiple perceptrons, with softmax
    - regression: identity function, sigmoid or tanh
  - Train NN with Hidden Layers 
    - Using back propagation
      - compute errors at the output layer w.r.t. each weight using partial differentiation, then propagate those errors back to each of the input layers
  - NN in practice 
    - Disadvantages 
      - Long time to train, many parameters
      - Feature engineering less critical, it turns to be architecture engineering
      - Overfitting 
        - L1/L2 regularisation over weights
        - early stopping
        - dropout units
      - Contain a number of random variables, hard to interpret
    - Advantages 
      - Compact model, can be applied to both classification and  regression.



### Deep Learning

- Combination of “deep” models with sufficient data to train the model

- One key facet of deep learning is **<u>representation learning</u>**, i.e. transformation of raw inputs into a suitable representation

  - Document representation
    - frequencies
    - Word embedding matrices
  - image representation 
    - RGB pixels matrices
    - Grey scale matrices

- Representation Learning 

  - Embedding (dense real-valued vector) advantages 
    - fewer features
    - Feature engineering easier
    - represent an instance by a combination of embeddings, allowing us to use the trained network for other problems
  - word2vec
    - continuous bag of words (CBOW)
    - for each word predict from its context words which ignore sequence
    - Nagative sampling is used to keep the word away which are not going to fit the original context
    - Simple feed-forward neural network (without a hidden layer), using logistic regression as the objective function

- Convolutional Neural Networks 

  - Staple of deep learning

  - Often use ReLU since

    1. It is fast to differentiate
    2. Tends to avoid the vanishing gradient problem

  - convolutional layers + max pooling layers + fully-connected layers

  - Deep convnets → ReLU activation function 

    - fast to differentiate
    - tends to avoid the “vanishing gradient” problem

  - Convolution Layer

    - Kernel
      - overlaid on different sub-regions of the image, and combined through an element-wise product
    - Stride
      - defines how many positions in the image to advance the kernel on each iteration

  - Pooling

    - kernel and stride

    - maxpooling
    - Averagepooling

- Deep Learning Overview

  - Advantage 
    - Huge impact on vision and speech recognition tasks
    - Possible to model much larger contexts
    - Easy to combine different input modalities
  - Disadvantage 
    - Cost in architecture engineering
    - Expensive to train on large dataset
    - Overblown claims about the capabilities of deep learning, hard to reproduce