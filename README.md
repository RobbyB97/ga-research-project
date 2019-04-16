## Genetic Algorithm vs. Random Agent
___
#### Random agent:
The random agent is the control, for which every GA solution is compared to. A queen is placed randomly on each row of the board. It keeps running until it finds a goal state.
___
#### Genetic Algorithm
The genetic algorithm employs GA techniques to be as fast as possible at finding a solution. It is different for every trial.
___
### Trial 1
* (10,000 GA and RA solutions)
* #### Genetic Algorithm
  1. Create and execute 100 random chromosomes
  2. Get the best 20% (determined by number of conflicts)
  3. Splice them randomly
  4. Execute 20 spliced chromosomes
  5. Get the best 20%
  6. Splice them randomly
  5. Execute 4 spliced chromosomes
