class Node:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}"

class Edge:
    def __init__(self, value, node2, node1):
        self.node1 = node1
        self.node2 = node2
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value} entre {self.node1} et {self.node2}"


class Graph:
    def __init__(self, nodeList, edgeList):
        self.nodeList  = nodeList
        self.edgeList = edgeList

    def getAdjacent(self, node):
        return [e.node2 for e in self.edgeList if e.node1 == node] + [e.node1 for e in self.edgeList if e.node2 == node]

    def isCyclic(self):
        for node in self.nodeList:
            visited = {n: False for n in self.nodeList}
            if self.checkCyclic(node, None, visited):
                return True
            return False

    def checkCyclic(self,node,parent,visited):
        # Mark the current node as visited
        visited[node]= True
        for i in self.getAdjacent(node):
            if  visited[i]==False :
                if(self.checkCyclic(i,node,visited)):
                    return True
            elif  parent!=i:
                return True
        return False

    def Kruskall(self):
        sortedEdgeList = sorted(self.edgeList.copy(),key=lambda x: x.value)
        tree = Graph(self.nodeList, [sortedEdgeList.pop(0)])
        i = 0
        while len(tree.edgeList) != len(tree.nodeList)-1:
            tree.edgeList.append(sortedEdgeList[i])
            if tree.isCyclic():
                tree.edgeList.remove(sortedEdgeList[i])
            i+=1
        return tree

    def __repr__(self) -> str:
        return str(self.edgeList)

lille = Node('Lille')
strasbourg = Node('Strasbourg')
paris = Node('Paris')
brest = Node('Brest')
bordeaux = Node('Bordeaux')
nice = Node('Nice')
perpignan = Node('Perpignan')

nodes = [lille, strasbourg, paris, brest, bordeaux, nice, perpignan]

lille_strasbourg = Edge(522,lille,strasbourg)
strasbourg_nice = Edge(804, strasbourg, nice)
nice_perpignan = Edge(476, nice, perpignan)
perpignan_bordeaux = Edge(451, perpignan, bordeaux)
bordeaux_brest = Edge(623, bordeaux, brest)
brest_lille = Edge(725, brest, lille)
paris_lille = Edge(222 ,paris, lille)
paris_strasbourg = Edge(490, paris, strasbourg)
paris_nice = Edge(932, paris, nice)
paris_perpignan = Edge(857, paris, perpignan)
paris_bordeaux = Edge(583, paris, bordeaux)
paris_brest = Edge(596, paris, brest)

edges = [lille_strasbourg, strasbourg_nice, nice_perpignan, perpignan_bordeaux, bordeaux_brest, brest_lille, paris_lille, paris_strasbourg, paris_nice, paris_perpignan, paris_bordeaux, paris_brest]


g = Graph(nodes, edges)
print(g.Kruskall())


