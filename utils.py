import seaborn as sns
import matplotlib as plt


def plot_facet(name: str, X, cluster_predictions):
    temp = X.copy().reset_index(drop=True)
    temp[f"{name}_cluster"] = cluster_predictions
    temp = temp.melt(id_vars=f"{name}_cluster")
    
    means = temp.groupby([f"{name}_cluster", "variable"]).mean().reset_index()
    
    g = sns.FacetGrid(means, col="variable", hue=f"{name}_cluster", col_wrap=5, height=2, sharey=False)
    g = g.map(plt.bar, f"{name}_cluster", "value").set_titles("{col_name}")
    g.savefig(f"outputs/{name}_facetgrid.png")
    plt.clf()
    
    return
