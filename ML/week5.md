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
      - Train and evaluate model on each single attribute.
      - Do, until convergence
        - Train and evaluate model on best attributes, plus each remaining single attribute.
        - Choose best attribute out of the remaining set.
      - Pros
        - Normally converges very quick in practice
      - Cons
        - Normally converge to a sub-optimal solution
        - Assume in dependance of attributes
    - Ablation approach
      - Start with all attributes, each time remove the most unhelpful one until divergence.
      - Terminate when performance starting to degrade by more than $\epsilon $
      - Pros
        - At the start mostly removes irrelevant attributes
      - Cons
        - Also assumes independence of attributes
        - Actually does take $O(m^2)$ time, cycles are slower with more attributes
        - Not feasible on non-trivial data sets.
- Embedded
  - Some models actually perform feature selection
    - SVM and Logistic Regression
    - Decision Tree and Random Forest
  - Often benefit from other feature selection approaches
- Filters
  - Consider each attribute separately
  - Try to control inter-dependence



### Filtering method

- Pointwise Mutual Information (PMI)

  - Independent
    - $\frac{P(A,C)}{P(A)P(C)} = 1$, if independant
    - If LHS >> 1, attribute and class occur together much more often than random
    - If LHS $\approx$ 1, most likely independent
    - If LHS << 1,  attribute and class are negatively correlated
  - PMI(A = a, C = c) = $log_2\frac{P(a,c)}{p(a)P(c)}$ 
  - Higher PMI, more correlation with class
  - Problem
    - Could not show the case for all case, since one attribute may works well for one class but not the others.

- Contingency table and MI

  - Can be used to calculate PMI, MI and chi-square

  - ![image-20190409153342377](assets/image-20190409153342377.png)

    

- MI(mutual information)

  - MI(A,C) = $P(a, c)*PMI(a,c) \\+ P(\bar{a},c)*PMI(\bar{a},c) \\+ P(a,\bar{c})*PMI(a,\bar{c}) \\+ P(\bar{a}, \bar{c}* PMI(\bar{a}, \bar{c}))$ 
    - We still use $0log0 \equiv 0​$
  - Problems
    - Biased toward common, uninformative features

- Chi-square

  - $\chi^2 = \sum\limits^r_{i=1}\sum\limits^c_{j=1} \frac{(O_{i,j}-E_{i,j})^2}{E_{i,j}}$

  - Normally expect value are uniform distribution

  - Problems

    - Biased toward rare, informative features, since we squaring the difference
    - If a feature is seen rarely but always with a given class, it will be seen as "good"

    

### Data Type Issue

- Nominal attributes
  - Use one-hot
  - Expand the contingency table
- Continuous attributes
  - Fit the empirical data by using normal distribution
  - Discretised the values
- Ordinal attributes (low, med, high or 1,2,3,4)
  - Treat as binary
    - Count frequency
  - Treat as continuous
  - Treat as nominal
    - Throw away ordering