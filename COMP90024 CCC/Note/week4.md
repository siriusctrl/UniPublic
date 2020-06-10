# Week4 - The Spartan HPC System

### Supercomputer

- Any single computer system that has exceptional processing power for its time.

### HPC - high performance computing

- It is any computer system whose architecture allows for above average performance
- A collection of smaller computers strapped together with a high-speed local network

### Parallel and Research Programming

- Parallel computing refers to the submission of jobs or processes over multiple processors and by splitting up the data or tasks between them
- Research computing is the software applications used by a research community to aid research.

### Flynn’s Taxonomy and Multicore System

- Over time computing systems have moved towards multi-processor, multi-core, and often multi-threaded and multi-node systems.
- As computing technology has moved increasingly to the MIMD taxonomic classification additional categories have been added:
  - Single program, multiple data streams (SPMD)
  - Multiple program, multiple data streams (MPMD)

### Things are more important than performance

- Correctness of code and signal
- Clarity of code and architecture
- Reliability of code and equipment
- Modularity of code and components
- Readability of code and hardware documentation
- Compatibility of code and hardware

### Terms from the exam

- Data parallelization
  - Split data into chunk and process each chunk in parallel (just like assignment 1)
- Compute parallelization
  - Computation is not bound by data, for example, you have a for loop that create thousands and thousands of threads but each of them should run independently
- Wall-time
  - The limit you say how long your program will run
  - If too long
    - Then others may suffer from resource starvation
  - If too short
    - The job may not finish in this short period

