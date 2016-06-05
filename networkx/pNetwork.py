#!/bin/python
import networkx as nx
import matplotlib.pyplot as plt
from math import sqrt
import getopt
import os
import sys
import json

def main():
    opts,args=getopt.getopt(sys.argv[1:],"p:")
    fPath=opts[0][1]
    filename=os.path.basename(fPath)
    fDir=os.path.dirname(fPath)
    sDir=os.path.join(fDir,filename+".fig")
    if not os.path.exists(sDir):
        os.mkdir(sDir)
    with open(fPath,'rb') as fh:
        G_analysis=nx.read_edgelist(fh)
    num_nodes=nx.number_of_nodes(G_analysis)

    G_nodes=G_analysis.nodes()
    G_edges=G_analysis.edges()
    num_bins=int(sqrt(num_nodes))

## degree distribution
    G_degree=G_analysis.degree(G_nodes).values()
    plt.hist(G_degree,bins=num_bins,normed=True)
    plt.xlabel("node degrees")
    plt.ylabel("number of nodes")
    plt.title('Histogram of degree distribution')
    #plt.xlim([0,10*int(max(G_degree)/10)])
    plt.grid(True)

    plt.savefig(os.path.join(sDir,"degreeDistribution.jpg"))
    #plt.show()

## clustering coefficient

    plt.figure()
    clusterCoef=nx.clustering(G_analysis)
    plt.hist(clusterCoef.values(),bins=num_bins,normed=True)
    plt.xlabel("clustering coefficient")
    plt.ylabel("number of nodes")
    plt.title('Histogram of clustering coefficient distribution')
    plt.grid(True)
    plt.savefig(os.path.join(sDir,"clusteringCoefficientDistribution.jpg"))
    #plt.show()

## components and sizes
    components=nx.connected_components(G_analysis)
    comp_size=list()

    for comp in components:
        comp_size.append(len(comp))
    Dict_comp={nx.number_connected_components(G_analysis):comp_size}
    str_comp=json.dumps(Dict_comp)
    with open(os.path.join(sDir,"components.json"),'w') as fh:
        fh.write(str_comp)

## closeness

    closeness=nx.closeness_centrality(G_analysis)
    plt.figure()
    plt.hist(closeness.values(),bins=num_bins,normed=True)
    plt.xlabel("closeness coefficient")
    plt.ylabel("number of nodes")
    plt.title('Histogram of closeness coefficient distribution')
    plt.grid(True)
    plt.savefig(os.path.join(sDir,"closenessDistribution.jpg"))
    #plt.show()

## betweenness
    betweenness=nx.betweenness_centrality(G_analysis)
    plt.figure()
    plt.hist(betweenness.values(),bins=num_bins,normed=True)
    plt.xlabel("betweenness coefficient")
    plt.ylabel("number of nodes")
    plt.title('Histogram of betweenness coefficient distribution')
    plt.grid(True)
    plt.savefig(os.path.join(sDir,"betweennessDistribution.jpg"))
    #plt.show()


if __name__=="__main__":
    main()
