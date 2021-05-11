import networkx as nx
import matplotlib.pyplot as plt

data=open("E:\\Academics\\VIT\\Project\SIN\\roadNet.csv","r")
Graphtype=nx.Graph()

G=nx.parse_edgelist(data,delimiter=',',create_using=Graphtype,nodetype=int,data=(('weight',float),))