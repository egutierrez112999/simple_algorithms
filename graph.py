

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

    def add_edge(self, u, v):
        source = self.nodes[u-1]
        destination = self.nodes[v-1]
        u_node = Node(u-1)
        v_node = Node(v-1)

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
                outgoing_edges.append(current.next.vertex+1)
                current = current.next
            print(f"Node {i+1}: {outgoing_edges}")

    def create_fig_3_1(self):
        self.total_nodes = 13
        self.nodes = [None]*13
        for i in range(13):
            node = Node(i)
            self.nodes[i] = node
        self.add_edge(1,2)
        self.add_edge(1,3)
        self.add_edge(1,4)
        self.add_edge(1,5)
        self.add_edge(1,6)
        self.add_edge(1,7)
        self.add_edge(1,9)
        self.add_edge(1,10)
        self.add_edge(1,11)
        self.add_edge(1,12)
        self.add_edge(2,3)
        self.add_edge(3,4)
        self.add_edge(4,5)
        self.add_edge(5,6)
        self.add_edge(6,7)
        self.add_edge(6,8)
        self.add_edge(7,8)
        self.add_edge(7,9)
        self.add_edge(7,13)
        self.add_edge(9,10)
        self.add_edge(9,11)
        self.add_edge(9,13)
        self.add_edge(10,11)
        self.add_edge(11,12)
        self.add_edge(11,13)


        


g = Graph(10)
g.create_fig_3_1()
g.print_graph()