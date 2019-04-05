## Lecture 1

### Instance-based learning (IBL)

- IBL algorithms are supervised learning algorithms
- Require labelled data
- Directly “learn-by-example”
  - Input
    - instances
  - Model
    - Function that map instances to labels



### Comparison

- Similarity
  - Jaccard Similarity
    - $sim(A, B) = \frac{|A \cap B|}{|A\cup B|}​$
  - Dice Coefficient
    - $sim(A, B) = \frac{2|A\cap B|}{|A|+|B|}$
    - Since there are 2 intersection part in $|A| + |B|$
  - Feature vectors (very often used in NLP)
    - A vector locates an instance as a point in an n-D space. The angle of the vector in that space is determined by the relative weight of each term.

- Distance

  - Euclidean Distance ($L_2$ distance)

    - $d(A,B) = \sqrt{\sum^n_{i=1}(a_i-b_i)^2}​$

  - Manhattan Distance ($L_1​$ distance)

    - $d(A,B) = \sum^n_{i=1}|a_i-b_i|​$

  - Cosine Similarity

    - $cos(P, Q) = \frac{pq}{|p||q|} = \frac{\sum_i p_iq_i}{\sqrt{\sum_ip_i^2}\sqrt{\sum_iq_i^2}}$

      

### Nearest Neighbour

- 