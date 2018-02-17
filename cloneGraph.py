# Definition for a undirected graph node
 class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

def cloneGraph(node):
    if not node:
        return node
    root = UnidirectedGraphNode(node.label)
    stack = [node]
    visit = {}
    visit[node.label] = root
    while stack:
        top = stack.pop()
        for n in top.neighbors:
            if n.label not in visit:
                stack.append(n)
                visit[n.label] = UndirectedGraphNode(n.label)
            visit[top.label].neighbors.append(visit[n.label])
    return root


# Definition for a undirected graph node
 class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

UndirectedGraphNode.__hash__ = lambda self: id(self)


class Solution:
    def __init__(self):
        self.visited = {}

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node not in self.visited:
            new_node = UndirectedGraphNode(node.label)
            self.visited[node] = new_node
            new_node.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        return self.visited[node]