graph={}

def add_node(v):
    if v in graph:
        print(v,'is already in graph')
    else:
        graph[v]=[]

# this is also a way to print graph:

# def printgraph():
#     for i in graph:
#         print(i,graph[i],end=' ')

a=[2,3,4,5,6,7,8]
for _ in a:
    add_node(_)

# printgraph()

print(graph)