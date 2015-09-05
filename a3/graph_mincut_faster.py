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
    def __init__(self, name, adj_nodes):
        self.name = name;
        self.adj_nodes = adj_nodes;
    def __str__(self):
        return "name: " + str(self.name) + " adj_nodes: " + str(self.adj_nodes);
    def get_num_adj_nodes(self):
        return len(self.adj_nodes);

class Graph:
    def __init__(self):
        self.nodes = [];
    def add_node (self, node):
        self.nodes.append(node);
    def __str__(self):
        s = "";
        for node in self.nodes:
            s += str(node) + "\n";
        return s;
    def get_num_nodes(self):
        return len(self.nodes);
    def get_node_by_name(self, name):
        for node in self.nodes:
            if node.name == name:
                return node;

#-------------------------------------------------------------------------------------#
#------------------------------------- Functions -------------------------------------#
#-------------------------------------------------------------------------------------#

def contract_edge (graph, src, dest):
    #print ("Contracting edge between ", src.name, " and ", dest.name);
    
    #Add the neighbors of dest node to src node
    for neighbor in dest.adj_nodes:
        src.adj_nodes.append(neighbor);
        
    #Replace the edges with dest as the destination node with src node
    for node in graph.nodes:
        for index, edge in enumerate(node.adj_nodes):
            if edge == dest.name:
                node.adj_nodes[index] = src.name;
                
    #delete the destination node from graph
    graph.nodes[:] = list(filter(lambda node: node.name != dest.name, graph.nodes));
    
    #delete self edges
    src.adj_nodes[:] = list(filter(lambda name: src.name != name, src.adj_nodes));
    
def find_min_cut(graph):
    while graph.get_num_nodes() > 2:
        #Select an edge at random
        src = random.choice(graph.nodes);
        dest = graph.get_node_by_name (random.choice(src.adj_nodes));
        
        #contract the edge between src and dest nodes in the graph
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
        node = Node (words[0], words[1:]);
        graph.add_node (node);
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

#script
main();
#profile.run ('main()');
