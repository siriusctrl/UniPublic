### feature selection

- Wrapper
  - Aim
    - Choose subset of attributes that give best performance on the development data (w.r.t a single learner)
  - How it works
    - Train the model on all combination of the features, and chose the one with best feature set.
  - Advantages
    - We can find the optimal feature set for a single learner
  - Disadvantages
    - Extremely time consuming, especially on large data set.
  - Improvement
    - Greedy approach
      - Train and evaluate model on each single attribute
      - 

