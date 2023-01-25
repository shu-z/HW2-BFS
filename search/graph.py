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
        """
        path_list=[end]
        new_end=end

        while new_end != start:
            path_list.append(pred[new_end])
            new_end=pred[new_end]
        
        return(path_list[::-1])


        





   
    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G
        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        G=self.graph

         #check that it's not an empty graph
        if nx.is_empty(G):
            raise ValueError(f"Graph is empty!")

        #make sure to handle unconnected graph
       

        #check that start and end node exists in graph 



        #lists of visted nodes and nodes to visit in queue
        queue=[start]
        visited=[start]
        traversed=[start]

        #dictionary of predecessors
        pred={}
        pred[start]=None

        #loop through while queue is not empty 
        while queue:
            #print('current queue: ' + str(queue))
            #pop first element of queue!!!!
            v=queue.pop(0)
            #print(v)
            N=G.neighbors(v)
            traversed.append(v)
            
            #print(dict(enumerate(N)))
            
            for w in N:
                if w not in visited:
                    #print('current w: ' + str(w))
                    pred[w] = v
                    visited.append(w)
                    queue.append(w)
                    #print('visted: ' + str(visited))


        
        if end == None:
            #return list of nodes with order of BFS traversal

            return(visited)


        elif nx.has_path(self.graph, start, end):

            #turn predecessors dict into list of shortest path 
            return(self.shortest_path(pred, start, end))   

        #has end node input but does not have path 
        else:
            return(None)



        




