## Auction

- Multi-agent systems

- Mechanism design

  - How to design a game that results in maximizing a global utility function in a multi-agent system, given that each agent pursues their own rational strategy
  - We focusing on auction, which consists of three main components
    - A **<u>language to describe</u>** the allowable strategies an agent can follow
    - A **<u>protocol for communicating bids</u>** from bidder to the auctioneer, and
    - An **<u>outcome rule</u>**, used by the auctioneer to determine the outcome

  

### Dimensions of auction protocols

- Winner determination — which bidder wins, and what do they pay?
  - First-price auctions
    - Bidder with highest bid is allocated the good
  - Second-price auctions
    - Bidder with highest bid wins but pays the auctioneer the price of the second highest bidder.
- Knowledge of bis — who can see the bids?
  - Open-cry
    - Every bidder can see all bids from all other bidders
  - Sealed-bid
    - Bidder can see it own bids, not those of other bidders
- Order of bids — in what order can bids be made?
  - One-shot
    - Each bidder can make only one bid
  - Ascending
    - Each successive bid must exceed the previous bid
  - Descending
    - Auctioneer starts from a high price, and each bid must be lower than the previous bid.
- Number of goods — how many goods are for sale?
  - Single good
  - Many goods
    - Combinatorial auction
  - We focusing on single good!



### Value that Affecting Mechanism Design

- Common Value
  - The worth of the good is the same for all bidders, but that worth is unknown and must be estimated by each bidder.
  - e.g. an ounce of gold
- Private Value
  - Each bidder has a utility value that reflects the worth of the good to the bidder
  - A golden earring



### Desirable Properties

- Efficient
  - The goods go to the agent who values them the most
- Discourage collusion
  - The auction mechanism should discourage illegal or unfair agreements between two or more bidders to manipulate prices
- Dominant strategy
  - There exists a dominant strategy for bidders, where a strategy is dominant if it gives the bidder a better pay-off than any other strategy
- Truth-revealing
  - The dominant strategy results in bidder revealing their true value for the good





### Type of Auction

- English auction (ascending-bid)
  - First-price, open-cry, ascending
  - Properties
    - There is a **<u>dominant strategy</u>**
      - Bid higher than others, but smaller than your value
    - Efficient
      - Too high
        - Bidder who values good may not bid
      - Too low
        - Seller may lose revenue
    - Susceptible to collusion
    - Winner's curse
- Dutch auction (descending-bid)
  - Open-cry, descending
  - Properties
    - Similar problem as English auction
- First-price sealed-bid auction (FPSB)
  - Properties
    - **<u>No</u>** dominant strategy
      - Bid less that your true value, but how much less depends on other agents' bid
    - May not be **<u>efficient</u>**
    - Make it hard for collusion
    - Much simpler
- Vickrey Auction (SPSB)
  - Price paid by winner is the price of second-highest bid
  - Properties
    - Efficient
    - Truth-revealing
    - Overcome the winner's curse
    - Harder for collusion
    - A bit counter-intuitive for human bidders





