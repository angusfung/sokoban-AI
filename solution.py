import os
import numpy as np
import math
from search import * #for search engines
from sokoban import SokobanState, Direction, PROBLEMS, sokoban_goal_state #for Sokoban specific classes and problems

#SOKOBAN HEURISTICS
def heur_displaced(state):
  '''trivial admissible sokoban heuristic'''
  '''INPUT: a sokoban state'''
  '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''       
  count = 0
  for box in state.boxes:
    if box not in state.storage:
      count += 1
  return count

def absolute(num):
  if num < 0:
    return num * -1
  else:
    return num

def heur_manhattan_distance(state):
#IMPLEMENT
    '''admissible sokoban heuristic: manhattan distance'''
    '''INPUT: a sokoban state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''      

    h=0 #heuristic cost.
    for box in state.boxes:
      box_num=state.boxes[box] #returns the value associated with the key
      if state.restrictions == None:
        #find closest storage
        min_distance = float("inf") 
        for storage in state.storage:
          distance = absolute(storage[0]-box[0])+absolute(storage[1]-box[1])
          if distance <= min_distance:
            min_distance=distance
      elif (len(state.restrictions[box_num])!=1): #if there are multiple restrictions
                                                 #find the closest restriction
          #print(len(state.restrictions[box_num]),box_num)
          #convert frozen set to list
          min_distance = float("inf") 
          for i in range(len(state.restrictions[box_num])): #find closest restriction
            restriction = list(state.restrictions[box_num])
            restriction = restriction[i]
            distance = absolute(restriction[0]-box[0])+absolute(restriction[1]-box[1])
            if distance <= min_distance:
              min_distance=distance
              
      else: #if there is only one restriction, must go there.
          #print(len(state.restrictions[box_num]),box_num)
          #convert frozen set to list
          restriction = list(state.restrictions[box_num])
          restriction = restriction[0]
          distance = absolute(restriction[0]-box[0])+absolute(restriction[1]-box[1])
          min_distance = distance
      h+=min_distance  #total heuristic.
      min_distance = float("inf") #reintialize for next iteration
    return h

def heur_euclidean_distance(state): #euclidean distance from each box to each storage.


    h=0 #heuristic cost.
    for box in state.boxes:
      box_num=state.boxes[box] #returns the value associated with the key
      if state.restrictions == None:
        #find closest storage
        min_distance = float("inf") 
        for storage in state.storage:
          distance = math.sqrt(abs(storage[0]-box[0])**2+abs(storage[1]-box[1])**2)
          if distance <= min_distance:
            min_distance=distance
      elif (len(state.restrictions[box_num])!=1): #if there are multiple restrictions
                                                 #find the closest restriction
          #print(len(state.restrictions[box_num]),box_num)
          #convert frozen set to list
          min_distance = float("inf") 
          for i in range(len(state.restrictions[box_num])): #find closest restriction
            restriction = list(state.restrictions[box_num])
            restriction = restriction[i]
            distance = math.sqrt(abs(restriction[0]-box[0])**2+abs(restriction[1]-box[1])**2)
            if distance <= min_distance:
              min_distance=distance
              
      else: #if there is only one restriction, must go there.
          #print(len(state.restrictions[box_num]),box_num)
          #convert frozen set to list
          restriction = list(state.restrictions[box_num])
          restriction = restriction[0]
          distance = math.sqrt(abs(restriction[0]-box[0])**2+abs(restriction[1]-box[1])**2)
          min_distance = distance
      h+=min_distance  #total heuristic.
      min_distance = float("inf") #reintialize for next iteration
    return h

def heur_robot_to_goal(state):
    '''provides an (admissible) estimate of the distance between the robot to the goal
       this goal is the closest storage.
    '''
    h=0 #heuristic cost.
    distance = float('inf')
    min_distance = float('inf')
    
    x=state.robot[0]
    y=state.robot[1]
    
    for storage in state.storage:
      if state.robot not in storage:
        distance = abs(storage[0]-x) + abs(storage[1]-y)
        if distance < min_distance:
          min_distance = distance
    return min_distance

def L2Norm(state): #sums the distances from any box to any storage
    min_distance = float('inf')
    distance = 0
    for box in state.boxes:
      for storage in state.storage:
        distance += ((storage[0]-box[0])**2 + (storage[1]-box[1])**2)**0.5
        #if distance < min_distance:
          #min_distance = distance
    return distance

def L2Norm1(state): #min distance
    min_distance = float('inf')
    for box in state.boxes:
      for storage in state.storage:
        distance = ((storage[0]-box[0])**2 + (storage[1]-box[1])**2)**0.5
        if distance < min_distance:
          min_distance = distance
    return min_distance
    

problem_number = 0 

def heur_alternate(state):
#IMPLEMENT
    '''a better sokoban heuristic'''
    '''INPUT: a sokoban state'''
    '''OUTPUT: a numeric value that serves as an estimate of the distance of the state to the goal.'''
    
    global problem_number
    global last_heuristic
    global prev_state
    global look_up
    key = ''
    

    
    if state.parent == None:
      look_up = {}
      problem_number += 1
    try:
      if state.boxes == prev_state:
        return last_heuristic
    except:
      pass
    
    prev_state = state.boxes
    height = state.height
    width = state.width
    
    #add entry to dictionary
    for box in state.boxes:
      key = key + str(box)
    if key in look_up:
      last_heuristic = look_up[key]
      return last_heuristic
    
    #run the actual deadlocking loop
    manhattan_distance = 0
    for box in state.boxes:
      if state.restrictions == None: #if no restriction, just pass in storage.
        result = deadblock_check(box,state,height,width,state.storage,key)
        if result == float('inf'):
          return result
      else: #there is restriction and we make sure it's the right one.
        index = state.boxes[box] #index of the appropriate RESTRICTION for the BOX in loop.
        result = deadblock_check(box,state,height,width,state.restrictions[index],key)
        if result == float('inf'):
          return result
      #manhattan_distance += result
    
    #last_heuristic = manhattan_distance
    last_heuristic = result
    look_up[key] = last_heuristic 
    return result 
  
def deadblock_check(box,state,height,width,goal_restriction,key):
  
  global last_heuristic
  global prev_state
  global look_up


  #if box not in state.storage:
  if box not in goal_restriction: #there may be none, or there may be some.
    x=box[0]
    y=box[1]
    
    left_obs = False
    right_obs = False
    top_obs = False
    bottom_obs = False
    
    left = (x-1,y)
    right = (x+1,y)
    top = (x,y-1)
    bottom = (x,y+1)
    
    if top in state.obstacles or top[1] < 0 or top in state.boxes:
      top_obs = True
    if bottom in state.obstacles or bottom[1] > (height - 1) or bottom in state.boxes:
      bottom_obs = True
    if left in state.obstacles or left[0] < 0 or left in state.boxes:
      left_obs = True
    if right in state.obstacles or right[0] > (width -1) or right in state.boxes:
      right_obs = True
    
    
    safe = False 
    
    #case 1
    if box[0] == 0 or box[0] == (width-1): #along the side walls, if any neighbours, bad.
      if top_obs or bottom_obs: 
        last_heuristic = float('inf')
        look_up[key] = last_heuristic
        return float('inf')
        
      if state.restrictions != None:
        goal_index = state.boxes[box]
        corr_restriction = state.restrictions[goal_index]
        for restriction in corr_restriction: 
        #along the left and right wall, checking to see if there's any goal along it.
          if box[0] == 0 and restriction[0] == 0:
            safe = True
          if box[0] == (width-1) and restriction[0] == (width-1):
            safe = True
        if safe == False:
          last_heuristic = float('inf')
          look_up[key] = last_heuristic
          return float('inf')
          
      elif state.restrictions == None: #boxes can go in any of the storages.
        #therefore, we can check if any of the storages are along  the wall, if so, safe.
        for storage in state.storage:
          #along the top and bottom wall, checking to see if there's any goal along it.
          if box[0] == 0 and storage[0] == 0:
            safe = True
          if box[0] == (width-1) and storage[0] == (width-1):
            safe = True
        if safe == False:
          last_heuristic = float('inf')
          look_up[key] = last_heuristic
          return float('inf')

        
    #case 2    
    elif box[1]==0 or box[1] == (height-1): #along the  top and bottom walls. 
      if left_obs or right_obs: #if any on left or right, bad. 
        last_heuristic = float('inf')
        look_up[key] = last_heuristic
        return float('inf')
        
      if state.restrictions != None:  
        goal_index = state.boxes[box]
        corr_restriction = state.restrictions[goal_index]
        for restriction in corr_restriction:
          #along the top and bottom wall, checking to see if there's any goal along it.
          if box[1] == 0 and restriction[1] == 0:
            safe = True
          if box[1] == (height-1) and restriction[1] == (height-1):
            safe = True
        if safe == False:
          last_heuristic = float('inf')
          look_up[key] = last_heuristic
          return float('inf')
          
      elif state.restrictions == None: #boxes can go in any of the storages.
        #therefore, we can check if any of the storages are along  the wall, if so, safe.
        for storage in state.storage:
          #along the top and bottom wall, checking to see if there's any goal along it.
          if box[1] == 0 and storage[1] == 0:
            safe = True
          if box[1] == (height-1) and storage[1] == (height-1):
            safe = True
        if safe == False:
          last_heuristic = float('inf')
          look_up[key] = last_heuristic
          return float('inf')
 
    #ONLY CONSIDER OBSTACLES NOW. WE CAN MOVE BOXES. ONLY PROBLEM ARE REAL OBSTACLES.
    left_obs = False
    right_obs = False
    top_obs = False
    bottom_obs = False
    
    if top in state.obstacles or top[1] < 0:
      top_obs = True
    if bottom in state.obstacles or bottom[1] > (height - 1):
      bottom_obs = True
    if left in state.obstacles or left[0] < 0:
      left_obs = True
    if right in state.obstacles or right[0] > (width -1):
      right_obs = True

    if top_obs and right_obs:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf')
    elif right_obs and bottom_obs:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf')
    elif bottom_obs and left_obs:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf')
    elif left_obs and top_obs:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf') 
    
#CONSIDER 4 CASES WITH OBSTACLES:

#  CASE 1:   CASE 2:   CASE 3:   CASE 4: 
#  XO        0X        XX        XX   
#  XX        XX        XO        OX
  
    left_obs = False
    right_obs = False
    top_obs = False
    bottom_obs = False
    
    if top in state.obstacles or top[1] < 0 or top in state.boxes:
      top_obs = True
    if bottom in state.obstacles or bottom[1] > (height - 1) or bottom in state.boxes:
      bottom_obs = True
    if left in state.obstacles or left[0] < 0 or left in state.boxes:
      left_obs = True
    if right in state.obstacles or right[0] > (width -1) or right in state.boxes:
      right_obs = True
      
    bottom_left_corner = (x-1,y+1)
    bottom_right_corner = (x+1,y+1)
    top_left_corner = (x-1,y-1)
    top_right_corner = (x+1,y-1)
   
    if left_obs and bottom_obs and bottom_left_corner in state.obstacles:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf')
    if right_obs and bottom_obs and bottom_right_corner in state.obstacles:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf')
    if left_obs and top_obs and top_left_corner in state.obstacles:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf')
    if right_obs and top_obs and top_right_corner in state.obstacles:
      last_heuristic = float('inf')
      look_up[key] = last_heuristic
      return float('inf')
    
  #   #passes all tests
  #   min_distance = float('inf')
  #   if state.restrictions != None:
  #     goal_index = state.boxes[box]
  #     corr_restriction = state.restrictions[goal_index]
  #     for restriction in corr_restriction:
  #       distance = absolute(restriction[0]-box[0])+absolute(restriction[1]-box[1])
  #       if distance < min_distance:
  #         min_distance = distance
  #     return min_distance
  #   elif state.restrictions == None:
  #     for storage in state.storage:
  #       distance = absolute(storage[0]-box[0])+absolute(storage[1]-box[1])
  #       if distance < min_distance:
  #         min_distance = distance
  #     return min_distance
  return 0 #passed all tests      
      


def fval_function(sN, weight):
#IMPLEMENT
    """
    Provide a custom formula for f-value computation for Anytime Weighted A star.
    Returns the fval of the state contained in the sNode.

    @param sNode sN: A search node (containing a SokobanState)
    @param float weight: Weight given by Anytime Weighted A star
    @rtype: float
    """

    return sN.gval + weight * sN.hval

def anytime_gbfs(initial_state, heur_fn, timebound = 10):
#IMPLEMENT
    '''Provides an implementation of anytime greedy best-first search, as described in the HW1 handout'''
    '''INPUT: a sokoban state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False'''
    best_path_cost = float("inf")
    time_remain = 8
    iter = 0
    
    se = SearchEngine('best_first', 'full')
    se.init_search(initial_state, goal_fn =sokoban_goal_state, heur_fn=heur_fn)
    
    while (time_remain > 0) and not se.open.empty():
      iter += 1
      t_start = os.times()[0]
      print(t_start)
        
      if iter == 1:
        final = se.search(timebound)
        
        try: 
          goalval = final.gval
          time_remain = 8 - t_start 
          if goalval < best_path_cost:
            best_path_cost = goalval
            optimal_final = final
              
        except: #when final = False
          time_remain = 8 - t_start 
      
      else:
        costbound = (best_path_cost, float('inf'), float('inf'))
        final = se.search(timebound, costbound)
        
        try: 
          goalval = final.gval
          time_remain = 8 - t_start 
          if goalval < best_path_cost:
            best_path_cost = goalval
            optimal_final = final
              
        except: #when final = False
          time_remain = 8 - t_start 
            
    try: 
      return optimal_final
    except:
      return final
    
    
def anytime_weighted_astar(initial_state, heur_fn, weight=1., timebound = 10):
#IMPLEMENT
    '''Provides an implementation of anytime weighted a-star, as described in the HW1 handout'''
    '''INPUT: a sokoban state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False''' 
    
    #initialization
    best_path_cost = float("inf")
    time_remain = 8
    iter = 0 
    
    wrapped_fval_function = (lambda sN: fval_function(sN, weight))
    se = SearchEngine('custom', 'full')
    se.init_search(initial_state, sokoban_goal_state, heur_fn, wrapped_fval_function)
    
    while (time_remain > 0) and not se.open.empty():
      iter += 1
      t_start = os.times()[0]
      
      if iter == 1:
        final = se.search(timebound)
        try:
          goalval = final.gval + heur_fn(final) #f=g+h
          time_remain = 8 - t_start 
          if goalval < best_path_cost:
            best_path_cost = goalval #optimal cost
            optimal_final = final #optimal state
        except: #if no solution found, final = False, just update the timer.
          time_remain = 8 - t_start 

      else: #prune only when current final f is larger than best_path_cost (f)
        costbound = (float("inf"), float("inf"),best_path_cost) 
        final = se.search(timebound, costbound)
        
        try:
          goalval = final.gval + heur_fn(final) #f=g+h
          time_remain = 8 - t_start 
          if goalval < best_path_cost:
            best_path_cost = goalval
            optimal_final = final
              
        except: #when final = False
          time_remain = 8 - t_start 
            
    try: 
      return optimal_final
    except:
      return final
    
    
    return False

if __name__ == "__main__":
  #TEST CODE
  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 2; #2 second time limit for each problem
  print("*************************************")  
  print("Running A-star")     

  for i in range(0, 10): #note that there are 40 problems in the set that has been provided.  We just run through 10 here for illustration.

    print("*************************************")  
    print("PROBLEM {}".format(i))
    
    s0 = PROBLEMS[i] #Problems will get harder as i gets bigger

    se = SearchEngine('astar', 'full')
    se.init_search(s0, goal_fn=sokoban_goal_state, heur_fn=heur_displaced)
    final = se.search(timebound)

    if final:
      final.print_path()
      solved += 1
    else:
      unsolved.append(i)    
    counter += 1

  if counter > 0:  
    percent = (solved/counter)*100

  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************") 

  solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 8; #8 second time limit 
  print("Running Anytime Weighted A-star")   

  for i in range(0, 10):
    print("*************************************")  
    print("PROBLEM {}".format(i))

    s0 = PROBLEMS[i] #Problems get harder as i gets bigger
    weight = 10
    final = anytime_weighted_astar(s0, heur_fn=heur_displaced, weight=weight, timebound=timebound)

    if final:
      final.print_path()   
      solved += 1 
    else:
      unsolved.append(i)
    counter += 1      

  if counter > 0:  
    percent = (solved/counter)*100   
      
  print("*************************************")  
  print("{} of {} problems ({} %) solved in less than {} seconds.".format(solved, counter, percent, timebound))  
  print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))      
  print("*************************************") 



