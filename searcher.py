#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Jason Wang
# email: jasonw77@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *


class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ initializes the Searcher class with 3 attributes: states, num_tested, depth_limit
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
    
    def add_state(self, new_state):
        """ takes a single State object called new_state and adds it to the Searcher‘s 
            list of untested states.
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """ takes a State object called state and returns True if the called Searcher 
            should add state to its list of untested states, and False otherwise.
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True
        
        
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes the elements of new_states one at a time as follows:
            If a given state s should be added to the Searcher‘s list of untested states ,the method should use the Searcher‘s add_state() method to add s to the list of states.
            If a given state s should not be added to the Searcher object’s list of states, the method should ignore the state.
        """
        for x in new_states:
            if self.should_add(x) == True:
                self.add_state(x)

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """ performs a full state-space search that begins at the specified initial state init_state and ends 
            when the goal state is found or when the Searcher runs out of untested states.
        """
        self.add_state(init_state)
        while self.states != []:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None

### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ a class called BFSearcher for searcher objects that perform breadth-first search (BFS) instead of random search.
        Is a subclass of the Searcher class
    """
    def next_state(self):
        """ overrides (i.e., replaces) the next_state method that is inherited from Searcher. Rather than choosing at random 
            from the list of untested states, this version of next_state should follow FIFO (first-in first-out) ordering – 
            choosing the state that has been in the list the longest.
        """
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """ a class called DFSearcher for searcher objects that perform depth-first search (DFS) instead of random search.
        Is a subclass of the Searcher class
    """
    def next_state(self):
        """ overrides (i.e., replaces) the next_state method that is inherited from Searcher. Rather than choosing at random 
            from the list of untested states, this version of next_state should follow LIFO (last-in first-out) ordering – 
            choosing the state that was most recently added to the list
        """
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ takes a State object called state, and that computes and returns an estimate 
        of how many additional moves are needed to get from state to the goal state.
    """
    misplaced = state.board.num_misplaced()
    return misplaced 

def h2(state):
    """ computes the difference between the tile number's indices and the goal state's indices for the same number
    """
    
    diff = 0
    for r in range(3):
        for c in range(3):
            number  = state.board.tiles[r][c]
            if number == '1':
                dr = abs(r - 0)
                dc = abs(c - 1)
                diff += dr
                diff += dc
            elif number == '2':
                dr = abs(r - 0)
                dc = abs(c - 2)
                diff += dr
                diff += dc    
            elif number == '3':
                dr = abs(r - 1)
                dc = abs(c - 0)
                diff += dr
                diff += dc
            elif number == '4':
                dr = abs(r - 1)
                dc = abs(c - 1)
                diff += dr
                diff += dc
            elif number == '5':
                dr = abs(r - 1)
                dc = abs(c - 2)
                diff += dr
                diff += dc
            elif number == '6':
                dr = abs(r - 2)
                dc = abs(c - 0)
                diff += dr
                diff += dc
            elif number == '7':
                dr = abs(r - 2)
                dc = abs(c - 1)
                diff += dr
                diff += dc
            elif number == '8':
                dr = abs(r - 2)
                dc = abs(c - 2)
                diff += dr
                diff += dc
                
        
    return diff

            
            


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """ initializes a new GreedySearcher object
        """
        super().__init__(-1)
        self.heuristic = heuristic
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
        
    def add_state(self, state):
        """ the method should add a sublist that is a [priority, state] pair, 
            where priority is the priority of state that is determined by calling the priority method
        """
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """ This version of next_state should choose one of the states with the highest priority.
        """
        s = max(self.states)
        self.states.remove(s)
        return s[1]
        
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ an informed search algorithm that assigns a priority to each state based on a heuristic function, 
        and that selects the next state based on those priorities. Takes into account the cost that has 
        already been expended to get to that state.
    """
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
        
        
        
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
        
    
