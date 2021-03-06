## Research

Sources, citations and notes.
___


### Sources/ Survey
___
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
1. "By harnessing the of the genes of a single parent, researchers may be able to 'breed' programs that solve problems even when no person can fully understand their structure."
    * Genetic algorithms need only know what a goal is, and a way to measure how close they are to a goal. Using tactics employed by natural selection and using them more efficiently than natural selection, genetic algorithms discover how to solve a problem by themselves. This makes GAs  a very useful strategy when you have absolutely no idea how to find a solution and are therefore unable to tell a computer how to solve a problem.
2. "...these so-called genetic algorithms have already demonstrated the ability to make breakthroughs in the design of such complex systems such as jet engines."
3. Different types of genetic algorithms use chromosomes differently.
___
* [Handbook of Genetic Algorithms](https://pdf.sciencedirectassets.com/271585/1-s2.0-S0004370200X00409/1-s2.0-S0004370298000162/main.pdf?x-amz-security-token=AgoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQDpzPbx4LEra4y6iA5UCzm%2BI0m4Fr3XOaec%2Bdq7cDl9cAIhAMaFRwHAv2ujEA6RZiAp%2BvGV2cFG5CcC3sVG79eNppLEKtoDCHkQAhoMMDU5MDAzNTQ2ODY1IgzvFdJnUwUixqpGc50qtwNJd1Pv1REKQtXoNrSCI474QjYP0dY4gRHmaESnnNdsQxBx0xYgc3uPz3EmH18Y3tMK11zC88uQEktwcg%2FYw6R5GVcJcknNcGI%2Bh1Ml7zfZwo9L7NZVWjGQ7DH4hHiMHbEmnamWDeV6XrcjcxD5F5Fg2vjjh0He1Qw5PPWlMYxNgBvGzmoG1rdfB032NcBCZuQUpTwZB1vHZJbeHnqFG9q5vxgLzYIA%2Fqfpte%2FLIUkDRIwVEhSjSb8OBFZZSYdP%2BI0tQjXfGOX18oTHXtE5ODEOV8QtvANsKS%2BK%2FQI2hYEPQTMwD7G7gM1AN8mHLse1bLgMlJJVlDvxjuPF1viNtTu22bX2PsYgKVOfaUlzB96Mhs1oY7y%2FLtLBaCb192nUURMBgEiDr%2B346nRFDQokiGHYYv%2FXIE7uopqj%2F%2BpQ5WQ3c3BNWcwldXCeWKjnOQz3VzCXYMdrtznkM75DjZ4H1P%2BkOHhiXSrpvnuTHFyomVV9i4kfUJmVMaodrzldYf4MOkP3vWwLSULk32JQuSIXLSI75dr53Vj6CoJU8qTPG71SOsfS%2B3%2BMmTisaXWcxalsk8ysZ473WBRxMNnroeYFOrMBLhjtL2qqa7wMmYiEDWYfu9psGCIQ6iamKCiEHgXsd5OgfoFtLNUYMhbTm45w0eE2AgcP%2FUuJRwe5jdOnmR5J0c8l9Sxk4idnGAeqm4hVnv24%2Bvbau8PAYnhUd%2F%2FpXib6KKawjpGmVt96hzTrOrwNwSZwMJrKwqBAxyFJhQdbhMMQuGs2nIAfwXRwYySRDf%2BGg8CiTqb3tMDCqHY19FdT3DBT5AVrmEOfwQupVG22WMGMSgQ%3D&AWSAccessKeyId=ASIAQ3PHCVTY77Q2SRHI&Expires=1556647044&Signature=85iou3lZ7FCNCVKpfvZ%2Faw1Mz2s%3D&hash=aa3283b7a51418824c8cd528f02b6b40487f77f5b19b597b6fdf3a0bfa71fde8&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0004370298000162&tid=spdf-8292c0e2-f061-4e90-bb5a-c5733e08e359&sid=6fd1a561227386480f8a7df0b43635c9fe6fgxrqa&type=client)
#### Notes
1. This article explains GAs at a slightly more technical level. Speaks in detail about various types of fitness functions and splicing methods.
2. The term 'genetic algorithm' can be misleading in the sense that there isn't necessarily a strong link between any given genetic algorithm and the natural behavior of genes in nature.
    * Selection in genetic algorithms can be much tighter than in nature, mutation and splicing can be done more intelligently in genetic algorithms than in nature.
    * There are many different methods of crossing over in genetic algorithms.
3. Genetic algorithms can be implemented with other machine learning strategies as well.
    * Crossing over can be used on Artificial Neural Networks
___
* [A Summary of Research on Parallel Genetic Algorithms](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=1115E425DCC85D6A7942493DE5F3442A?doi=10.1.1.49.4669&rep=rep1&type=pdf)
#### Notes

___
* [Genetic algorithms: An Overview](https://onlinelibrary.wiley.com/doi/epdf/10.1002/cplx.6130010108)
#### Notes
1. GAs are a form of 'evolutionary computation'
2. GA concept began with John Holland in the 1960s
3. AI is developed using a 'bottom-up paradigm.' "In such a paradigm, human programmers encode simple rules, and complex behaviors such as intelligence emerge from these simple rules."
4. Goal of GAs is typically to minimize or maximize a certain function.
    * Let's say a robot is trying to finish a maze as quickly as possible. "The fitness of a particular sequence (chromosome) can be calculated by letting the robot follow the sequence, and then measuring the number of steps between its final position and the exit-the smaller the distance, the higher the fitness of the sequence."
5. Since GAs rely heavily on randomness, they must be run many times to get an accurate estimate of their efficiency.
6. GA Common uses:
    * Optimization (scheduling, numerical optimization)
    * Automatic programming
    * Economic models
    * Immune system models
    * Ecological models
    * Population genetics models (as in, under what conditions will a certain trait become evolutionarily viable)
    * Relationship between evolution and learning
___
* [Systems Research, Genetic Algorithms and Information Systems](https://search.proquest.com/docview/196893337?accountid=27112)
#### Notes

___
* [A Study on Genetic Algorithm and its Applications](https://www.researchgate.net/publication/309770246_A_Study_on_Genetic_Algorithm_and_its_Applications)
#### Notes
1. 3 Main stages of a GA:
    * Selection operation
    * Crossover operation
    * Mutation operation
2. Selection operation:
    * Chromosomes to be mutated or recombined can be randomly selected from the population with or without a bias towards the best chromosomes. The selection process does not need an element of randomness.
    * One highly effective selection method is to always select the best chromosome from the population, but add an element of randomness to the rest of the selections.
3. Crossover operation:
    * Single-point crossover: Splits chromosomes in half at a random point, then recombines them with each other
    * Two-point crossover: Split chromosomes into three pieces, crossing over the middle section between chromosomes
    * Uniform crossover: Group chromosomes into pairs, randomly generate a string of 1s and 0s for each pair. Swap bits of the chromosomes at the locations of every 1 in the string.
4. Mutation operation:
    * Set a probability for each gene in the chromosome to mutate
___
* [Adapting Crossover and Mutation Rates in Genetic Algorithms](https://www.researchgate.net/profile/Wen-Yang_Lin/publication/220587952_Adapting_Crossover_and_Mutation_Rates_in_Genetic_Algorithms/links/09e41507ecb25e3e07000000/Adapting-Crossover-and-Mutation-Rates-in-Genetic-Algorithms.pdf)
#### Notes
1. "The mutation operator is used to change some elements in selected individuals with a probability p m (the mutation rate or mutation probability), leading to additional genetic diversity to help the search process escape from local optimal traps."
    * It's worth noting that adding a mutation probability to a genetic algorithm doesn't necessarily increase the efficiency. Only with objective functions in which there are local minimums/maximums are they typically helpful.
___
* [Optimal Mutation Rates in Genetic Search](http://neuro.bstu.by/ai/To-dom/My_research/Papers-0/For-research/Needle/back.pdf)
#### Notes

___
* [Evolutionary Computation: Comments on the History and Current State](https://www.researchgate.net/profile/Hans-Paul_Schwefel/publication/3418513_Evolutionary_Computation_Comments_on_the_History_and_Current_State/links/00463534e624d0358e000000/Evolutionary-Computation-Comments-on-the-History-and-Current-State.pdf)
#### Notes
1. Main types of evolutionary algorithms:
    * Genetic Algorithms
    * Evolutionary Programming
    * Evolution Strategies
2. Genetic Algorithms were 'originally proposed as a general model of adaptive processes, but by far the largest application of the techniques is in the domain of optimization.'
3. Genetic Algorithms were originally introduced in the 1950s, but didn't gain traction until Holland's work in the 1970's. They were initially inefficient not only because of the limited computational power available at the time, but also because the approaches being taken lacked the refinement necessary to make any evolutionary computational algorithm to be viable.
4. Another big issue evolutionary computational algorithms had to overcome before they could become viable was finding the types of problems they solve most efficiently.
5.
___
