# + Build graph
# + In-degree, out-degree, total degree
# + List edges

# Describe/print graph

from collections import deque

def search(start_node, target_node, graph):
    queue = deque([start_node])
    visited = []
    
    while queue:
        current_node = queue.popleft()
        neighbours = graph[current_node]
        for new_node in neighbours:
            if new_node not in visited:
                queue.append(new_node)
                visited.append(new_node)
    
    return visited
        

def build_graph(edges):
    graph = {
    }
    for start,end in edges:
        # if start not in graph:
        #     graph[start] = []
        # if end not in graph:
        #     graph[end] = []
        
        graph.setdefault(start,[])
        graph.setdefault(end,[])
            
        graph[start].append(end)

    return graph

def get_degree(graph,node_name):
    in_degree = _get_in_degree(graph,node_name)
    out_degree = _get_out_degree(graph, node_name)
    total_degree = in_degree + out_degree
    return total_degree, in_degree, out_degree

def _get_in_degree(graph,node_name):
    counter = 0
    for _,neighbours in graph.items():
        if node_name in neighbours:
            counter+=1
        
    return counter
    
def _get_out_degree(graph,node_name):
    return len(graph[node_name])

def get_edges(grap):
    edge_list = []
    for start_node, neighbours in grap.items():
        for target_node in neighbours:
            edge_list.append((start_node,target_node))
            
    return edge_list

if __name__ == "__main__":
    directed_edges = [
        ("A", "B"),
        ("A","C"),
        ("A","E"),
        ("B", "C"),
        ("C", "A"),
        ("C", "D"),
        ("D", "E")
    ]
    
    graph = build_graph(directed_edges)
    print("Grap Dict.",graph)
    
    selected_node_name = "C"
    t,i,o = get_degree(graph,selected_node_name)
    print("Selected : ",selected_node_name)
    print("Total Degree",t)
    print("In-Degree",i)
    print("Out-Degree",o)
    
    edges = get_edges(graph)
    print("Edges :")
    print(edges)

    
    