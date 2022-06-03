# adding a new node between v1 and v2 in the following ways:
# adding a edge between v1 and v2
# adding a weighted edge between v1 and v2
# aadding a weighted and directed edge between v1 and v2

from msilib import add_data

graph={}

def add_node(v):
    if v in graph:
        print(v,'is already in graph')
    else:
        graph[v]=[]

def add_edge(v1,v2):  #adding a edge between v1 and v2
    if v1 not in graph:
        print(v1,'is not present in the graph')
    elif v2 not in graph:
        print(v2,'is not present in the graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def add_edge1(v1,v2,cost):  #adding a weighted edge between v1 and v2
    if v1 not in graph:
        print(v1,'not in graph')
    elif v2 not in graph:
        print(v2,'is not present in the graph')
    
    list1=[v2,cost]
    list2=[v1,cost]

    graph[v1].append(list1)
    graph[v2].append(list2)


def add_edge2(v1,v2,cost): #aadding a weighted and directed edge between v1 and v2
    if v1 not in graph:
        print(v1,'not in graph')
    elif v2 not in graph:
        print(v2,'not in graph')
    else:
        list1=[v2,cost]
        graph[v1].append(list1)


a=[2,3,4,5,6,7,8]
for _ in a:
    add_node(_)
print(graph)
add_edge(2,3)
add_edge1(4,5,200)
add_edge2(7,8,100)
print(graph)
