# Multicast



## Types

- Operations
  - X-multicast(g, m)
  - X-deliver(m)
  - X is 
    - B
      - basic
    - R
      - reliable
    - FO
      - FIFO order
    - CO
      - Causal order
    - TO
      - total order
- <img src="assets/image-20200624152858858.png" alt="image-20200624152858858" style="zoom:33%;" />



## Basic Multicast (B-multicast)

![image-20200624152950424](assets/image-20200624152950424.png)



## Reliable Multicast (R-multicast)

- Analysis
  - Integrity
    - ![image-20200624153054109](assets/image-20200624153054109.png)
  - Validity
    - If a correct process multicasts message m, then it will eventually deliver m (liveness)
  - Agreement
    - ![image-20200624153119943](assets/image-20200624153119943.png)
  - Agreement and validity together ensure overall liveness
    - If one process delivers a message $m$, then $m$ will eventually be delivered to all group members

- Algorithm
  - ![image-20200624153230274](assets/image-20200624153230274.png)

- Compare with B-Multicast
  - ![image-20200624153253236](assets/image-20200624153253236.png)

