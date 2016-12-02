class Graphx:

    def __init__(self):
        self.Adjacency = {}    

    def InsertVertex (self, x):
        self.Adjacency[x] = [] 

class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacent = []

    def Addadjacent(self, adjacent):
        if adjacent not in self.adjacent:
            self.adjacent.append(adjacent)
            self.adjacent.sort()

class Graphx(object):
    def __init__(self):  
        self.nodes = [] 
        
    def finder(self, value):
        for i in range(len(self.nodes)):
            if self.nodes[i].name == value:
                return i

    def AddEdge(self, addleft, addright): 
        if self.finder(addleft) == None:
            self.AddNode(Node(addleft))
        if self.finder(addright) == None:
            self.AddNode(Node(addright))
        dexleft = self.finder(addleft)
        dexright = self.finder(addright)
        self.nodes[dexleft].Addadjacent(addright)
        self.nodes[dexright].Addadjacent(addleft)


    def AddNode(self, node):
        self.nodes.append(node)

    def printGraph(self):
        for i in self.nodes:
            print(i.name, i.adjacent)

Graphx = Graphx()

Edges = ['AC', 'AB', 'BE', 'CF', 'CD', 'FI', 'DI', 'EH', 'HI', 'IG', 'JG', 'DB']

for i in Edges:
    Graphx.AddEdge(i[:1], i[1:])

Graphx.printGraph()
#no time for pseudo :/
