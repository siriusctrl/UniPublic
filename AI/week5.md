### Learning Strategy

- Book Learning
  - Learn sequence of moves for important positions
  - Problem
    - How do we recognise which moves were important?
- Search Control Learning
  - Learn how to make search more efficient
  - Since,
    - Order of move generation affects $\alpha - \beta$ pruning
    - Learn a classifier to predict what depth we should search to based on current states.
- Gradient descent Learning
  - Eval(s) = $wf(s) $
  - Update using gradient descent
    - $w_i \leftarrow w_i - \frac{\partial E}{\partial w_i}$
  - Use the MSE to measure the error
    - Error = $\frac{1}{2}\sum(t-z)^2$
    - Where $z$ is Eval(s) and $t$ is desired output
  - Combine the error function
    - $\frac{\partial E}{\partial w_i} = \frac{\partial[\frac{1}{2}(t-z)^2]}{\partial z} \frac{\partial z}{\partial w_i}\\ \ \ \ \ \ \ =(z-t)\frac{\partial z}{\partial w_i}\\ \ \ \ \ \ \ = (z - t)f_i(s)$
    -  We normally add a learning rate when updating the parameters
      - $w_i \leftarrow w_i - \eta(z-t)f_i(s)$ 



### Reward Assignment

- Problems
  - Delayed reinforcement
    - Reward resulting from an action may not be received until several time steps later, which also slows down the learning
  - Credit assignment
    - Need to know which actions was responsible for the outcome
- TD (Temporal Difference Learning) — reinforcement learning algorithm
  - TD learning is for multi-step prediction
  - Correctness of prediction not known until several steps later
  - Intermediate steps provide information about correctness of prediction
  - Basic idea
    - Update weight in evaluation function to reduce differences in rewards predicted at different levels in search tree.
- TDLeaf($\lambda$)
  - Parameters
    - eval(s, w)
      - Evaluation function for state s with parameters $w = [w_1,..,w_k]$
    - $s_1,…,s_N$
      - The N states that occurred during a game
    - $r(s_N)$
      - Reward based on outcome of game ${+1, 0, -1}$
    - $s^l_i$
      - Best leaf found at max cut-off depth using minimax search starting at state $s_i$
  - We can convert an evaluation score into a reward using
    - $r(s^l_i, w) = tanh(eval(s^l_i,w))$
    - Where tanh squashes the evaluation score into the range [-1,1]
  - For $i = 1,…,N-1$
    - Compute temporal difference between successive states
      - $d_i = r(s^l_{i+1}, w) - r(s^l_i,w)$
    - Then update each weight accordingly with learning rate $\eta$
    - $w_j \leftarrow w_j + \eta\sum\limits^{N-1}_{i=1}\frac{\part r(s^l_i,w)}{\part w_j}[\sum\limits^{N-1}_{m=i}\lambda^{m-i}d_m]$
    
    - $\lambda$ Control the the how far the influence of a action propagate
      - $\lambda = 1$ Look towards the final true reward
      - $\lambda = 0$ Look towards the next move