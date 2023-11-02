import pandas
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import gzip
import shutil


# Download data from : 
# https://xenabrowser.net/datapages/?dataset=TCGA-BRCA.htseq_fpkm-uq.tsv&host=https%3A%2F%2Fgdc.xenahubs.net
# The file is named: TCGA-BRCA.htseq_fpkm-uq.tsv.gz

# Unpack the .gz file:
with gzip.open('TCGA-BRCA.htseq_fpkm-uq.tsv.gz', 'rb') as f_in:
        with open('TCGA-BRCA.tsv', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


# Read the tsv file and convert to numpy:
data=pandas.read_csv('TCGA-BRCA.tsv',sep='\t')
npdata=data.to_numpy()
data_clean=npdata[1:,2:].astype('float')


# set the hyperparameters

# Calculate mean and variance of all genes

# Select 100 genes (two methods)

# Calculate the covariance matrix of the selcted genes and the precision matrix

# Initiate a graph
# You can read more about networkx here:
# https://networkx.org/

graph=nx.Graph()

# Add edges to the graph by your precision matrix
# Use command graph.add_edge():
# https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.add_edge.html

# draw your graph:
nx.draw(graph)
plt.show()

