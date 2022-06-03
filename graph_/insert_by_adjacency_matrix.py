#appending a graph using adjacency matrix representaion

nodes=[]
graph=[]
count_nodes=0  

def insert_node(data):
    global count_nodes
    if data in nodes:
        print(data,'is allready in the graph!')
        
    else:
        nodes.append(data)
        count_nodes+=1
        for i in graph:
            i.append(0)
        temp=[0 for _ in range(count_nodes)]
        graph.append(temp)

def printgraph():
    for i in range(count_nodes):
        for j in range(count_nodes):
            print(graph[i][j],end=' ')
        print()

a=[1,3,2,5,4,7,6,2,9]
for _ in a:
    insert_node(_)    
printgraph() 
print(nodes)
