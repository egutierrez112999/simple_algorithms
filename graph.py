

class Node:

    def __init__(self, val):
        self.next = None
        self.vertex = val

class Graph:

    def __init__(self, n):
        self.total_nodes = n
        self.nodes = [None]*n
        for i in range(n):
            node = Node(i)
            self.nodes[i] = node

    def addEdge(self, u, v):
        source = self.nodes[u]
        destination = self.nodes[v]
        u_node = Node(u)
        v_node = Node(v)

        #Add v to list of outgoing edges for u
        v_node.next = source.next
        source.next = v_node

        #Add u to list of outgoing edges for v
        u_node.next = destination.next
        destination.next = u_node

    def print_graph(self):
        for i in range(self.total_nodes):
            outgoing_edges = []
            current = self.nodes[i]
            while(current.next is not None):
                outgoing_edges.append(current.next.vertex)
                current = current.next
            print(f"Node {i}: {outgoing_edges}")



g = Graph(10)
g.addEdge(4, 6)
g.print_graph()