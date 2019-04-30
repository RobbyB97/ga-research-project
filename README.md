## Genetic Algorithm vs. Random Agent
This research project sets out to prove that Genetic Algorithms can be implemented to generate solutions efficiently. The toy problem being used for this project is the 8 Queens problem, where 8 queens must be placed on a chess board such that no queen is capable of capturing any other queen. The performance of the genetic algorithm (GA) is compared to the performance of a random agent. If the 8 Queens problem can be solved by the GA faster than the random agent on average, then the GA is efficient.
___
#### Random agent:
The random agent is the control, for which every GA solution is compared to. A queen is placed randomly on each row of the board. It keeps running until it finds a goal state.

#### Genetic Algorithm:
The genetic algorithm employs GA techniques to be as fast as possible at finding a solution. It is different for every trial.
___
### Control
* (10,000 RA solutions)
#### Random Agent Algorithm
1. Randomly generate column to place queen in row
2. Repeat step 1 for each row of the board
3. Check to see if any queen can capture another queen
4. Repeat steps 1-3 until a goal state is achieved
#### Results
* Mean average of attempts to find goal state: 182556
* Histogram:

![Histogram](./screenshots/random_agent.png)
___
### Trial 1
* (10,000 GA solutions)
#### Genetic Algorithm
1. Create and execute 100 random chromosomes
2. Get the best 20% (determined by number of conflicts)
3. Splice them randomly
4. Execute 20 spliced chromosomes
5. Get the best 20%
6. Splice them randomly
7. Execute 4 spliced chromosomes
#### Results
* Mean average of attempts to find goal state: 75848
* ~2.4x faster than the random agent
* Histogram:

![Histogram](./screenshots/ga_trial_one.png)
#### Notes
1. The mean average number of attempts for the control to find a goal state was 2.4 times higher than trial one.
2. Although this is not recorded, from all of the executions that I watched most of the GA solutions seemed to be 2nd or 3rd generation (randomly spliced, not randomly generated).
3. The effectiveness of the fitness function seems apparent from trial one, both from the mean average of the data and the frequency of spliced chromosomes finding goal states.
___
### Trial 2
* (10,000 GA solutions)
* Due to the very high success rate of the fitness function, the best way to improve the speed of this genetic algorithm seems to be to put more emphasis on splicing the fittest chromosomes. The first trial would take the best chromosomes and splice them only once. If this didn't yield a positive result, it would crop the best solutions again. For trial 2, each time the fittest chromosomes are cropped, they are spliced multiple times before the best solutions are cropped.
#### Genetic Algorithm
1. Create and execute 100 random chromosomes
2. Get the best 20% (determined by number of conflicts)
3. Splice them randomly
4. Execute 20 spliced chromosomes
5. Repeat steps 2 through 4 four times
6. Get the best 20%
7. Splice them randomly
8. Execute 4 spliced chromosomes
9. Repeat steps 7-8 twice
#### Results
* Mean average of attempts to find goal state: 48936
* ~3.7x faster than the random agent
* Histogram:

![Histogram](./screenshots/ga_trial_two.png)
#### Notes

___
### Sources/ Survey
* [Genetic Algorithms and Machine Learning](https://link.springer.com/content/pdf/10.1023%2FA%3A1022602019183.pdf)
#### Notes
1. Common argument against genetic algorithms is that humans took billions of years to evolve, and that somehow means that genetic algorithms take billions of years to find solutions?
    * 1 Human generation = ~20 years
    * 1 GA generation = < 1 second
    * Selection process can be constrained pretty tightly in GAs, much tighter than in nature. Anything that has 1 successful copulation in nature can pass on its genes, GAs can be set to only push the best 20% or better forward. Insects with short life spans can adapt to new situations in a matter of days. This argument about adaptation taking a long time in nature, and therefore taking a long time artificially falls apart at the first ounce of thought.
    * The best solutions in a GA can all 'breed' with each other, exploring every possible outcome of the best solutions.
2. "Simply stated, genetic algorithms are probabilistic search procedures designed to work on large spaces involving states that can be represented by strings."
    * GAs are not universally applicable.
    * GAs can produce much better solutions much faster on certain types of problems than other machine learning algorithms.
3. "...the idea that the mind is subject to the same competitive-cooperative pressures as evolutionary systems has achieved some currency outside of GA circles."
___
* [Genetic Algorithms](https://www.jstor.org/stable/pdf/24939139.pdf?refreqid=excelsior%3A7b79ef68affedd67375ee74ef85c5ed3)
#### Notes
1. "By harnessing the of the genes of a single parent, researchers may be able to 'breed' programs that
solve problems even when no person can fully understand their structure."
    * Genetic algorithms need only know what a goal is, and a way to measure how close they are to a goal. Using tactics employed by natural selection and using them more efficiently than natural selection, genetic algorithms discover how to solve a problem by themselves. This makes GAs  a very useful strategy when you have absolutely no idea how to find a solution and are therefore unable to tell a computer how to solve a problem.
2. "...these so-called genetic algorithms have already demonstrated the ability to make breakthroughs in the design of such complex systems such as jet engines."
3. Different types of genetic algorithms use chromosomes differently.
