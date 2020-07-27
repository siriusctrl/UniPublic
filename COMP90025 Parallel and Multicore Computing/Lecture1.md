# Introduction



## What is parallel computing

- Subset of HPC, includes as other aspects that are not concerned with parallelism
  - Cache techniques
  - Data structure
  - Algorithm specialization
  - I/O optimization
  - Instruction reorganization 
  - Optimizing compilers
- A way to achieve high performance
- Requires parallel architectures
  - No single architecture suits every problem
- Sometimes parallelism is not effective
- Big gap between parallel computing and theory and practice is possible





## Notations

- $O$ is the lower bound of a function
  - Where the original function $g$ grows no faster than (a constant time of) function $f$
  - $|f(n)| \leq c|g(n)|$
- $\Omega$ Is the upper bound
  - Where the original function $g$ grows no slower than (a constant time of) function $f$
- If $O(g(n)) = \Omega(g(n))$ 
  - $\Theta(g(n)) = f(n)$



## Models

### RAM



### PRAM

- EREW
  - exclusive read, exclusive write
- CREW
  - concurrent read, exclusive write
- CRCW
  - concurrent read, concurrent write
- ERCW
  - exclusive read, concurrent write



#### Simultaneous Write Conflict Resolution

- COMMON
  - Value is written $\iff$ all processors write the same value
  - Otherwise, error condition may be flagged
- ARBGITRARY
  - A process is randomly picked to write to the memory
  - Randomness may or may not be usable
  - The algorithm should work regardless of which processor is picked
- PRIORITY
  - The processor with the lowest identifier among the conflicting processors can write to the memory
- COMBININING
  - A function of the conflicting values is written
  - Requires defining the combining operation



#### Variations

- Any algorithm that runs on a <u>EREW PRAM</u> will run on a <u>CREW PRAM</u>
  - ==Why? Can we guarantee the correctness in this case?==
- Any algorithm that runs on a <u>CREW PRAM</u> will run on a <u>COMMON CRCW PRAM</u>
- 

