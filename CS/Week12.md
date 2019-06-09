### Spectre Vulnerability

- Goal: Read memory we shouldn’t be able to
- Kernel memory is in process address space
- Javascript is executed in a “sandbox” within a browser’s process; it is not allowed to access the main process’s data
- Techniques
    - Misleading branch prediction
    - Speculatively execute illegal code in victim process
    - Observe impact on cache in spectre process
        - Side channel: Way of communicating that was not intended for communication
        - Cache-based side channel: reads data from well-spaced memory addresses
            - Before the attack, Spectre flushes the cache
            - Access to most cache lines is slow; only one will be fast
        - It is possible to use the ill-gotten data to make a change to the “micro-architectural state”
  - All register in CPU
- Ways of inducing speculative execution
    - Inside sandbox: attack code written by others in our address space
    - eBPF
        - VMs allow guests to use extended BPF
        - A Spectre gadget written in eBPF can leak hypervisor code
