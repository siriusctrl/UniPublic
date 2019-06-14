### Logistic regression

- It is a **linear** classification algorithms.

  - Works well when data is linear separable.

- Output is probability of a class

- Use **logistic function (sigmoid)** to make sure the probability is smooth and in range of [0,1]

  - $P(c|x) = \frac{1}{1+e^{-(\beta x)}} = h_\beta(x)$ 
  - Where $\beta x$ is the results of linear regression

- Compare NB and LR

  - In NB, we are trying to maximize $P(x_i|c_j)$
  - In logistic regression we model $P(c_j|x_1,x_2,…,x_D)$ directly

- Using gradient descent to learn the $\beta$ 

  - We want the probability belongs to one class to be 1 and the other to be 0
  - In this case, we have the likelihood function
    - $P(Y|X;\beta) = \prod\limits^{N}_{I=1}(h_\beta(x_i))^{y_i} * (1-h_\beta(x_i))^{1-y_i}$
    - Where $y_i$ can only take 0 or 1 to indicate which class it belongs to
    - This is a Bernoulli distribution
    - Take log of it and use gradient ascent to maximize it

- LR for multi-class problem

  - Chose any class to be pivot, so that we can conclude linear relation between different class
  - Which is
    - $log\frac{P(A|x)}{P(C|x)} = \beta_A*x$
      - The larger the fraction, the more likely the instance belongs to non-pivot (Class A), the smaller the value, the more likely the instance belongs to pivot (Class B).
    - $P(A|x) = P(C|x) * exp(\beta_A *x)$
    - Similar for $P(B|x)$
    - $P(A|x) + P(B|x) + P(C|x) = 1$
    - Probability of all class sum to 1
    - $P(A|x) = \frac{1}{1+\sum\limits_{k \in A,B} -e^{\beta*x}}$
    
  - Therefore, we could express all other class in terms of all other class.

- 

