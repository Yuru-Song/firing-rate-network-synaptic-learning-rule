import numpy as np 
import networkx as nx 
from scipy.io import loadmat
import matplotlib.pyplot as plt 
# plt.style.use('classic')
i1 = 1
i2 = 59
i3 = 99
evol_data_file = './1_unstable_learning_rule/net_properties.mat'
evol_data = loadmat(evol_data_file)
Creg = evol_data['Creg'][0,:]
Cran = evol_data['Cran'][0,:]
Lreg = evol_data['Lreg'][0,:]
Lran = evol_data['Lran'][0,:]
C = evol_data['C'][0,:]
L = evol_data['L'][0,:]

subcap_font = {
	'fontweight':'bold'
}
plt.figure(figsize = (12,2.5))


ax = plt.subplot(1,4,4)
plt.scatter(np.arange(i1,i3)*50,Lran[i1:i3]/L[i1:i3] - C[i1:i3]/Creg[i1:i3],s = 5, c = 'k')
plt.xlabel('time step',fontsize= 11)
plt.ylabel(r'$\omega$',fontsize= 11)
plt.xlim([i1*50,i3*50])

adj_data_file = 'adj_' + str(i1) + '.mat'
adj_data = loadmat(adj_data_file)
adj = adj_data['adj']
node = adj.shape
plt.title('(d)', fontdict = subcap_font)
ax = plt.subplot(1,4,1)
plt.imshow(adj,cmap=plt.cm.get_cmap('cubehelix', 2))
plt.xticks([0,int(node[1]/2),node[1]-1])
ax.set_xticklabels([1,int(node[1]/2)+1,node[1]])
plt.yticks([0,int(node[1]/2),node[1]-1])
ax.set_yticklabels([1,int(node[1]/2)+1,node[1]])
plt.colorbar(ticks = range(2))
plt.xlabel('#node')
plt.ylabel('#node')
plt.title('(a)', fontdict = subcap_font)
# nx.draw(nx.from_numpy_matrix(adj), node_size= 10, linewidths = .5, pos = nx.spring_layout(nx.from_numpy_matrix(adj)))

adj_data_file = 'adj_' + str(i2) + '.mat'
adj_data = loadmat(adj_data_file)
adj = adj_data['adj']
node = adj.shape
ax = plt.subplot(1,4,2)
plt.imshow(adj,cmap=plt.cm.get_cmap('cubehelix', 2))
plt.xticks([0,int(node[1]/2),node[1]-1])
ax.set_xticklabels([1,int(node[1]/2)+1,node[1]])
plt.yticks([0,int(node[1]/2),node[1]-1])
ax.set_yticklabels([1,int(node[1]/2)+1,node[1]])
plt.colorbar(ticks = range(2))
plt.xlabel('#node')
plt.ylabel('#node')
plt.title('(b)', fontdict = subcap_font)

adj_data_file = 'adj_' + str(i3) + '.mat'
adj_data = loadmat(adj_data_file)
adj = adj_data['adj']
node = adj.shape
ax = plt.subplot(1,4,3)
plt.imshow(adj,cmap=plt.cm.get_cmap('cubehelix', 2))
plt.xticks([0,int(node[1]/2),node[1]-1])
ax.set_xticklabels([1,int(node[1]/2)+1,node[1]])
plt.yticks([0,int(node[1]/2),node[1]-1])
ax.set_yticklabels([1,int(node[1]/2)+1,node[1]])
plt.colorbar(ticks = range(2))
plt.xlabel('#node')
plt.ylabel('#node')
plt.title('(c)', fontdict = subcap_font)
# nx.draw(nx.from_numpy_matrix(adj), node_size= 10, linewidths = .5, pos = nx.spring_layout(nx.from_numpy_matrix(adj)))
plt.tight_layout()
plt.savefig('fig_1.eps')
plt.show()