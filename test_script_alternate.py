
# import student's functions
from solution import *
#from backs import *
#from solutiontest import *
from test_problems import PROBLEMS

#Select what to test
print_problems = False
test_alternate = True

if print_problems:
    for i, p in enumerate(PROBLEMS):
        print("\nProblem {}\n".format(i))
        print(p.state_string())

if test_alternate:

  ##############################################################
  # TEST ALTERNATE HEURISTIC
  print('Testing alternate heuristic with greedy best-first search')

  solved = 0; unsolved = []; benchmark = 0; timebound = 4 #4 second time limit
  for i in range(0, len(PROBLEMS)):
    print("*************************************")
    print("PROBLEM {}".format(i))

    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    se = SearchEngine('best_first', 'full')
    se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_alternate)
    #se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_euclidean_distance)
    final = se.search(timebound)

    if final:
      final.print_path()
      solved += 1
    else:
      unsolved.append(i)

  print("\n*************************************")
  print("Of 10 initial problems, {} were solved in less than {} seconds by this solver.".format(solved, timebound))
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))
  print("The benchmark implementation solved 14 out of the 40 practice problems given 4 seconds.")
  print("*************************************\n")
  ##############################################################
  
