# Sokoban_AI

AI of the game Sokoban, using basic search strategies {depth-first search, breadth-first search, best-first search, A-star search,
uniform-cost search, custom search} and more advanced search variants thereof {anytime greedy best-first search, anytime weighted
A-start search}, with heuristics {displaced blocks, manhattan distance, euclidean distance, L2-norm, etc.},
fully equipped with deadblock checking and dictionary lookup (for better amortized runtime). 

Modular enough to add custom search strategies or heuristics in solution.py, and any more advanced techniques can be built
on top of them. 

To run, ensure all files are in the same working directory and run the test scripts. Additional test cases can be added. 
