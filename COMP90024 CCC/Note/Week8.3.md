# Week 8.3 Serverless - FaaS



## What is?

### Definitions

- FasS is also know as Serverless computing
- Develop software applications without bothering with the infrastructure
  - Especially scaling-up and down as load increases or decreases
- It is more Server-unseen than Server-less
- A FaaS service allows functions to be 
  - added
  - removed
  - updated
  - executed
  - auto-scaled
- FaaS is an extreme form of *micro-service* architecture



### Why Functions

- A function in computer science is typically a piece of code that takes in parameters and returns a value
- Functions are the founding concept of functional programming
  - One of the oldest programming paradigms
- Functions are (should be) 
  - free of side-effects
  - ephemeral
  - stateless
- Ideal for **<u>parallel execution</u>** and rapid **<u>scaling up and down</u>**



### Why Faas?

- Simpler deployment
  - The service provider takes care of the infrastructure
- Reduced computing costs
  - Only the time during which functions are executed is blind
- Reduced application complexity due to loosely-coupled architecture



### Applications

- Functions are triggered by events
  - Event-driven
- Functions can call each other
- Functions and events can be combined to build software applications
- Application Examples
  - A function can be triggered every hour, or every time disk space on a volume is scarce, or when a pull-request is closed in Github
  - Combining event-driven scenarios and functions resembles how user interface  software is built
    - User actions trigger the execution of piece of code



### FaaS Services and Framework

- Commercial
  - AWS Lambda
  - Google Cloud
  - Azure Functions
- Open source
  - OpenWhisk
  - OpenFaaS
  - Kubernetes Knative
- Difference
  - Open source choice can be easily deployed on your cluster, peered into, disassembled and improved by you



## Functions

### Side-effect Free Functions

- A function that does not modify the state of the system is said to be ***side-effect*** free, otherwise, it is not side-effect free
  - A function that takes an image and returns a thumbnail of that image
- Can be run in parallel easily and guaranteed to return the same output given the same input
- Side-effects are almost inevitable in a relatively complex system. 
  - Must carefully consider how to run functions with side effects in parallel, as typically required in FaaS environments.



### Stateful/Stateless Function

- Definition
  - A function output changes in relation to internally stored information, otherwise, it is a stateless function
  - Example
    - A function that adds items to a shopping cart

- Stateful function $\sub$ functions with side-effects
- Important as there are multiple instances of the same function, and there is no guarantee the same user would call the same function instance twice.



### Synchronous/Asynchronous Function

- By default functions in FaaS are synchronous
- Why async?
  - Function that takes longer time to return a result incur timeouts and lock connection with clients in the process
- Asynchronous functions return a code that informs the client that the execution has started and then trigger an event when the execution completes
- Publish/subscribe pattern, involving a queuing system, can be used to deal with async functions.



## OpenFaaS

### Properties

- Open-source framework that uses Docker containers to deliver FaaS functionality
- Every function in OpenFaaS is a Docker container, ensuring loose coupling between functions
  - Function can be written in different languages and mixed freely
- Functions are passed a request as an object in the language of choice and return a response as an object
- OpenFaaS can use either Docker Swarm or Kubernetes to manage cluster of nodes on which functions run
- By using Docker containers as functions, OpenFaaS allow to freely mix different languages and environments at the cost of **<u>decreased performance</u>** as containers are inherently heavier than threads
  - However, it is possible to reduce the size to only a few MBs

