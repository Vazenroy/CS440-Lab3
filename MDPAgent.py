import vacuum
class MDPAgent(vacuum.vacuum):
    def call_MDP(self, live_cost):
        self.living_cost = live_cost
        self.disc_factor = 0.9
    
    def get_trans_outcomes(state, action):

    def choose_move(self, env):
