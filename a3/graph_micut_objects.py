#-------------------------------------------------------------------------------------#
#------------------------------------- Introduction ----------------------------------#
#-------------------------------------------------------------------------------------#

print ("Assignment 3\n",
       "Course: Design and analysis of algorithms, part-1\n",
       "Author: Siva Patibandla\n",
       "Date: July 21 2015");

#-------------------------------------------------------------------------------------#
#------------------------------------- Globals ---------------------------------------#
#-------------------------------------------------------------------------------------#

import random;
import math;
import sys;
import copy;
import cProfile as profile;

class Node:
    def __init__(self, name):
        self._name = name;
        self.adj_nodes = [];
        self.index = sys.maxsize;
    def __str__(self):
        s = "name: " + str(self._name) + " index: " + str (self.get_index()) + " adj nodes:";
        for node in self.adj_nodes:
            s += " " + str(node._name);
        return s;
        
    def del_self_edges(self):
        index = 0;
        while index < len (self.adj_nodes):
            adj_node = self.adj_nodes[index];
            if self._name == adj_node._name:
                end_index = len (self.adj_nodes) - 1;
                self.adj_nodes[index] = self.adj_nodes[end_index];
                self.adj_nodes.pop();
            else:
                index += 1;
    #Interestingly, the perf. of del_self_edges_filter() is 2x the del_self_edges().  
    def del_self_edges_filter(self):
        self.adj_nodes[:] = list(filter(lambda node: self._name != node._name, self.adj_nodes));
    def add_adj_node(self, adj_node):
        self.adj_nodes.append(adj_node);
    
    def get_num_adj_nodes(self):
        return len(self.adj_nodes);
    def get_rand_adj_node(self):
        if len(self.adj_nodes) > 0:
            return self.adj_nodes[random.randint(0, len(self.adj_nodes)-1)];
        return None;
    def get_index (self):
        return self.index;
    def set_index (self, index):
        self.index = index;
    def get_adj_nodes(self):
        return self.adj_nodes;

#Alternate idea: Even make the adjacent nodes also as a node. 
#Algorithm: whenever you see an adjacent node make a node and append it to nodes list, and 
#append it to the adjacent nodes list. 
class Graph:
    def __init__(self):
        self.nodes = [];
        self.num_nodes = 0;
    def __str__(self):
        s = "";
        for node in self.nodes:
            s += str(node) + "\n";
        return s;
    
    def add_node (self, name):
        present = False;
        node = None;
        for existing_node in self.nodes:
            if existing_node._name == name:
                present = True;
                node = existing_node;
                break;
        if not present:
            node = Node (name);
            node.set_index(len(self.nodes));
            self.nodes.append(node);
        return node;
    def del_node (self, node):
        #print ("Deleting node name: ", node._name, " index: ", node.get_index());
        end_node = self.nodes[len(self.nodes)-1];
        self.nodes[node.get_index()] = end_node;
        end_node.set_index(node.get_index());
        self.nodes.pop();
        
    def get_num_nodes(self):
        return len(self.nodes);
    def get_rand_node(self):
        if len(self.nodes) > 0:
            index = random.randint(0, len(self.nodes)-1);
            node = self.nodes[index];
            assert node.get_index() == index;
            return node;
        return None;

#-------------------------------------------------------------------------------------#
#------------------------------------- Functions -------------------------------------#
#-------------------------------------------------------------------------------------#

def contract_edge (graph, src, dest):
    #print ("Contracting edge between ", src._name, " src index: " , src.get_index(), " and ", dest._name(), " dest index: ", dest.get_index());
    
    #Add the neighbors of dest node to src node
    for node in dest.get_adj_nodes():
        src.adj_nodes.append(node);
    
    #Replace the dest node with src node throughout the graph
    for node in graph.nodes:
        for index, adj_node in enumerate(node.adj_nodes):
            if adj_node._name == dest._name:
                node.adj_nodes[index] = src;
    
    #delete the destination node
    graph.del_node(dest);
    
    src.del_self_edges();
    #src.del_self_edges_filter();
    
def find_min_cut(graph):
    while graph.get_num_nodes() > 2:
        #Select an edge at random
        src = graph.get_rand_node();
        dest = src.get_rand_adj_node();
        #Contract the edge between src and dest nodes in the graph
        contract_edge (graph, src, dest);
        #print (graph);
    assert graph.nodes[0].get_num_adj_nodes() == graph.nodes[1].get_num_adj_nodes();    
    return graph.nodes[0].get_num_adj_nodes();

#-------------------------------------------------------------------------------------#
#------------------------------------- Main program ----------------------------------#
#-------------------------------------------------------------------------------------#

def main():
    graph = Graph ();
    
    #f = open ('graph.txt', 'r');
    f = open ('kargerMinCut.txt', 'r');
    
    for line in f:
        words = line.split();
        words = [int (w) for w in words];
        src_node = graph.add_node (words[0]);
        for word in words[1:]:
            node = graph.add_node(word);
            src_node.add_adj_node(node);
    #print (graph);
    
    n = graph.get_num_nodes();
    repeat = int (n * (n-1) * math.log(n) / 2);
    repeat = min (100, repeat);
    print ("No. of repetitions required: ", repeat);
    
    min_cut = sys.maxsize;
    max_cut = 0;
    graph_copy = copy.deepcopy(graph);
    while repeat > 0:
        cut = find_min_cut(graph);
        if cut < min_cut:
            min_cut = cut;
        if cut > max_cut:
            max_cut = cut;
        graph = copy.deepcopy(graph_copy);
        repeat -= 1;
    
    print ("Graph's min-cut: ", min_cut, " max-cut: ", max_cut);

def test():
    
    #Example for random number generation
    #The sequence of random numbers returned by this library function may not be the same in each run
    #if a & b are arguments to the randint function, random number returned is such that a<=random<=b.
    for i in range (10):
        print ("iteration: ", i, " random: ", random.randint(0, 9));
    
    #Example for pop operation with lists
    l = [1,2,3];
    l.pop(); #run time of pop() is O(1);
    l.append(4); #run time of append() is O(1)
    print (l);
    print (l[-1])
    
#Script
main();
#profile.run ('main()');
