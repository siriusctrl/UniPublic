### Bayesian Network

-  A **<u>simple</u>**, **<u>graphical notation</u>** for conditional independence assertions and hence for **<u>compact specification of full joint distribution</u>**
- Example
  - ![image-20190621230616254](assets/image-20190621230616254.png)
- Compactness
  - Growth linear with n $O(n*2^k)$, comparing to $O(2^n)$ for the full joint distribution.
- Global Semantics
  - Full joint distribution as product of the local conditional distributions
  - ![image-20190621231259631](assets/image-20190621231259631.png)
  - Given the graph
    - ![image-20190621231332372](assets/image-20190621231332372.png)

- Local Semantics
  - Each node is conditionally independent of its non-descendants given its parents
- Constructing Bayesian Networks
  - ![image-20190621232217585](assets/image-20190621232217585.png)



### Inference Task

- Simple queries — Computer posterior marginal $P(X_I|E=e)$

  - $P(NoGas|Gauge=empty,Lights=on, starts=false)$
  - Example
    - 

- Conjuncive queries

  - $P(X_i,X_j|E=e) = P(X_i|E=e)P(X_j|X_i,E=e)$

  