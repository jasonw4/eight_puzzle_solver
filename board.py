#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Jason Wang
# email: jasonw77@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        count = 0
        while count < 9:
            for r in range(len(self.tiles)):
                for c in range(len(self.tiles[0])):
                    self.tiles[r][c] = digitstr[count]
                    count += 1
                    if self.tiles[r][c] == '0':
                        self.blank_r = r
                        self.blank_c = c


    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of the board
        """
        s = ''
        for r in range(3):
            s += '\n'
            for c in range(3):
                if self.tiles[r][c] == '0':
                    s += '_ '
                else:    
                    s += self.tiles[r][c] + ' '
                    
                    
        s += '\n'
    
        
        
   

        return s[1:]
    
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction in which 
            the blank should move, and that attempts to modify the contents of the 
            called Board object accordingly.
        """
        if direction == 'up':
            if self.blank_r-1 in range(3):
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r-1][self.blank_c]
                self.tiles[self.blank_r-1][self.blank_c] = "0"
                self.blank_r -= 1
                return True
            else: 
                return False
        elif direction == 'down':
            if self.blank_r+1 in range(3):
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r+1][self.blank_c]
                self.tiles[self.blank_r+1][self.blank_c] = '0'
                self.blank_r += 1
                return True
            else: 
                return False
        elif direction == 'left':
            if self.blank_c-1 in range(3):
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c-1]
                self.tiles[self.blank_r][self.blank_c-1] = '0'
                self.blank_c -= 1
                return True
            else: 
                return False
        elif direction == 'right':
            if self.blank_c+1 in range(3):
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c+1]
                self.tiles[self.blank_r][self.blank_c+1] = '0'
                self.blank_c += 1
                return True
            else: 
                return False
        else:
            return False
        
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the current contents of the called Board object’s tiles attribute
        """
        s = ''
        for r in self.tiles:
            for c in r:
                s += c
        return s
    
    
    def copy(self):
        """ returns a newly-constructed Board object that is a 
            deep copy of the called object
        """

        return Board(self.digit_string())
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object that 
            are not where they should be in the goal state.
        """
        notright = 0
        for r in range(len(GOAL_TILES)):
            for c in range(len(GOAL_TILES[0])):
                if self.tiles[r][c] == '0':
                    notright += 0
                elif GOAL_TILES[r][c] != self.tiles[r][c]:
                    notright += 1
        return notright
    
    def __eq__(self, other):
        """ compares the two Board objects. The method should return True
            if the called object (self) and the argument (other) have the same values 
            for the tiles attribute, and False otherwise
        """
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != other.tiles[r][c]:
                    return False
        return True
            
        
                    
            
    
    
    
    
    
    
    
    
    
    
    
    
