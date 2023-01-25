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

    #make instance of tiny_network graph 
    G_tiny=Graph('./data/tiny_network.adjlist')
    
    #bfs with only start 
    traversed_G_tiny=(G_tiny.bfs('Michael Keiser'))

    #check number of nodes traversed
    assert len(traversed_G_tiny) == 30, "Not all nodes traversed"

    #check order of nodes traversed
    assert traversed_G_tiny[0:4]== ['Michael Keiser', '33232663', 'Charles Chiu','Martin Kampmann'], "Nodes traversed in wrong order"



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

    #make instance of citation network graph
    G_cit=Graph('./data/citation_network.adjlist')

    #pairs of start-end nodes to check
    pair_list=[('Lani Wu', 'Martin Kampmann'), 
            ('Hani Goodarzi', 'Tanja Kortemme'),
            ('Tony Capra', 'Jimmie Ye') ]

    #check shortest path against networkx shortest path 
    for pair in pair_list:
        #find all possible shortest paths for given pair
        all_shortest=[x for x in nx.all_shortest_paths(G_cit.graph, pair[0], pair[1])]
        #check that path output is one of all possible shortest
        assert  G_cit.bfs(pair[0], pair[1]) in all_shortest, "Shortest path detected incorrect"
    

    #check if unconnected nodes (but nodes that exist) return None
    assert G_cit.bfs('Hao Li', 'Bruce Conklin') == None, "Unconnected nodes does not return None"


    
    



def test_bfs_edgecase():
    """
    Additional edge cases to check

    """

    #read in empty graph 
    G_empty=Graph('./data/empty_graph.adjlist')

    #make sure exception is raised when given empty graph
    with pytest.raises(Exception):
        G_empty.bfs(start=0)


    #read in tiny graph
    G_tiny=Graph('./data/tiny_network.adjlist')
      
   #test nonexistent start node 
    with pytest.raises(ValueError):
        G_tiny.bfs(start='Nonexistent faculty member')

    #test nonexistent end node (when not None)
    with pytest.raises(ValueError):
        G_tiny.bfs(start='Luke Gilbert', end='Nonexistent faculty')




 





