class Graph:
    def __init__(self,v):
       self.v=v
       self.adj=[[] for i in range (v)]
    def DFS(self,temp,v,visited):
       visited[v]=True
       temp.append(v)
       for i in self.adj[v]:
	       if visited[i]==False:
		       temp=self.DFS(temp,i,visited)
       return temp
    def addE(self,v,w):
	    self.adj[v].append(w)
	    self.adj[w].append(v)
    def connected(self):
	    visited=[]
	    c=[]
	    for i in range(self.v):
		    visited.append(False)
	    for v in range(self.v):
		    if visited[v]==False:
			    temp=[]
			    c.append(self.DFS(temp,v,visited))
	    return c
g=Graph(8)
g.addE(1,7)
g.addE(2,1)
g.addE(5,6)
g.addE(4,0)
c=g.connected()
print("these are the connected components")
print(c)
