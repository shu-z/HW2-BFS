# write tests for bfs
import pytest
import networkx as nx
from search import Graph


def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    G_tiny=Graph('./data/tiny_network.adjlist')
    
    #bfs with only start 
    traversed_G_tiny=(G_tiny.bfs('Lani Wu'))

    #check number of nodes traversed
    assert len(traversed_G_tiny) == 30

    #check order of nodes traversed
    assert traversed_G_tiny 

   #check correct number of nodes
   #check node order ? 

    #assert 
    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    G_cit=Graph('./data/citation_network.adjlist')

    pair_list=[('Lani Wu', 'Martin Kampmann'), 
            ('Hani Goodarzi', 'Tanja Kortemme'),
            ('Tony Capra', 'Jimmie Ye') ]

    #check shortest path against networkx shortest path 
    for pair in pair_list:
        #find all possible shortest paths for given pair
        all_shortest=[x for x in nx.all_shortest_paths(G_cit.graph, pair[0], pair[1])]
        #check that path output is one of all possible shortest
        assert  G_cit.bfs(pair[0], pair[1]) in all_shortest, "Shortest path detected incorrect"
    

    #check if nodes unconnected
    assert G_cit.bfs('Hao Li', 'Bruce Conklin') == None, "Unconnected nodes does not return None"


    
    



def test_bfs_edgecase():

    #read in empty graph 
    G_empty=Graph('./data/empty_graph.adjlist')

    #make sure exception is raised
    with pytest.raises(ValueError):
        G_empty.bfs(start=0)


    G_tiny=Graph('./data/tiny_network.adjlist')
   
   
   #test nonexistent start node 

    with pytest.raises(ValueError):
        G_tiny.bfs(start='Nonexistent faculty member')



   #test nonexistent end node if end node given

    assert G_tiny.bfs(start='Luke Gilbert', end='Nonexistent faculty') == None, "Incorrect end node does not return None"




 





