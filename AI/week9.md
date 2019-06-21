### Inference by enumeration

- Use hidden variable
  - ![image-20190621221706911](assets/image-20190621221706911.png)

- Problem

  - Worst case time complexity $O(d^n)$ where d is the largest arity
  - Space complexity $O(d^n)$ to store the joint distribution
  - Independent entry number are calculated by $2^n -1$

- Solution — conditional probability

  - ![image-20190621222320051](assets/image-20190621222320051.png)

  
  - Therefore, we could have
    - ![image-20190621222346716](assets/image-20190621222346716.png)