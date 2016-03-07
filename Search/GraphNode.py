'''
Created on Jan 31, 2016

@author: karim
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self, state, gn=0, hn=0, fn=0, cost=None, parent=None):
        '''
        Constructor
        '''
        self.state = state
        self.gn = gn
        self.hn = hn
        self.fn = fn
        self.x = state[1]
        self.y = state[0]
        self.parent = parent
        self.cost = cost


            
    def evaluate_fn(self, gn, hn):
        '''
        evaluate_fn: calculates f(n) known in A* as the estimated
        cost of the cheapest solution through node n.
        parameters:
            gn = g(n), cost to reach a node
            hn = h(n), cost to get from node to goal
        '''
        return gn + hn
    
    def calculate_cost(self, world,costs):
        ascii = world[self.get_y()][self.get_x()]
        cost = costs[ascii]
        return cost
    
    def get_cost(self):
        return self.cost

    
    def set_cost(self, value):
        self.cost = value


    def get_state(self):
        return self.state


    def get_gn(self):
        return self.gn


    def get_hn(self):
        return self.hn


    def get_fn(self):
        return self.fn


    def get_x(self):
        return self.x


    def get_y(self):
        return self.y


    def get_parent(self):
        return self.parent

    def set_state(self, value):
        self.state = value

    def set_gn(self, value):
        self.gn = value


    def set_hn(self, value):
        self.hn = value


    def set_fn(self, value):
        self.fn = value


    def set_x(self, value):
        self.x = value


    def set_y(self, value):
        self.y = value


    def set_parent(self, value):
        self.parent = value


