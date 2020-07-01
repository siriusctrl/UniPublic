# Transaction Recovery

## Why?

- To ensure 
  - failure atomicity
    - Effects of transactions are atomic even when the server crashes.
  - durability
    - Objects are saved in permanent storage and will be available indefinitely thereafter
- Service provides failure atomicity
  - Which means effects of transactions are atomic even when server crashes
- To simplify
  - We assume all running server store their object in <u>volatile memory</u>
  - All of its committed objects are in a recovery file in <u>permanent storage</u>
- Recovery consists of restoring the server with the latest committed versions of all of its objects from its recovery file



## Recovery manager (RM)

- Tasks
  - To save objects in permanent storage for committed transactions
    - In recovery files
  - To restore the server’s objects after a crash
  - To reorganize the recovery file to improve the performance of recovery
  - To reclaim storage space
    - In the recovery files
- <u>Media failures</u> also need to be covered, using mirrored disks or copies at a different location
  - Disk failures affecting the recovery file
  - Need another copy of the recovery file one an independent disk



### Intention list

- Each server records an intentions list for each of its currently active transactions
- An *intentions list* 
  - contains a list of the object references of all the objects that are altered by the transaction
- When a transaction commits, the intentions list is used to identify the objects affected
  - The committed version of each object is replaced by the tentative one
  - The new value is written to the server’s recovery file
- In 2PC, when a participant says it is ready to commit, its RM must record its intentions list and its objects in the recovery file
  - It will be able to commit later on even if it crashes
  - When a client has been told a transaction has committed, the recovery files of all participating servers must show that the transaction is committed
    - Even if they crash between prepare to commit and commit
- Entry example
  - ![image-20200626180045417](assets/image-20200626180045417.png)



### Logging

- It contains a log of the history of all the transactions at a server

  - Including objects, intentions lists and transaction status
  - In happened order
  - A recent snapshot + a history of transactions after the snapshot
  - During normal operation the RM is called whenever a transaction prepares commits or aborts
    - ![image-20200626181040262](assets/image-20200626181040262.png)

  - Example
    - ![image-20200626181431381](assets/image-20200626181431381.png)
    - In P3
      - First line is status
      - Following by two intentional list
      - The last one is the pointer to the previous transaction before change

- Recovery of <u>objects</u>

  - ![image-20200626181756468](assets/image-20200626181756468.png)
- Uncommitted value should be ignore
  - Idempotent since the server may crash in the middle of recovering
  
- Recovery of <u>two-phase commit</u>
  - ![image-20200626190716211](assets/image-20200626190716211.png)
  - Procedure
    1. In phase 1, 
       - when the coordinator is prepared to commit add a $prepare$ entry to its recovery file
         - Add another $coordinator$ entry to its recovery file
       - Before a participant can vote $yes$, its recovery manager records a $participant$ entry to its recovery file and adds an $uncertain$ transaction status to its recovery file as a <u>forced write</u>.
    2. In phase 2
       - Adds either a $committed$ or an $aborted$ transaction status to its recovery file
       - This must be a forced write, which will force all the buffered message to write to the recovery files.
       - RM of participants add a $commit$ or $abort$ transaction status to their recovery files according to the message received from the coordinator.
       - When a coordinator has received a confirmation from all of its participants
         - Its RM adds a $done$ transaction status to its recovery file.
  - ![image-20200626190722793](assets/image-20200626190722793.png)
  - ![image-20200626190729763](assets/image-20200626190729763.png)

