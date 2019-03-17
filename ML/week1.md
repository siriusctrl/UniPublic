## lecture 1
What is ML, differences between ML and Data mining or AI.

## lecture 2
> **Instance** : A real world examples of a concept  
> **Attributes** : measuring aspects of an instance  
> **Concepts** : What we want to learn in the form of labels or classes    

#### Style  of concept (different kinds of task) 
- Classification 
  - **supervised** : prior knowledge of the relationship between instance and labels required
  - Learning predicting which class does the new object belonging
  - provide with set of classified training data for learning, need to give predictions about which class does the test instance in
    ![FF057575-BF1B-44D4-86EF-D180A001F9CA](assets/FF057575-BF1B-44D4-86EF-D180A001F9CA.png)

- Clustering
  - **Unsupervised** : not prior knowledge required
  - grouping similar instances together without giving the labels of all the instances.
- Regression
  - **Supervised**
  - predicting a numeric quantity
  - a good regression is acceptably close to the true value
- Association Learning
  - detecting useful associations or structures between attribute values
  - we can use the new rule to infer an attributes values based on another

#### Different type of attribute
1. Nominal Quantities (**Categorical**, discrete)
  - values are distinct symbols, theirs no relation between them
  - can only perform equality tests
  - **one-hot** is the most salient method to process categorical data
2. Ordinal Quantities
  - explicit order in-between possible values but **no** numerical distances are defined
3. Continuous Quantities
  - real-valued attributes with well-defined zero point and no upper bound
  - numerical distances are defined between values
  - allow all mathematical operations

#### real world problem and world flow
1. Data Wrangling
2. Different Data Representations
  * e.g.  CSV, RAFF, etc 
3. Missing Values
  * 	Sometimes the missing value maybe really important, for example medical examination.
4. Inaccurate Values
  * maybe caused by unintentional (bad sensor on a robot) or deliberate (wrong post codes)
5. May cause some ethical problem
  * race & sex in medical application: OK
  * in loan or student application selections: unethical