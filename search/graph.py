import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object

        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")




    def shortest_path(self, pred, start, end):
        """
        takes in dict of predecessors and finds shortest path
        starts from end node and works backwards to start 

        in predecessor dict: value is predecessor of key

        """
        path_list=[end]
        new_end=end

        #value of old key becomes new key
        while new_end != start:
            path_list.append(pred[new_end])
            new_end=pred[new_end]
        
        return(path_list[::-1])



    def bfs(self, start, end=None):
        """
        Performs breadth first traversal and pathfinding on graph G
        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        G=self.graph


         #check that G is not an empty graph
        if nx.is_empty(G):
            raise Exception(f"Graph is empty!")

    
        #check that start and end nodes exists in graph 
        if start not in G:
            raise ValueError(f"Start node not in graph!")
        
        if (end not in G) and (end != None):
            raise ValueError(f"End node not in graph!")
        
    
        #lists of visted nodes and nodes to visit in queue
        queue=[start]
        visited=[start]

        #dictionary of predecessors
        pred={}
        pred[start]=None

        #loop through while queue is not empty 
        while queue:
            #pop first element of queue and get neighbors
            v=queue.pop(0)
            N=G.neighbors(v)

            #check each neighbor of current node
            for w in N:
                if w not in visited:
                    #add queue node as predecessor to frontier node
                    pred[w] = v
                    #add new frontier nodes to queue and visited
                    queue.append(w)
                    visited.append(w)
                    


        #values returned depend on end node value
        #already checked that end node exists in graph
 
        if end == None:
            #return list of nodes with order of BFS traversal
            return(visited)

        #has end node input and has path
        elif nx.has_path(self.graph, start, end):
            #turn predecessors dict into list of shortest path 
            return(self.shortest_path(pred, start, end)) 

        #has existing end node but no path
        else:
            return(None)


       



        




