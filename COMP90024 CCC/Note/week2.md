# Week 2 - Domain Driver --  why we need Cluster and Cloud Computing

## Compute Scaling

- Massive amount of data generated among a time requires compute infrastructure
  - Mapping the sky with data from tele-scope
- Cloud Computing in Different Domains
  - **High energy physics**
    - 
  - Astrophysics
  - **Macro-micro simulations**
  - Electronics
  - Arts and humanities
  - Life sciences
  - Social sciences
    - Aurin
  - Clinical sciences
  - Data sharing and ethics
  - e-Health
    - **Security**
  - environmental
  - social
  - geographical
  - Genome



## Versioning System

### What

- Version control = Revision control = Source control
- Managing changes to
  - Documents
  - programs
  - Large websites
- Revision numbers
  - Letters or numbers used to represent each change



### Why

- Work simultaneously on big projects and keep track of changes
- Be able to simply revert back to a specific checkpoint in any project
- Create necessary redundancy by duplicating codes and resources to avoid data loss



### Types

- Local
  - This tool basically works by keeping patch sets using a special format in the version tracker and is stored in local hard disk. You may lose all data if local hardware failed.
  - Example
    - Revision Control System (RCS)
- Centralised
  - In this approach, all the changes in the files are tracked under the centralized server. The centralized server includes all the information of versioned files, and list of clients that check out files from the central place. In this case, you could have more control over the system.
  - Examples
    - Subversion(SVN)
    - Concurrent version system (CVS)
- Decentralised
  - The clients completely clone the repository including its full history, If any server dies, any of the client repositories can be copied on the the server which help restore the server and prevent single point of failure. However, in this case, you cannot, for example, have a fine-grained control of access for a single repository.
  - Example
    - Git