## Link Layer

- Services
  - Framing 
    - Parse a sequence of bits into frames
  - Error control
    - Correct bit errors, or discard error frames
  - Flow control
    - Stop sender sending if the receiver is not ready to receive
- Similar as transport layers 
  - point to point (two sides of a link)
  - **Not** end-to-end (over the whole network)



### Hub

- ![image-20190605125415973](assets/image-20190605125415973.png)
- A wiring pattern based on running individual cables to each machine from a hub
- Mitigated wiring problems, but increased cabling complexity and cost
  - Particularly around the hub
  - Even though the cable was considerably thinner
- Hub acts as if all cables are soldered together, every frame that comes in is sent out along all other lines
- Problems
  - Fixed capacity that is being shared by all hosts
  - As the number of host increase their share of the network capacity is reduced dramatically.
  - The alternative was switched Ethernet

### Bridges

- A bridge connects two LANs with the same “link-layer”