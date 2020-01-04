import numpy as np 
import networkx as nx 
from scipy.io import loadmat
import matplotlib.pyplot as plt 
# plt.style.use('classic')
i1 = 1
i2 = 11
i3 = 16
subcap_font = {
	'fontweight':'bold'
}
plt.figure(figsize = (20,6))


adj_data_file = './jan-01/adj_' + str(i1) + '.mat'
adj_data = loadmat(adj_data_file)
adj = adj_data['adj']
node = adj.shape
plt.title('(d)', fontdict = subcap_font)
ax = plt.subplot(1,3,1)
nx.draw_networkx(nx.from_numpy_matrix(adj), node_size= 10, linewidths = .5, with_labels = False)
# plt.imshow(adj,cmap=plt.cm.get_cmap('cubehelix', 2))
# plt.xticks([0,int(node[1]/2),node[1]-1])
# ax.set_xticklabels([1,int(node[1]/2)+1,node[1]])
# plt.yticks([0,int(node[1]/2),node[1]-1])
# ax.set_yticklabels([1,int(node[1]/2)+1,node[1]])
# plt.colorbar(ticks = range(2))
# plt.xlabel('#node')
# plt.ylabel('#node')
plt.title('(a)', fontdict = subcap_font)
# nx.draw(nx.from_numpy_matrix(adj), node_size= 10, linewidths = .5, pos = nx.spring_layout(nx.from_numpy_matrix(adj)))

adj_data_file = './jan-01/adj_' + str(i2) + '.mat'
adj_data = loadmat(adj_data_file)
adj = adj_data['adj']
node = adj.shape
ax = plt.subplot(1,3,2)
nx.draw_networkx(nx.from_numpy_matrix(adj), node_size= 10, linewidths = .5, with_labels = False)
# plt.imshow(adj,cmap=plt.cm.get_cmap('cubehelix', 2))
# plt.xticks([0,int(node[1]/2),node[1]-1])
# ax.set_xticklabels([1,int(node[1]/2)+1,node[1]])
# plt.yticks([0,int(node[1]/2),node[1]-1])
# ax.set_yticklabels([1,int(node[1]/2)+1,node[1]])
# plt.colorbar(ticks = range(2))
# plt.xlabel('#node')
# plt.ylabel('#node')
plt.title('(b)', fontdict = subcap_font)

adj_data_file = './jan-01/adj_' + str(i3) + '.mat'
adj_data = loadmat(adj_data_file)
adj = adj_data['adj']
node = adj.shape
ax = plt.subplot(1,3,3)
nx.draw_networkx(nx.from_numpy_matrix(adj), node_size= 10, linewidths = .5, with_labels = False)
# plt.imshow(adj,cmap=plt.cm.get_cmap('cubehelix', 2))
# plt.xticks([0,int(node[1]/2),node[1]-1])
# ax.set_xticklabels([1,int(node[1]/2)+1,node[1]])
# plt.yticks([0,int(node[1]/2),node[1]-1])
# ax.set_yticklabels([1,int(node[1]/2)+1,node[1]])
# plt.colorbar(ticks = range(2))
# plt.xlabel('#node')
# plt.ylabel('#node')
plt.title('(c)', fontdict = subcap_font)
# nx.draw(nx.from_numpy_matrix(adj), node_size= 10, linewidths = .5, pos = nx.spring_layout(nx.from_numpy_matrix(adj)))
plt.tight_layout()
# plt.savefig('fig_2.eps')
plt.show()