"""Additional Sokoban test problems.
"""

from sokoban import SokobanState

def generate_coordinate_rect(x_start, x_finish, y_start, y_finish):
    """
    Generate tuples for coordinates in rectangle (x_start, x_finish) -> (y_start, y_finish)
    """
    coords = []
    for i in range(x_start, x_finish):
        for j in range(y_start, y_finish):
            coords.append((i, j))
    return coords


PROBLEMS = (
    # Sokobanonline lesson problems are from https://www.sokobanonline.com/play/lessons
    # Boxxle problems are from: http://sokoban.info/?2 (any restrictions are our own)
    # Easiest 10
    # Problem 0, Sokobanonline lesson #2-1
    SokobanState("START", 0, None, 4, 4, # dimensions
                 (0, 3), #robot
                 {(1, 2): 0, (1, 1): 1}, #boxes
                 {(2, 1): 0, (2, 2): 1}, #storage
                 frozenset(((0, 0), (1, 0), (3, 3))), #obstacles
                 (frozenset(((2, 1),)), frozenset(((2, 2),))), #restrictions,
                 {0: 'cyan', 1: 'magenta'}, #box colours
                 {0: 'cyan', 1: 'magenta'} #storage colours
                 ),
    # Problem 1, Sokobanonline lesson #2-3
    SokobanState("START", 0, None, 5, 4, # dimensions
             (0, 3), #robot
             {(2, 1): 0, (3, 1): 1}, #boxes
             {(2, 1): 0, (3, 1): 1}, #storage
             frozenset(((0, 0), (4, 0), (2, 3), (3, 3), (4, 3))), #obstacles
             (frozenset(((3, 1),)), frozenset(((2, 1),))), #restrictions,
             {0: 'cyan', 1: 'magenta'}, #box colours
             {1: 'cyan', 0: 'magenta'} #storage colours
             ),
    # Problem 2, Sokobanonline lesson #2-5
    SokobanState("START", 0, None, 6, 4, # dimensions
             (5, 3), #robot
             {(1, 1): 0, (3, 1): 1}, #boxes
             {(2, 0): 0, (2, 2): 1}, #storage
             frozenset(((2, 1), (0, 0), (5, 0), (0, 3), (1, 3), (2, 3), (3, 3))), #obstacles
             (frozenset(((2, 0),)), frozenset(((2, 2),))), #restrictions,
             {0: 'cyan', 1: 'magenta'}, #box colours
             {0: 'cyan', 1: 'magenta'} #storage colours
             ),
    # Problem 3
    SokobanState("START", 0, None, 5, 5, # dimensions
                 (2, 1), # robot
                 {(1, 1): 0, (1, 3): 1, (3, 1): 2, (3, 3): 3}, #boxes
                 {(0, 0): 0, (0, 4): 1, (4, 0): 2, (4, 4): 3}, #storage
                 frozenset(((1, 0), (2, 0), (3, 0), (1, 4), (2, 4), (3, 4))), #obstacles
                 None
                 ),
    # Problem 4
    SokobanState("START", 0, None, 5, 5, # dimensions
                 (4, 0), #robot
                 {(3, 1): 0, (3, 2): 1, (3, 3): 2}, #boxes
                 {(0, 0): 0, (0, 4): 1, (0, 2): 2}, #storage
                 frozenset(((2, 0), (2, 1), (2, 3), (2, 4))), #obstacles
                 (frozenset(((0, 0),)), frozenset(((0, 4),)), frozenset(((0, 2),))), #restrictions
                 {0: 'cyan', 1: 'magenta', 2: 'yellow'},
                 {0: 'cyan', 1: 'magenta', 2: 'yellow'}
                 ),
    # Problem 5, Problem 4 with no hints
    SokobanState("START", 0, None, 5, 5, # dimensions
                 (4, 0), #robot
                 {(3, 1): 0, (3, 2): 1, (3, 3): 2}, #boxes
                 {(0, 0): 0, (0, 2): 1, (0, 4): 2}, #storage
                 frozenset(((2, 0), (2, 1), (2, 3), (2, 4))), #obstacles
                 None #restrictions
                 ),
    # Problem 6
    SokobanState("START", 0, None, 6, 5, # dimensions
        (0, 4), #robot
        {(1, 3): 0, (3, 3): 1}, # boxes
        {(5, 4): 0, (0, 1): 1}, # storages
        frozenset((generate_coordinate_rect(0, 4, 2, 3))), # obstacles
        None, # restrictions
        ),
    # Problem 7, Boxxle 1, problem 2
    SokobanState("Start", 0, None, 8, 7, # dimensions
        (5, 5), # robot
        {(3, 5): 1, (1, 3): 1, (3, 2): 0, (2, 1): 0}, # boxes
        {(0, 0): 1, (1, 0): 1, (0, 1): 0, (1, 1): 0}, # storages
        frozenset(((0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (1, 5), (1, 6), (7, 6), (7, 5),
        (7, 4), (7, 3), (7, 2), (2, 2), (4, 2), (5, 2), (5, 1))), # obstacles
        (frozenset(((0, 1), (1, 1),)), frozenset(((0, 0), (1, 0),))),
        {0: 'cyan', 1: 'magenta'},
        {0: 'cyan', 1: 'magenta'}
        ),
    # Problem 8, Boxxle 1 problem 3
    SokobanState("Start", 0, None, 6, 4, # dimensions
        (1, 0),
        {(1, 1): 0, (2, 1): 0, (3, 2): 0, (4, 1): 0, (5, 2): 0}, # boxes
        {(4, 0): 0, (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0}, # storages
        frozenset(((0, 0), (2, 0), (3, 0), (0, 3), (1, 3), (2, 3))), # obstacles
        None
        ),
    # Problem 9, Boxxle 1 problem 4
    SokobanState("Start", 0, None, 6, 6, # dimensions
        (1, 0), # robot
        {(2, 1): 0, (1, 4): 0, (4, 5): 0}, # boxes
        {(0, 3): 0, (0, 4): 0, (0, 5): 0}, # storages
        frozenset(((0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (3, 2), (3, 3), (4, 4),
        (3, 0), (4, 0), (5, 0), (5, 1), (5, 2))), # obstacles
        None
        ),

    # MEDIUM 10
    # Problem 10, Sokobanonline lesson #2-12
    SokobanState("START", 0, None, 6, 4, # dimensions
         (5, 3), #robot
         {(3, 1): 0, (2, 2): 1, (3, 2): 2, (4, 2): 3}, #boxes
         {(0, 0): 0, (2, 0): 1, (1, 0): 2, (1, 1): 3}, #storage
         frozenset((generate_coordinate_rect(4, 6, 0, 1)
                   + generate_coordinate_rect(0, 3, 3, 4))), #obstacles
         (frozenset(((0, 0),)), frozenset(((2, 0),)), frozenset(((1, 0),)), frozenset(((1, 1),))), #restrictions,
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red'}, #box colours
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red'} #storage colours
         ),
    # Problem 11, Sokobanonline lesson #2-12, less hints
    SokobanState("START", 0, None, 6, 4, # dimensions
         (5, 3), #robot
         {(3, 1): 0, (2, 2): 1, (3, 2): 2, (4, 2): 3}, #boxes
         {(0, 0): 0, (2, 0): 1, (1, 0): 2, (1, 1): 3}, #storage
         frozenset((generate_coordinate_rect(4, 6, 0, 1)
                   + generate_coordinate_rect(0, 3, 3, 4))), #obstacles
         (frozenset(((0, 0),)), frozenset(((2, 0),)), frozenset(((1, 0),)), frozenset(((0, 0), (2, 0), (1, 0), (1, 1),))), #restrictions,
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'normal'}, #box colours
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red'} #storage colours
         ),
    # Problem 12
    SokobanState("START", 0, None, 9, 6, # dimensions
        (0, 0), #robot
        {(4, 3): 0, (6, 4): 1}, # Boxes
        {(1, 3): 0, (1, 5): 1}, # Storages
        frozenset((generate_coordinate_rect(2, 7, 2, 3) + generate_coordinate_rect(2, 3, 2, 6))), # obstacles
        None, #restrictions
        ),
    # Problem 13
    SokobanState("START", 0, None, 10, 7, # dimensions
        (0, 0), #robot
        {(5, 3): 0, (7, 4): 1}, # Boxes
        {(1, 3): 0, (1, 6): 1}, # Storages
        frozenset((generate_coordinate_rect(2, 8, 2, 3) + generate_coordinate_rect(2, 3, 2, 7))), # obstacles
        None, #restrictions
        ),
    # Problem 14
    SokobanState("Start", 0, None, 6, 6, # dimensions
        (5, 5), #robot
        {(3, 2): 0, (3, 3): 1, (3, 4): 2, (4, 3): 3}, # boxes
        {(0, 2): 0, (0, 3): 1, (0, 4): 2, (0, 5): 3}, # storages
        frozenset(((1, 2), (1, 3), (1, 4), (1, 5), (2, 2), (5, 1), (5, 0))), # obstacles
        None, # restrictions
        ),
    # Problem 15
    SokobanState("Start", 0, None, 6, 5, # dimensions
        (1, 4), # robot
        {(4, 4): 0, (1, 2): 1, (4, 0): 3}, # boxes
        {(0, 4): 0, (5, 2): 1, (0, 0): 3}, # storages
        frozenset(), # no obstacles
        None
        ),
    # Problem 16
    SokobanState("Start", 0, None, 7, 6, # dimensions
        (1, 0),
        {(1, 1): 0, (2, 3): 1, (2, 4): 1},
        {(2, 5): 0, (5, 1): 1, (5, 3): 1},
        frozenset(((3, 0), (3, 1), (3, 2), (3, 4), (3, 5),)),
        (frozenset(((2, 5),)), frozenset(((2, 5), (5, 1), (5, 3),))),
        {0: 'cyan', 1: 'normal'},
        {0: 'cyan', 1: 'magenta'}
        ),
    # Problem 17, Boxxle 1, problem 1
    SokobanState("Start", 0, None, 7, 7, # dimensions
        (0, 0), #robot
        {(1, 1): 0, (1, 2): 1, (2, 1): 1}, # boxes
        {(6, 2): 0, (6, 3): 1, (6, 4): 2}, # storages
        frozenset(((0, 3), (0, 4), (0, 5), (0, 6), (1, 3), (1, 4), (3, 0), (3, 1), (3, 2), (3, 3),
        (4, 3), (5, 3), (5, 2), (5, 1), (6, 1), (6, 6), (5, 6), (4, 6), (4, 5), )), # obstacles
        None
        ),
    # Problem 18, Boxxle 1 problem 5
    SokobanState("Start", 0, None, 8, 5, # dimensions
        (1, 2), # robot
        {(1, 1): 0, (3, 2): 0, (5, 3): 0, (6, 2): 0}, # boxes
        {(1, 4): 0, (1, 3): 0, (2, 4): 0, (2, 3): 0}, # storages
        frozenset(((0, 0), (0, 1), (0, 4), (3, 4), (3, 3), (7, 4), (7, 3), (7, 0), (6, 0),
            (2, 1), (3, 1), (4, 1))), # obstacles
        None
        ),
    # Problem 19, Boxxle 1 problem 8
    SokobanState("Start", 0, None, 8, 5, # dimensions
        (7, 2), # robot
        {(2, 2): 0, (3, 1): 0, (3, 3): 0, (4, 2): 0, (5, 3): 0}, # boxes
        {(0, 2): 0, (0, 3): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0}, # storages
        frozenset(((0, 1), (0, 0), (1, 0), (2, 0), (4, 1), (5, 1), (7, 0), (7, 1), (7, 3), (7, 4),
            (0, 4), (1, 4), (2, 4), (3, 4))),
        None
        ),

    # HARD 20
    # Problem 20, Sokobanonline lesson #2-15
    SokobanState("START", 0, None, 8, 6, # dimensions
         (1, 2), #robot
         {(1, 3): 0, (2, 3): 1, (3, 3): 2, (4, 3): 3, (5, 3): 4}, #boxes
         {(7, 0): 0, (7, 1): 1, (7, 2): 2, (7, 3): 3, (7, 4): 4}, #storage
         frozenset((generate_coordinate_rect(0, 7, 0, 2) + [(0, 2), (6, 2), (7, 5)]
         + generate_coordinate_rect(0, 5, 5, 6))), #obstacles
         (frozenset(((7, 0),)), frozenset(((7, 1),)), frozenset(((7, 2),)), frozenset(((7, 3),)), frozenset(((7, 4),))), #restrictions,
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red', 4: 'green'}, #box colours
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red', 4: 'green'} #storage colours
         ),
    # Problem 21, https://www.sokobanonline.com/play/community/pc46/remodel-3/18907_puzzle-0201-kbr-901
    SokobanState("START", 0, None, 6, 5, # dimensions
         (5, 2), #robot
         {(3, 1): 0, (3, 2): 1, (3, 3): 2, (4, 2): 3}, #boxes
         {(1, 2): 0, (2, 2): 1, (3, 2): 2, (0, 2): 3}, #storage
         frozenset((generate_coordinate_rect(4, 6, 0, 1)
                    + generate_coordinate_rect(3, 6, 4, 5))
                    + [(1, 1), (1, 3)]), #obstacles
         (frozenset(((1, 2),)), frozenset(((2, 2),)), frozenset(((3, 2),)), frozenset(((0, 2),)), frozenset(((7, 4),))), #restrictions,
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red', 4: 'green'}, #box colours
         {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red', 4: 'green'} #storage colours
         ),
    # Problem 22
    SokobanState("START", 0, None, 8, 5, # dimensions
        (0, 3), #robot
        {(1, 3): 0, (3, 3): 1, (5, 3): 2}, # boxes
        {(7, 4): 0, (0, 1): 1, (0, 4): 2}, # storages
        frozenset((generate_coordinate_rect(0, 6, 2, 3))), # obstacles
        (frozenset(((7, 4), (0, 1),)), frozenset(((7, 4), (0, 1),)), frozenset(((0, 4),))), # restrictions,
        {0: 'normal', 1: 'normal', 2: 'cyan'},
        {0: 'magenta', 1: 'magenta', 2: 'cyan'}
        ),
    # Problem 23
    SokobanState("START", 0, None, 8, 5, # dimensions
        (0, 3), #robot
        {(1, 3): 0, (3, 3): 1, (5, 3): 2}, # boxes
        {(7, 4): 0, (0, 1): 1, (0, 4): 2}, # storages
        frozenset((generate_coordinate_rect(0, 6, 2, 3))), # obstacles
        None, # restrictions
        ),
    # Problem 24
    SokobanState("Start", 0, None, 10, 6, # dimensions
        (0, 3), #robot
        {(1, 1): 0, (3, 1): 1, (5, 1): 1}, # boxes
        {(7, 1): 0, (9, 5): 1, (8, 5): 1}, # storages
        frozenset((generate_coordinate_rect(0, 8, 0, 1) + generate_coordinate_rect(1, 8, 3, 4))), # obstacles
        (frozenset(((7,1),)), frozenset(((8, 5), (9, 5),))),
        {0: 'cyan', 1: 'magenta'},
        {0: 'cyan', 1: 'magenta'}
        ),
    # Problem 25
    SokobanState("Start", 0, None, 10, 6, # dimensions
        (0, 3), #robot
        {(1, 1): 1, (3, 1): 1, (5, 1): 0}, # boxes
        {(7, 1): 0, (9, 5): 1, (8, 5): 1}, # storages
        frozenset((generate_coordinate_rect(0, 8, 0, 1) + generate_coordinate_rect(1, 8, 3, 4))), # obstacles
        (frozenset(((7,1),)), frozenset(((8, 5), (9, 5),))),
        {0: 'cyan', 1: 'magenta'},
        {0: 'cyan', 1: 'magenta'}
        ),
    # Problem 26
    SokobanState("Start", 0, None, 6, 6, # dimensions
        (5, 5), #robot
        {(3, 2): 0, (3, 4): 1, (4, 3): 2, (3, 3): 3}, # boxes
        {(0, 5): 0, (0, 4): 1, (0, 3): 2, (0, 2): 3}, # storages
        frozenset(((1, 2), (1, 3), (1, 4), (1, 5), (2, 2), (5, 1), (5, 0))), # obstacles
        (frozenset(((0, 5),)), frozenset(((0, 4),)), frozenset(((0, 3),)), frozenset(((0, 2),))), # restrictions
        {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red'},
        {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red'}
        ),
    # Problem 27
    SokobanState("Start", 0, None,6, 5, # dimensions
        (5, 2), # robot
        {(4, 2): 0, (4, 1): 1, (3, 1): 2, (4, 3): 3, (3, 3): 4}, # boxes
        {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 3): 3, (1, 4): 4}, # storages
        frozenset(((2, 1), (2, 3), (2, 4), (2, 0),)), # obstacles
        (frozenset(((0, 0),)), frozenset(((0, 1),)),
         frozenset(((0, 2),)), frozenset(((1, 3),)), frozenset(((1, 4),))), # restrictions
        {0: 'magenta', 1: 'yellow', 2: 'red', 3: 'green', 4: 'blue'},
        {0: 'magenta', 1: 'yellow', 2: 'red', 3: 'green', 4: 'blue'}
        ),
    # Problem 28
    SokobanState("Start", 0, None,6, 5, # dimensions
        (5, 2), # robot
        {(3, 1): 1, (4, 1): 1, (4, 2): 1, (4, 3): 1, (3, 3): 1}, # boxes
        {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 3): 1, (1, 4): 1}, # storages
        frozenset(((2, 1), (2, 3), (2, 4), (2, 0))), # obstacles
        None
        ),
    # Problem 29
    SokobanState("Start", 0, None,7, 5, # dimensions
        (5, 2), # robot
        {(1, 1): 0, (4, 2): 1, (4, 1): 2, (3, 1): 3, (4, 3): 4, (3, 3): 5}, # boxes
        {(6, 2): 0, (0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 3): 4, (1, 4): 5}, # storages
        frozenset(((2, 1), (2, 3), (2, 4),)), # obstacles
        (frozenset(((6, 2),)), frozenset(((0, 0),)), frozenset(((0, 1),)),
         frozenset(((0, 2),)), frozenset(((1, 3),)), frozenset(((1, 4),))), # restrictions
        {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red', 4: 'green', 5: 'blue'},
        {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red', 4: 'green', 5: 'blue'}
        ),
    # Problem 30
    SokobanState("Start", 0, None,7, 5, # dimensions
        (5, 2), # robot
        {(1, 1): 0, (3, 1): 1, (4, 1): 1, (4, 2): 1, (4, 3): 1, (3, 3): 1}, # boxes
        {(6, 2): 0, (0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 3): 1, (1, 4): 1}, # storages
        frozenset(((2, 1), (2, 3), (2, 4),)), # obstacles
        (frozenset(((6, 2),)), frozenset(((0, 0), (0, 1), (0, 2), (1, 3), (1, 4),))), # restrictions
        {0: 'cyan', 1: 'magenta'},
        {0: 'cyan', 1: 'magenta'}
        ),
    # Problem 31
    SokobanState("Start", 0, None, 6, 6, # dimensions
        (0, 0), # robot
        {(4, 1): 0, (4, 2): 1, (4, 3): 2, (4, 4): 3}, # boxes
        {(0, 2): 0, (0, 3): 1, (1, 3): 2, (0, 5): 3}, # storages
        frozenset(((0, 1), (1, 1), (2, 1), (2, 2), (2, 3))), # obstacles
        None
        ),
    # Problem 32
    SokobanState("Start", 0, None, 5, 5, # dimensions
        (4, 1), # robot
        {(1, 3): 0, (1, 1): 1, (3, 2): 2}, # boxes
        {(0, 1): 0, (4, 2): 1, (0, 3): 2}, # storages
        frozenset(((0, 0), (1, 0), (0, 4), (1, 4))), # obstacles
        (frozenset(((1, 0),)), frozenset(((4, 2),)), frozenset(((0, 3),))), # restrictions
        {0: 'cyan', 1: 'magenta', 2: 'yellow'},
        {0: 'cyan', 1: 'magenta', 2: 'yellow'}
        ),
    # Problem 33
    SokobanState("Start", 0, None, 5, 5, # dimensions
        (2, 2), # robot
        {(1, 1): 0, (1, 2): 0, (1, 3): 0, (3, 1): 1, (3, 2): 1, (3, 3): 1}, # boxes
        {(0, 1): 1, (0, 2): 1, (0, 3): 1, (4, 1): 0, (4, 2): 0, (4, 3): 0}, # storages
        frozenset(), # No obstacles
        (frozenset(((4, 1), (4, 2), (4, 3),)), frozenset(((0, 1), (0, 2), (0, 3)))),
        {0: 'cyan', 1: 'magenta'},
        {0: 'cyan', 1: 'magenta'}
        ),
    # Problem 34
    SokobanState("Start", 0, None, 7, 5, # dimensions
        (6, 2), # robot
        {(3, 2): 0, (5, 2): 1, (3, 3): 1, (3, 1): 2, (4, 3): 2}, # boxes
        {(0, 1): 0, (0, 2): 1, (1, 2): 1, (0, 3): 2, (1, 3): 2}, # storages
        frozenset(((0, 4), (1, 4), (0, 0), (1, 0), (1, 1), (3, 0), (4, 4))), # walls
        (frozenset(((0, 1),)), frozenset(((0, 2), (1, 2))), frozenset(((0, 1), (0, 2), (1, 2), (0, 3), (1, 3)))), # restrictions
        {0: 'cyan', 1: 'magenta', 2: 'normal'},
        {0: 'cyan', 1: 'magenta', 2: 'yellow'}
        ),
    # Problem 35
    SokobanState("Start", 0, None, 7, 5, # dimensions
        (6, 2), # robot
        {(3, 3): 0, (3, 2): 1, (3, 1): 2, (4, 3): 3, (5, 2): 4}, # boxes
        {(0, 3): 0, (1, 3): 1, (0, 2): 2, (1, 2): 3, (0, 1): 4}, # storages
        frozenset(((0, 4), (1, 4), (0, 0), (1, 0), (1, 1), (3, 0), (4, 4))), # walls
        None,
        ),
    # Problem 36, Boxxle 1 problem 6 with simplification
    SokobanState("Start", 0, None, 9, 11, # dimensions
        (7, 0), # robot
        {(3, 5): 0, (3, 7): 1, (5, 7): 2, (5, 5): 3}, # boxes
        {(3, 3): 0, (1, 7): 1, (5, 9): 2, (7, 5): 3}, # storages
        frozenset(((4, 6), (6, 0), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (2, 2), (1, 2), (0, 2),
            (0, 8), (0, 9), (0, 10), (6, 10), (7, 10), (8, 10), (8, 3), (8, 4),
            (6, 3), (5, 3), (4, 3), (3, 4), (1, 4), (1, 5), (1, 6), (2, 7), (2, 9),
            (3, 9), (4, 9), (5, 8), (7, 8), (7, 7), (7, 6), (6, 5))), # obstacles
        (frozenset(((3, 3),)), frozenset(((1, 7),)), frozenset(((5, 9),)), frozenset(((7, 5),))),
        {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red'},
        {0: 'cyan', 1: 'magenta', 2: 'yellow', 3: 'red'}
        ),
    # Problem 37, Boxxle 1 problem 7
    SokobanState("Start", 0, None, 8, 6, # dimensions
        (7, 0), # robot
        {(2, 2): 0, (3, 4): 1, (4, 2): 2, (6, 2): 2, (3, 3): 2}, # boxes
        {(0, 5): 0, (1, 5): 1, (2, 5): 2, (3, 5): 2, (4, 5): 2}, # storages
        frozenset(((2, 0), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4), (7, 5), (7, 4),
            (5, 0), (5, 1), (5, 3), (5, 4), (4, 3))), # obstacles
        (frozenset(((0, 5),)), frozenset(((1, 5),)), frozenset(((2, 5), (3, 5), (4, 5)))),
        {0: 'cyan', 1: 'magenta', 2: 'yellow'},
        {0: 'cyan', 1: 'magenta', 2: 'yellow'}
        ),
    # Problem 38, Boxxle 1 problem 9
    SokobanState("Start", 0, None, 9, 7, # dimensions
        (7, 6), # robot
        {(1, 5): 0, (4, 5): 0, (7, 5): 0, (7, 2): 1, (1, 2): 2, (4, 1): 2}, # boxes
        {(3, 3): 0, (4, 3): 0, (5, 3): 0, (5, 4): 1, (4, 4): 2, (3, 4): 2}, # storages
        frozenset(((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (2, 4), (2, 3), (3, 2), (4, 2), (5, 2),
            (6, 3), (6, 4), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (3, 0), (4, 0))), # obstacles
        (frozenset(((3, 3), (4, 3), (5, 3),)), frozenset(((5, 4),)), frozenset(((4, 4), (3, 4),))),
        {0: 'cyan', 1: 'magenta', 2: 'yellow'},
        {0: 'cyan', 1: 'magenta', 2: 'yellow'}
        ),
    # Problem 39, Boxxle 1 problem 9 (no hints)
    SokobanState("Start", 0, None, 9, 7, # dimensions
        (7, 6), # robot
        {(1, 5): 0, (4, 5): 0, (7, 5): 0, (7, 2): 1, (1, 2): 2, (4, 1): 2}, # boxes
        {(3, 3): 0, (4, 3): 0, (5, 3): 0, (5, 4): 1, (4, 4): 2, (3, 4): 2}, # storages
        frozenset(((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (2, 4), (2, 3), (3, 2), (4, 2), (5, 2),
            (6, 3), (6, 4), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0), (3, 0), (4, 0))), # obstacles
        None,
        )
)