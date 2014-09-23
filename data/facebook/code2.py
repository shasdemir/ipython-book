
import networkx as nx

g = nx.read_edgelist('0.edges')
sg = nx.connected_component_subgraphs(g)[0]

ecc = nx.eccentricity(sg)
r = nx.radius(sg)

center = [node for node in sg.nodes() if ecc[node] == r]

print center
