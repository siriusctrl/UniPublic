### Classification Evaluation

> **Input**: set of labelled training instances
>
> **Model**: an estimate of underlying target function
>
> **Output**: prediction of the classes of the test instances

- Basic evaluation metric: Accuracy
  - $\frac{\text{number of correctly labelled test instances}}{\text{Total number of test instances}}$ 
  - how frequently the classifier is correct
- Need to split dataset
  - Training set
  - Test set
  - Evaluation set (not mentioned in lecture, but we need this)
  - Testing on training set tends to grossly over-estimate
- Premise
  - Inductive Learning Hypothesis
    - Any hypothesis found to approximate the target function well over training data set will also approximate the target function well over unseen test examples.
- Methods
  - Holdout
    - Pros
      - Simple to implement
      - Fairly high reproducibility
    - Cons
      - Size of the split affects estimate of the classifier's behaviour
        - Too many testing instances results in the learner does not have enough instance to learn the pattern.
        - Too many training instances results in the evaluation might not be representative. (High variance in estimation)
  - Repeated Random Subsampling
    - Like holdout but iterated multiple times. New training set and test are chosen each time but relative size of training-test is fixed across iterations.
    - Pros
      - Can averaging holdout method tends to be more reliable.
    - Cons
      - More difficult to reproduce (actually we can set a sequence of random seed to reproduce)
      - Instances overlap
      - Slower than holdout, since it about doing hold-out multiple times
      - Hard to decide a perfect train-test ratio
  - K-fold cross validation
    - Data split into a number of partitions k. Iterate through all of them, use one to test and others to train, then average the results.
    - Take rough the same amount of time as Repeated Random Subsampling
    - Very reproducible 
    - Minimize **<u>bias</u>** and **<u>variance</u>** of our estimates of how good is our model
    - How big is m?
      - Impact runtime and size of datas
        - \# of partition $\uparrow$ , runtime $\uparrow$, variance in performance estimates $\downarrow$ 
      - Most common choice k = 10 (occasionally, 5)
      - Best choice is k = \# of instances (leave-one-out cross-validation) but too slow in practice
- Stratification (inductive bias)
  - We assume the distribution in both seen and unseen data are the same
  - When doing hold-out and cross validation, need to make sure that the distribution in both class are the same.
    - Also called **<u>vertical sampling</u>**



### Evaluation Metrics

- 4 possible class (needs to specify interesting class and an uninteresting class)
  - True Positive (TP)
  - True Negative (TN)
  - False Positive (FP)
  - False Negative (FN)
- Some useful figures
  - ACC = $\frac{\text{TP + TN}}{\text{TP + FP +FN + TN}}$
  - ER = 1 - ACC
  - Precision: How often are we correct ,w.r.t the class that we are interested in
    - $\frac{\text{TP}}{\text{TP + FP}}$ 
  - Recall: proportion of the class we interested in that we correctly predicted.
    - $\frac{\text{TP}}{\text{TP + FN}}$ 
  - F-score (harmonic mean of precision and recall)
    - $F_\beta = \frac{(1+\beta^2)PR}{\beta^2P + R}$
    - We normally use $F_1$-score, with $\beta =1$
- Expand to multi-class scenario
  - Confusion matrix
    - ![image-20190325222555379](assets/image-20190325222555379.png)
  - Micro-averaging
    - Sum of all nominator / sum of all denominator
  - Macro-averaging (mean of each class)
    - $Precison_M = \frac{\sum\limits^c_{i=1}Precision(i)}{c}$
    - $Recall_M = \frac{\sum\limits^c_{i=1} Recall(i)}{c}$
  - Weighted-averaging (based on the proportion of instances in that class)
    - $Precison_W = \sum\limits^c_{i=1}(\frac{n_i}{N}) Precision(i)$
    - $Recall_W = \sum\limits^c_{i=1}(\frac{n_i}{N}) Recall(i)$



