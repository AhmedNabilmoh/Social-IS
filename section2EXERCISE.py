
#EXERCISE 1

li=[]
def get_leaves(g):
    for node in g.nodes:
        if g.degree(node)==1:
            li.append(node)
    return li            
#print(get_leaves(G))      

#EXERCISE 2
l=[]

def max_degree(g):
    ma=0
    n=''
    for node in g.nodes:
        if ma < g.degree(node):
            ma=g.degree(node)
            n=node
    l.append(('name',n))
    l.append(('degree',ma))
    return l            
#print(max_degree(G))

#EXERCISE 3
l=[]
def mutual_friends(G, node_1, node_2):
    n1=list(SG.neighbors(node_1))
    n2=list(SG.neighbors(node_2))
    for node1 in n1:
        for node2 in n2:
            if node1==node2:
                l.append(node1)
    return l
