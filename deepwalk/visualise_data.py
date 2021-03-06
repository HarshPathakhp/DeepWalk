import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.decomposition import PCA
    
matplotlib.rcParams.update({'font.size': 5})
f = open("embeddings.pkl", "rb")
mat_new,mat_old = pickle.load(f)

def draw(mat, path):
    colors = ['red','red','green','red','blue','blue','blue','red','purple','green','blue','red','red','red','purple','purple','blue','red','purple','red','purple','red','purple','purple','green','green','purple','green','green','purple','purple','green','purple','purple']
    text = [i for i in range(1,mat.shape[0]+1)]
    fig, ax = plt.subplots()
    ax.scatter(mat[:,0], mat[:,1], c = colors)
    for i, txt in enumerate(text):
        ax.annotate(txt, (mat[:,0][i], mat[:,1][i]))
    plt.savefig(path)
    plt.close()

def transform(mat, n_comp = 2):
    pca = PCA(n_components=2)
    mat = pca.fit_transform(mat)
    print(sum(pca.explained_variance_ratio_))
    return mat

def read_graph(pkl_file):
    f = open(pkl_file, "rb")
    g = pickle.load(f)
    print(g[0])
    print(g[1])
    f.close()
    print(len(g[1]))
##mat_old = transform(mat_old)
#mat_new = transform(mat_new)
draw(mat_old, "init_embeds.pdf")
draw(mat_new, "final_embeds.pdf")
#print(mat_new.shape)
#read_graph("./graph.pkl")
    