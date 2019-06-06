### Spectre

- Spectre provides a way to access any data in any process's address space
  - Provided we can trick that process into performing a sequence of operations
- Memory is often in a process's address space, even if it should not be able to access it
  - Kernel memory is in process address space
    - No need to reload page table for system calls
    - CPU raises segmentation fault for accessing invalid address
  - JS is executed in a “sandbox” within a browser's process, it is not allowed to access the main process's data
    - Compiler adds code checking memory access is within bounds



### Side channels

- Way of communicating that was not intended for communication
  - Typically not controlled 
  - Used for smuggling data into or out of systems
- It is possible to use the ill-gotten data to make a change to the “micro-architectural state”
  - All register in CPU



