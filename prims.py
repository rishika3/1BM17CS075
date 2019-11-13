import sys 
  
class Graph():
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    
    def printMST(self, p): 
        print ("Edge\tWeight")
        for i in range(1, self.V): 
            print (p[i], "-", i, "\t", self.graph[i][ p[i] ] )

    def minKey(self, key, mstSet): 
        min = sys.maxsize
        min_index = v 
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                
  
        return min_index 
    def primMST(self): 
 
        key = [sys.maxsize] * self.V 
        p= [None] * self.V

        key[0] = 0 
        mstSet = [False] * self.V 
  
        p[0] = -1 
  
        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                    key[v] = self.graph[u][v] 
                    p[v] = u 
  
        self.printMST(p) 
  
g = Graph(5) 
g.Graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
g.primMST() 
