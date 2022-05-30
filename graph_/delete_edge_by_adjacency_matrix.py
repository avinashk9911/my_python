nodes=[]
graph=[]
count_nodes=0  

def insert_node(data): #to add some new nodes
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

def insert_edge(v1,v2):  #adding a new edge between two values: v1 and v2
    if v1 not in nodes:
        print(v1,'not in nodes')
    elif v2 not in nodes:
        print(v2,'not in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=1
        graph[index2][index1]=1

def insert_edge1(v1,v2,value): #add a new weighted node between v1 and v2
    if v1 not in nodes:
        print(v1,'not in nodes')
    elif v2 not in nodes:
        print(v2,'not in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=value
        graph[index2][index1]=value

def insert_edge2(v1,v2,value): #inserting edge only from v1 to v2 with a lode of 'value'
    if v1 not in nodes:
        print(v1,'not in nodes')
    elif v2 not in nodes:
        print(v2,'not in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=value

def printgraph():
    for i in range(count_nodes):
        for j in range(count_nodes):
            print(graph[i][j],end=' ')
        print()

def delete(v1,v2):
    if v1 not in nodes:
        print(v1,'not in nodes')
    elif v2 not in nodes:
        print(v2,'not in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0

def delete1(v1,v2): #for directed graph(direction from : v1 to v2)
    if v1 not in nodes:
        print(v1,'not in nodes')
    elif v2 not in nodes:
        print(v2,'not in nodes')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=0 

a=[1,3,2,5,4]
for _ in a:
    insert_node(_) 

insert_edge(1,2)
insert_edge1(5,4,100)
insert_edge2(3,2,200)
printgraph() 
print(nodes)

delete(1,2) #deleting a edge between 1 and 2 (unweighted or weighted : this will work for both)
delete1(3,2)#deleting a edge between 3,2 (this edge is having weight of 200)
printgraph()
print(nodes)