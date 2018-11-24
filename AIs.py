'''
    Team 4 - Ben Duggan & Connor Altic
    11/23/18
    Class that contains all of the AIs used
'''

from Cube import *

'''
First AI tested.  Not an efficient AI as no heuristic is used and there is a large branching factor ~3*n
'''
class BFS:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        goal_state = Cube(self.cube.size).__hash__()
        depth = 0
        if self.cube.__hash__() == goal_state:
            print('Found goal at depth ' + str(depth))
            return 'yes'

        seen = set()
        seen.add(self.cube.__hash__())
        fringe = {}
        fringe[self.cube.__hash__()] = self.cube

        while True:
            depth += 1
            print(depth)
            new_fringe = {}
            for i in fringe:
                children = fringe[i].children('prime')
                for j in children:
                    if j.__hash__() == goal_state:
                        print('Found goal at depth ' + str(depth))
                        return 'yes'
                    if j.__hash__() not in fringe and j.__hash__() not in seen:
                        new_fringe[j.__hash__()] = j
                        seen.add(j.__hash__())
            fringe = new_fringe
            print(len(fringe))

class A_star:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        pass

class Bidirectional_A_star:
    def __init__(self, cube):
        self.cube = cube

    def solve(self):
        pass