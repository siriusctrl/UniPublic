## Lecture 1 (Game Playing and Adversarial Search)

### Perfect play 

- Find best solution

### resource limit

- Find best solution with limit resources

### $\alpha-\beta$ pruning

- Inprove our search efficiency without change the result 



### Real World Game

- It has lots of limitations
  - Unpredictable opponent
  - Time limitations
    - Unlikely to find a goal, must approximate
- Some of the game are only have imperfect information, and depends on chance
  - Poker (cannot see the card of our opponents)
  - Bridge
  - Nuclear war
- Some of the game are deterministic but with imperfect information
  - battleship



### Representing a game as a search problem

- Need to consider
  - Inital state
    - How do we start the game
  - actions
    - How can one player move in the environment
  - Termial test
    - Win condition
    - Lose condition
    - Draw condition
  - Utility function (numeric reward for outcome)
    - Chess: +1,0,-1
    - Poker: cash won or lost
- Method
  - Minimax
    - Assumption: our opponent is rational and won't let us always do the best decision.
    - Deterministic perfect-information games
    - Maximise the minimal value in successor (we should chose A1 to go in the following example)
    - ![image-20190326164402568](assets/image-20190326164402568.png)
    - Properties
      - Complete
        - Yes, if the tree is finite
      - Optimal
        - Yes, if against an optimal opponent
        - Otherwise, no
      - Time complexity 
        - $O(b^m)$
      - Space complexity (DFS exploration)
        - $O(bm)$
    - Resource limits 
      - Cutoff test
        - Depth limit
        - Quiescence search
          - If there is no significant move in successor, we stop searching, otherwise, keep searching deeper for a little bit
      - Evaluation function
        - Estimated desirability of position
          - Like alphaZero using residual-CNN to estimate how likely we are going to move to that state
        - Typically linear weighted sum of features depends on how important they are
          - $eval(s) = w_1f_1(s) + w_2f_2(s) + … + w_nf_n(s)$
  - Minimax cutoff
    - 