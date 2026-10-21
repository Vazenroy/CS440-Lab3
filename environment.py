import numpy as np
import vacuum
from HillClimbingAgent import HillClimbingAgent
from SimulatedAnnealing import SimulatedAnnealing

class environment():
    #creates environment
    def __init__(self):
        self.env = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    # different testing env
    def set_HC_env(self):
        self.env = [[0,3,2,0],
               [0,0,0,0],
               [0,4,6,8],
               [7,9,0,10]]
    
    # different testing env
    def set_SA_env(self):
        self.env = [[0,3,2,0],
               [3,6,0,0],
               [5,0,6,8],
               [4,9,0,10]]
        
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
    def get_percept(self, V):
        row = V.row
        col = V.col

        curr = self.env[row][col]
        neighbors = {}
        #check if valid move, if not, it isn't added to percept. 
        if row > 0:
            neighbors['Up'] = self.env[row - 1][col]
        if row < 3:
            neighbors['Down'] = self.env[row + 1][col]
        if col > 0:
            neighbors['Left'] = self.env[row][col - 1]
        if col < 3:
            neighbors['Right'] = self.env[row][col + 1]
        
        return curr, neighbors

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
    env.set_HC_env()
    V = HillClimbingAgent(env)
    env.insert_vacuum(V, 0,3)

    #WORKING HILL CLIMB ALGORITHM.
    print("\033[31mRunning Hill Climbing Algorithm:\033[0m",end=" ")
    completed = False
    while completed == False:
        print("Current location:", V.row, V.col)
        env.draw_environment()
        print()
        curr, neighbors = env.get_percept(V)
        direction = V.choose_move(curr, neighbors)
        if direction =='NoOp':
            print("Hill climbing maximum found at:",V.row, V.col)
            completed = True # dirt max found
        else:
            print("Moved", direction)
            env.move(V,direction)
    
    envSA = environment()
    envSA.set_SA_env()
    V_sa = SimulatedAnnealing(env)
    envSA.insert_vacuum(V_sa, 0, 3)

    #WORKING SIMULATED ANNEALING ALGORITHM
    print("\033[31mRunning Simulated Annealing Algorithm:\033[0m",end=" ")
    completedSA = False
    t = 1
    while completedSA == False:
        #print current environment state
        print("Current location:", V_sa.row, V_sa.col)
        envSA.draw_environment()
        print()

        #Run simulated annealing once
        curr, neighbors = envSA.get_percept(V_sa)
        direction = V_sa.choose_move(curr, neighbors, t)
        if direction == 'Highest Found':
            print("Simulated annealing maximum found at:",V_sa.row, V_sa.col)
            completedSA = True
        else:
            print()
            print("Moved", direction)
            env.move(V_sa, direction)
        t += 1
