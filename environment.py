import numpy as np
import vacuum
from MDPAgent import MDPAgent;

class environment():
    #creates environment
    def __init__(self):
        self.env = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    
    def set_MDP_env(self):
        self.env = [[0,0,0,0],
               [0,'X',0,0],
               [0,0,0,0],
               [0,-1,0,10]]
        
    # inserts vacuum 
    def insert_vacuum(self, V, row, col):
        V.dirt_level = self.env[row][col]
        V.row = row
        V.col = col
        self.vacuum = V

    # prints the environment as not <python_object> and places vacuum visually without overriding data
    def draw_environment(self):
        for row in range(4):
            for col in range(4):
                if row == self.vacuum.row and col == self.vacuum.col:
                    print("\033[31mV\033[0m",end=" ") # the weird text is to make it red to make it easier to see
                else:
                    print(self.env[row][col], end = " ")
            print() # newline

    # shows perceptible squares from where the vacuum is
    def get_valid_states(self, V):
        row = V.row
        col = V.col

        curr = self.env[row][col]
        states = {}
        #check if valid move, if not, it isn't added. 
        if row > 0:
            if self.env[row - 1][col] != 'X':
                neighbors['Up'] = self.env[row - 1][col]
        if row < 3:
            if self.env[row + 1][col] != 'X':
                neighbors['Down'] = self.env[row + 1][col]
        if col > 0:
            if self.env[row][col - 1] != 'X':
                neighbors['Left'] = self.env[row][col - 1]
        if col < 3:
            if self.env[row][col + 1] != 'X':
                neighbors['Right'] = self.env[row][col + 1]
        
        return curr, states

    # actually moves the vacuum 
    def move(self, V, direction):
        if direction == 'Up':
            V.row -= 1
        if direction == 'Down':
            V.row += 1
        if direction == 'Left':
            V.col -= 1
        if direction == 'Right':
            V.col += 1
        else:
            pass

# main statement just to prove that it works 
if __name__ == "__main__":
    env = environment()
    env.set_MDP_env()
    V = MDPAgent(env)
    env.insert_vacuum(V, 0,3)
