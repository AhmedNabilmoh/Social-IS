#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[3]:


p = 0.70
for _ in range(10):
    r = random.random()
    if r < p:
        print('ahmed')
    else:
        print('nabil')


# In[4]:


names = ['ali', 'ahmed', 'tarek', 'amr']
random.choice(names)


# In[6]:


G = nx.cycle_graph(5)
random.sample(G.nodes, 2)


# In[8]:


names = ['ahmed', 'amr', 'ali']
tickets = [1, 3, 4]
for _ in range(10):
    print(random.choices(names, tickets))


# In[9]:


random.choices(names, tickets, k=10)


# In[10]:


elements = [0, 1, 2, 3, 4,5,6,7]
list(itertools.combinations(elements, 2))


# In[11]:


G = nx.Graph()
G.add_nodes_from(elements)
list(itertools.combinations(G.nodes, 2))


# In[12]:




def gnp_random_graph(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for i, j in itertools.combinations(G.nodes, 2):
        r = random.random()
        if r < p:
            G.add_edge(i, j)
    return G


# In[13]:


G = gnp_random_graph(16, 0.15)
nx.draw(G)
print('Graph has', G.number_of_edges(), 'edges.')


# In[14]:


def gnm_random_graph(N, M):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    possible_edges = itertools.combinations(G.nodes, 2)
    edges_to_add = random.sample(list(possible_edges), M)
    G.add_edges_from(edges_to_add)
    
    return G


# In[15]:


G = gnm_random_graph(16, 18)
nx.draw(G)


# In[17]:


N = 30
G = nx.cycle_graph(N)
nx.draw_circular(G, with_labels=True)


# In[18]:


k = 4
for n in G.nodes:
    for i in range(1, k // 2 + 1):
        left  = (n-i) % N
        right = (n+i) % N 
        G.add_edge(n, left)
        G.add_edge(n, right)

nx.draw_circular(G, with_labels=True)


# In[20]:


p = 0.2
for u, v in list(G.edges):
    if random.random() < p:
        not_neighbors = set(G.nodes) - set(G.neighbors(u))
        w = random.choice(list(not_neighbors))
        G.remove_edge(u, v)
        G.add_edge(u, w)

nx.draw_circular(G, with_labels=True)


# In[21]:


def watts_strogatz_graph(N, k, p):
    G = nx.cycle_graph(N)
    for n in G.nodes:
        for i in range(1, k // 2 + 1):
            left  = (n-i) % N
            right = (n+i) % N 
            G.add_edge(n, left)
            G.add_edge(n, right)
    for u, v in list(G.edges):
        if random.random() < p:
            not_neighbors = set(G.nodes) - set(G.neighbors(u)) - {u}
            w = random.choice(list(not_neighbors))
            G.remove_edge(u, v)
            G.add_edge(u, w)

    return G


# In[22]:


G = watts_strogatz_graph(16, 4, 0.2)
nx.draw_circular(G, with_labels=True)


# In[24]:


G = nx.star_graph(7)
degrees = [G.degree(n) for n in G.nodes]

print(degrees)
nx.draw(G, with_labels=True)


# In[25]:


def barabasi_albert_graph(N, m):
    G = nx.complete_graph(m + 1)
    for i in range(G.number_of_nodes(), N):
        new_neighbors = []
        possible_neighbors = list(G.nodes)
        for _ in range(m):
            degrees = [G.degree(n) for n in possible_neighbors]
            j = random.choices(possible_neighbors, degrees)[0]
            new_neighbors.append(j)
            possible_neighbors.remove(j)
        for j in new_neighbors:
            G.add_edge(i, j)

    return G


# In[26]:


G = barabasi_albert_graph(20, 1)
nx.draw(G)


# In[ ]:




