## Genetic Algorithm vs. Random Agent
___
#### Random agent:
The random agent is the control, for which every GA solution is compared to. A queen is placed randomly on each row of the board. It keeps running until it finds a goal state.

#### Genetic Algorithm:
The genetic algorithm employs GA techniques to be as fast as possible at finding a solution. It is different for every trial.
___
### Trial 1
* (10,000 GA and RA solutions)
#### Genetic Algorithm
1. Create and execute 100 random chromosomes
2. Get the best 20% (determined by number of conflicts)
3. Splice them randomly
4. Execute 20 spliced chromosomes
5. Get the best 20%
6. Splice them randomly
7. Execute 4 spliced chromosomes
#### Notes
1. The mean average number of attempts for the GA to find a goal state (75848) was less than half than the RA control (182556).
2. Although this is not recorded, from all of the executions that I watched most of the GA solutions seemed to be 2nd or 3rd generation (randomly spliced, not randomly generated).
3. The effectiveness of the fitness function seems apparent from trial one, both from the mean average of the data and the frequency of spliced chromosomes finding goal states.
___
### Trial 2
* (10,000 GA solutions)
* Due to the very high success rate of the fitness function, the best way to improve the speed of this genetic algorithm seems to be to put more emphasis on splicing chromosomes. The first trial would take the best chromosomes and splice them only once. If this didn't yield a positive result, it would crop the best solutions again. For trial 2, each time the fittest chromosomes are cropped, they are spliced multiple times before the best solutions are cropped.
#### Genetic Algorithm
1. Create and execute 100 random chromosomes
2. Get the best 20% (determined by number of conflicts)
3. Splice them randomly
4. Execute 20 spliced chromosomes
5. Repeat steps 2 through 4 five times
6. Get the best 20%
7. Splice them randomly
8. Execute 4 spliced chromosomes
9. Repeat steps 7-8 twice
