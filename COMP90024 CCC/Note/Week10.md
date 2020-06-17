# Week 10 Security and Clouds

### Why important

- Large communities will not engage if not secure
  - Medical community, industry, financial community
  - Or they will use their own internal resources
- Expensive to repeat some experiments
  - Huge machines running large simulations for several years
- Legal and ethical issues possible to be violated with all sorts of consequences
  - Data protection act violations and fines incurred
- Trust is easily lost and hard to re-establish



### Challenges

- Grids and Clouds (IaaS) allow users to compile codes that do stuff on physical/virtual machines
  - Highly secure supercomputing facilities compromised by single user PCs/Laptops
  - Need security technologies that scales to meet wide variety of applications
- Should try to develop generic security solutions
- Clouds allow scenarios that stretch inter-organisational security
  - Policies that restrict access to and usage of resources based on pre-identified users, resources



## Authentication

### Authentication

- Establishment and propagation of a user’s identity in the system
- Not checking what user is allowed to do, only that we know (can check) who they are
- Masquerading always a danger
- Public key infrastructures (PKI) underpins many systems
- Federated authentication
  - Try to access a resources but authenticate your identity somewhere else
  - You login credential shared by the federation
- Shibboleth model (Decentralised Authentication)
  - ![image-20200610161324054](assets/image-20200610161324054.png)
  - Trust is the essential part
  - Pros
    - Powerful and convenient since you only need on username and password to login and access many resources
  - Cons
    - Protocols are static and not dynamic
      - You can’t assign a random role to someone that let him to get access to the cancer database. (Example provided by Rich in Week 12 Zoom lecture2)
  - Why don’t we use this to access many other cloud-based system
    - They may not ***Trust*** each other to do the authentication
    - Since different organisation have different CA mechanisms.



### Past Exam

- [2015 Q5 B] Why isn’t Shibboleth used to access Cloud-based systems more generally?
  - <u>Static federation</u> as mentioned above
  - <u>Trust</u>
  - No single CA



### Public Key Cryptography

- Also call Asymmetric Cryptography
  - Private key
  - Public key
- Two key complementary but essential that cannot find out value of private key from public key
  - With private keys can digitally sign messages, documents and validate them with associated public keys
  - Check whether changed, useful for non-repudiation
  - Public key cryptography simplifies key management
    - Do not need to have many keys for long time
      - The longer keys are left in storage, more likelihood of their being compromised
        - Instead us public keys for short time and then discard
        - Public keys can be freely distributed
      - Only private key needs to be kept long term and kept securely



### Public Key Certificates

- Mechanism connecting public key to user with corresponding private key is Public key certificate
- It contains public key and identifies the user with the corresponding private key
- Central component of PKI is ***Certification Authority***(CA), which in charge of
  - Policy and procedures
    - How to’s, don’ts and do’s of using certificate
  - Issuing certificates
    - Often need to delegate to local **<u>Registration Authority</u>**
      - Prove who you are
      - **<u>RA</u>** is the individual organization who responsible for checking someone’s identity
      - A registration authority (RA) is an authority in a network that verifies user requests for a <u>digital certificate</u> and tells the certificate authority (CA) to issue it.
  - Revoking certificates
    - Certificate Revocation List (CRL) for expired/compromised certificates
  - Storing, archiving

 

## Authorisation

### Authorisation

- Concerned with controlling access to resources based on policy
  - Can this user invoke this service, make use of this data?
- Complementary to authentication
- Defining what they can do and define and enforce rules
- Approaches
  - Group Based Access Control
    - Our project VM
  - Role Based Access Control (RBAC)
  - Identity Based Access Control (IBAC)
  - Attribute Based Access Control (ABAC)
- Consider the passport vs frequent customer shopping experience
- Often realised through Virtual Organisations (VO)
  - Provide conceptual framework for rules and regulations for resources to be offered/shared between VO members.
  - Different domains place greater/lesser emphasis on expression and enforcement of rules and regulations

- Identity Provider
  - The place you got authenticated
  - ![image-20200610161324054](assets/image-20200610161324054.png)



### Technologies

- RBAC is typical model
  - <u>Roles</u> applicable to specific collaboration
    - roles often hierarchical
    - Role X $\geq$ Role Y $\geq$ Role Z
    - X can do everything and more than Y who can do everything and more than Z
  - <u>Actions</u> allowed/not allowed for VO members
  - <u>Resources</u> comprising VO infrastructure
- A policy then consists of sets of these rules
- Policy engines consume this information to make access decisions



## Other Challenges

### Single sign-on

- Define
  - Login once, but can access many more resources that potentially provided by other providers
  - When you login The university of Melbourne Cloud, you could also access the amazon cloud

- The Grid model needed
- Currently not solved for Cloud-based IaaS
- Non-Cloud developers to define/support this, does not auto support out of the box.



### Auditing

- Logging the actions by each user
  - When bad thing happen, we have the record

- Logging, intrusion detection, auditing of security in external computer facilities
  - Well established in theory and practice and for local systems
    - Less mature in Cloud environments
  - Tools to support generation of diagnostic trails
- Problem
  - The record are distributed most of time
- Solution
  - Use block-chain ledger to provide confidentiality of the log





### Deletion

- Data deletion with no direct hard disk
  - Many tools and utilities do not work
- Scale of data
  - Securely deleting a few MB easy enough, what about a few TB+?



### Liability

- Using contract to state the risk



### Licensing

- Many license models
  - Per user
  - Per server
  - Per organisation
  - Floating licenses
  - Fixed to machines
- Challenges with the cloud delivery model



### Workflows

- Many workflow tools for combing SoA service/data flow
- Many workflows models
  - Orchestration
    - centralised
  - choreography
    - decentralised
- Serious challenges of
  - defining
  - enforcing
  - sharing
  - enacting
- Security-oriented workflows



### The Ever Changing Technical/Legal Landscape

