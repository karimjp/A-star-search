'''
Created on Jan 31, 2016

@author: karim
'''

import Queue
from Search.GraphNode import Node
import pdb

class A_Star_Search(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.frontier = Queue.PriorityQueue();
        self.explored = []
        self.current_state = ()
        self.goal = None
        self.goal_y = None
        self.goal_x = None
        self.world = None
        self.moves=None
        self.costs=None
        
        
    def set_properties(self, world, costs, goal, moves):
        self.set_goal(goal)
        self.set_world(world)
        self.set_costs(costs)
        self.set_moves(moves)
        
    def a_star_search(self, world, costs, start, goal, moves):
        self.set_properties(world, costs, goal, moves)
        print "Starting A Star Search"
        node = self.create_graph_node(start)
        self.add_frontier_element((node.get_fn(), node))
        while self.is_frontier_not_empty():
            current_tuple = self.get_frontier_element()
            current_node = current_tuple[1]
            #print current_node.get_state()
            #do goal test
            if self.is_terminal(current_node):
                print "A Star Search Completed"
                return self.getPath(current_node)
                
            
            children = self.successor(current_node)
            for child in children:
                undiscovered_childs = not bool( self.is_in_queue(child, self.get_frontier()) or 
                    self.is_in_list(child, self.get_explored()) )
                if undiscovered_childs:
                    self.add_frontier_element((child.get_fn(), child))
                self.get_explored().append(current_node)
        
                    
                
    def create_graph_node(self, state, minimum_cost=None, parent=None):
        node = Node(state)
        cost = node.calculate_cost(self.get_world(), self.get_costs())
        node.set_cost(cost)
        node.set_parent(parent)
        #pdb.set_trace()
        #Handler for root node
        if not parent:
            node.set_gn(0 + cost)
            hn = self.heuristic(node, cost)
        else:
            node.set_gn(parent.get_gn() + cost)
            hn = self.heuristic(node, minimum_cost)
        node.set_hn(hn)
        node.set_fn(node.evaluate_fn(cost, hn))
        return node
    
    def successor(self, current_node):
        '''
        Returns discovered children list as graph nodes.
        '''
        return self.get_children(current_node)
    
    def get_children(self, current_node):
        '''
        Creates children from current_node.
        '''
        children=[]
        children_states = self.get_new_moves(current_node)
        heuristic_minimum_cost = self.get_minimum_cost(children_states)
        for state in children_states:
            children.append(self.create_graph_node(state, heuristic_minimum_cost, current_node))
        return children
    
    def get_new_moves(self, current_node):
        y = current_node.get_y()
        x = current_node.get_x()
        node_position = y,x
        new_moves =[]
        for move in self.get_moves():
            new_move = self.add_tuples(node_position, move)
            new_move_x = new_move[1]
            new_move_y = new_move[0]
            illegal_move = bool( self.is_negative_num_in(new_move) or
                new_move_x >= len(self.get_world()[y]) or 
                new_move_y >= len(self.get_world()) or
                self.world[new_move_y][new_move_x] == "x")
            if not illegal_move:
                new_moves.append(new_move)
        return new_moves    
    
    def get_minimum_cost(self, moves):
        '''
        Gets the minimum cost from all current node permissible adjacent states 
        '''
        minimum_cost = Node(moves[0]).calculate_cost(self.get_world(), self.get_costs())
        for move in moves:
            if minimum_cost >Node(move).calculate_cost(self.get_world(), self.get_costs()):
                minimum_cost = Node(move).calculate_cost(self.get_world(), self.get_costs())
        return minimum_cost          
        
    def heuristic(self, node, minimum_cost):
        '''
        Using Manhattan distance.  Returns h(x)
        '''
        dy = abs(node.get_y() - self.goal_y)
        dx = abs(node.get_x() - self.goal_x)
        #pdb.set_trace()
        return minimum_cost * (dx + dy)
     
    def is_in_queue(self, item, queue):
        found = False
        temp_list = []
        while not queue.empty():
            current_tuple = queue.get_nowait()
            current_node = current_tuple[1]
            temp_list.append(current_node)
            
        for temp_element in temp_list:
            if item.get_state() == temp_element.get_state():
                found = True
                break
            
        for temp_element in temp_list:
            queue.put_nowait((temp_element.get_fn(), temp_element));
            
        return found
    
    def is_in_list(self, item, lst):
        found = False
        for temp_element in lst:
            if item.get_state() == temp_element.get_state():
                found = True
        return found
      
    def add_tuples(self, tuple_a, tuple_b):
        return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])    
        
    def is_negative_num_in(self, moves):
        for item in moves:
            if item < 0:
                return True
        return False
    
    def is_restricted_space(self, moves):
        self.world[moves]
    def is_frontier_not_empty(self):
        return not self.get_frontier().empty()

    def get_frontier_element(self):
        return self.get_frontier().get_nowait()
    
    def add_frontier_element(self,value):
        return self.get_frontier().put_nowait(value)
    
    def getPath(self,current_node):
        path=[]
        path.append(current_node.get_state())
        parent = current_node.get_parent()
        while parent:
            path.append(parent.get_state())
            parent = parent.get_parent()
        return path
    
    def is_terminal(self, current_node):
        return (True if current_node.get_state() == self.get_goal() else False)
    
    def get_moves(self):
        return self.moves


    def set_moves(self, value):
        self.moves = value


    def get_world(self):
        return self.world


    def set_world(self, value):
        self.world = value

        
    
    def get_costs(self):
        return self.costs

    def set_costs(self, value):
        self.costs = value

        
    def get_frontier(self):
        return self.frontier


    def get_explored(self):
        return self.explored


    def get_current_state(self):
        return self.current_state


    def get_goal(self):
        return self.goal
    
    def get_goal_x(self):
        return self.goal_x
    
    def get_goal_y(self):
        return self.goal_y


    def set_frontier(self, value):
        self.frontier = value


    def set_explored(self, value):
        self.explored = value


    def set_current_state(self, value):
        self.current_state = value


    def set_goal(self, value):
        self.goal = value
        self.goal_x = value[1]
        self.goal_y = value[0]

        
    
    
    
        
        
