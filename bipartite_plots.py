import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

get_projection= nx.algorithms.bipartite.projection.overlap_weighted_projected_graph
node_redundancy= nx.algorithms.bipartite.redundancy.node_redundancy
closeness_centrality= nx.algorithms.bipartite.centrality.closeness_centrality
clustering= nx.algorithms.bipartite.cluster.clustering
get_matching= nx.algorithms.bipartite.matching.maximum_matching
edge_cover= nx.algorithms.bipartite.covering.min_edge_cover

PLOT_NAME = "Leaves"

def score_sort(nodes_list, scores_dict):
    """
    Returns the list of the nodes sorted by the score specified
    in the scores dict.

    If a node has no redundancy, then it is put at the
    begin of the list.
    """
    not_metirc_nodes= list(filter(lambda x : x not in scores_dict ,nodes_list))
    yes_metirc_nodes= list(filter(lambda x : x in scores_dict ,nodes_list))
    nodes_list= not_metirc_nodes + sorted(yes_metirc_nodes,
                                               key=lambda x: scores_dict[x])
    return nodes_list


def bipartite_layoult(B,up_nodes,down_nodes=None,up= 1,down= 0):
    """
    Returns the dictionary of positions.

    Inputs:
    B: Bipartite graph
    up_nodes: One partition of B
    down_nodes: The other partition of B

    """
    if(down_nodes==None):
        down_nodes= set(B.nodes).difference(up_nodes)

    n_up= len(up_nodes)-1
    n_down= len(down_nodes)-1
    alpha= 0.85
    l_top_nodes = list(up_nodes)
    top_deg = list(B.degree(l_top_nodes))
    top_deg = sorted(top_deg,key=lambda x: x[1])
    top_deg_2 = [i[0] for i in top_deg]
    l_down_nodes = list(down_nodes)
    down_deg = list(B.degree(l_down_nodes))
    down_deg = sorted(down_deg,key=lambda x: x[1])
    down_deg_2 = [i[0] for i in down_deg]
    down_deg_2 .reverse()
    pos= {node:(i*(1+2*alpha)/n_up - alpha, up) for i,node in enumerate(top_deg_2)}
    pos.update({node:(i/n_down, down) for i,node in enumerate(down_deg_2)})
    return pos

def plot_bipartite(B,
                   up_nodes,
                   down_nodes=None,
                   ax= None,
                   scores_dict= None,
                   color_by_score= False,
                   n_colors= None,
                   e_colors= None,
                   e_cmap= plt.cm.Reds,
                   n_cmap= plt.cm.Reds,
                   font_size= None,
                  ):

    if(down_nodes==None):
        down_nodes= set(B.nodes).difference(up_nodes)
    if(ax==None):
        _, ax = plt.subplots()
    if(scores_dict==None):
        not_metirc_nodes= []
    else:
        up_nodes= score_sort(up_nodes, scores_dict)
        down_nodes= score_sort(down_nodes, scores_dict)
        not_metirc_nodes= list(filter(lambda x : x not in scores_dict ,B.nodes))
    if(color_by_score):
        n_colors= [B.degree[n] for n in B]

    pos= bipartite_layoult(B,up_nodes,down_nodes)
    options = {
        "node_color": n_colors,
        "cmap": n_cmap,
        "edge_color": e_colors,
        "edge_cmap": e_cmap,
        "font_size": 10,
        "node_size":8,
    }

    nx.draw(B,pos,ax,**options)

    for node in not_metirc_nodes:
        x,y= pos[node]
        plt.plot(x,y,"o",color="purple")

    for selected_gene in up_nodes:
        x,y= pos[selected_gene]
        plt.text(x,y,selected_gene,
                 {'ha': 'left', 'va': 'bottom'},
                 rotation=90,
                 size= 5,
                )

    for selected_gene in down_nodes:
        x,y= pos[selected_gene]
        plt.text(x,y,selected_gene,
                 {'ha': 'left', 'va': 'top'},
                 rotation= -90,
                 size= 8,
                )
    print('Guardando')
    plt.savefig(f'{PLOT_NAME}.jpg',dpi=900)
    print('Guardado')



df = pd.read_csv('all_interaction_leaves.csv')
B = nx.Graph()
B.add_nodes_from(df['Gene2'], bipartite=0)
B.add_nodes_from(df['Gene1'], bipartite=1)
B.add_edges_from(
    [(row['Gene1'], row['Gene2']) for idx, row in df.iterrows()])
top_nodes = {n for n, d in B.nodes(data=True) if d["bipartite"] == 0}
bottom_nodes = set(B) - top_nodes

colors = {2: "hotpink",3: "tab:green",4: "gold",1: "tab:blue", 5: "black"}
edge_colors = [colors[B.degree[e[0]]] for e in B.edges]
plot_bipartite(B,top_nodes,bottom_nodes,e_colors=edge_colors)
