## Lecture 1

### Timer

- There is **only one** timer in sender
- Simplified procedure
  - Data received from application layer
    - Create a TCP segment
    - Start a timer, if timer is not running
  - timeout
    - Retransmit oldest not-yet-acknowledge segment
    - Start timer
  - When received a ACK, if there are any not-yet one
    - Restart timer again
  - Problems
    - The timeout period can be relatively long, delay resending the lost packet, thereby increasing the end-to-end delay.
  - Solution
    - Fast Retransmission
      - Count duplicate ACK received for a segment with sequence number y
      - Increase the duplicate ACK counter of segment y by 1
      - If this counter reaches to 3
        - Resend the segment y before the timeout
        - Reset the counter of segment y to 0
      - Why 3?
        - Sometimes receiver are out of order, but when it reach to 3, it is very likely that the packet is lost.



### TCP Flow Control

- To eliminate the possibility of the sender overflowing the receiver's buffer

  - Let the sender know how much **free buffer space** is available at the receiver.

  - 16 bits number in header

    ![image-20190402224949944](assets/image-20190402224949944.png)





## Lecture 2