### Results Comparison

- Baseline
  - Naive method which we would expect any reasonable well-developed method to better than that.
  - Random baseline
    - Randomly assign a class to each test instance (normally just calculate the probability distribution)
    - Randomly assign a class $c_k$ to each test instance, weighting the class assignment according to P($c_k $)
  - Zero-R (most commonly used baseline)
    - Classify all instances according to the most common class in the training data
    - <u>Inappropriate</u> if the majority class is <u>FALSE</u> and the learning task is to identify needles in the haystack
  - One-R
    - Making predictions using only one attributes. **<u>Decision Stamp</u>** is created for each attribute but only the one with least error rate will be kept.
    - Pros
      - Simple to understand and implement
      - Simple to comprehend the results
      - Surprisingly good results
    - Cons
      - Unable to capture attribute interactions
      - ==Bias when attributes with many possible values==
        - Why it is the case?
- Benchmark
  - Established trivial technique which we are pitching our method against it.



### ID3 Algorithm for Decision Tree

- Construct decision tree using divide-and-conquer

  - ```pseudocode
    def ID3(Root):
    	if all instances at root have same class
      then stop
      else
      	1. selet an attribute
      	2. partitioning root node instances
      	3. create a branch for each attribute value
      	4. partition up root node instances according to each value
      	5. call ID3(LEAF) for each leaf node LEAF
    ```

- Since decision tree is a sequence of if-condition, it can be written in a disjunction form

- This algorithm searching a space of hypotheses for one that fits the training examples.

  - The hypothesis space is the set of possible decision trees.

- Pros

  - Highly regarded among basic supervised learners
  - Fast to train, even faster to classify

- Cons

  - Susceptible to the effects of irrelevant features



### Criterion for Attributes Selection

- Entropy
  - A measure of unpredictability
  - Given a probability distribution, the information required to predict an event is the **<u>distribution's entropy</u>** or **<u>information value</u>**
  - $H(x) = -\sum\limits^n_{i=1} P(i)log_2P(i) $
  - If most of the probability mass is assigned to a single event, **<u>entropy is low</u>** and the event is **<u>predictable</u>**. Otherwise, entropy is high and the event is unpredictable.
- Mean Information
  - Weighted average for child entropy
  - Mean Info($x_1$… $x_m$) = $\sum\limits^{m}_{I=1}P(x_i)H(x_i)$
- Information Gain (IG)
  - Difference between the entropy after and before the splitting the tree
  - If the entropy decreases, then we have a better tree
  - Parent entropy - child mean information
- Shortcomings
  - IG tends to prefer highly-branching attributes
    - A subset of instances is more likely to be homogeneous if there are only a few instances
    - Attribute with many values will have fewer instances at each child node.
  - This may result in overfitting
- Solution
  - Gain Ratio (GR)
    - Reduces the bias for information gain towards highly-branching attributes by normalizing relative to the **<u>split information</u>**
  - Split Info (SI) (aka Intrinsic Value)
    - Entropy of a given split (evenness of the distribution of instances to attribute values)
    - Discourages the selection of attributes with many uniformly distributed value.
  - $GR(R_A|R) \\= \frac{IG(R_A|R)}{SI(R_A|R)}  \\= \frac{IG(R_A|R)}{H(R_A)} \\= \frac{H(R)-\sum\limits^{m}_{i=1}P(x_i)H(x_i)}{-\sum\limits^{m}_{i=1}P(x_i)log_2P(x_i)}$



### Stopping Criteria

- Stop if all IG = 0

  - Means there are no improvement
  - This helps to ensure that the tree remains compact (Occam's Razor)

- More practical

  - Choose best attribute only if IG/GR is greater than some threshold $\tau$

- Using pruning to remove undesirable branches with few instances or small IG/GR improvements

- Run out of attributes but can still improve $\to$ probably evidence that the given attributes are insufficient

  



