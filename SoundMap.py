import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap.umap_ as umap

# Step 1: Load sample music feature data
# If you don't have real Spotify data, this simulates similar features
# Each row = one song, each column = one feature
import numpy as np
np.random.seed(42)
genres = ['Pop', 'Rock', 'Jazz', 'Hip-Hop', 'Classical']
n_samples = 500
data = pd.DataFrame({
    'genre': np.random.choice(genres, n_samples),
    'danceability': np.random.rand(n_samples),
    'energy': np.random.rand(n_samples),
    'loudness': np.random.rand(n_samples),
    'acousticness': np.random.rand(n_samples),
    'instrumentalness': np.random.rand(n_samples),
    'liveness': np.random.rand(n_samples),
    'valence': np.random.rand(n_samples),
    'tempo': np.random.rand(n_samples) * 200  # tempo in bpm
})

# Step 2: Standardize the features
features = ['danceability', 'energy', 'loudness', 'acousticness',
            'instrumentalness', 'liveness', 'valence', 'tempo']
X = data[features]
y = data['genre']  # for coloring the clusters

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Step 4: Apply t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

# Step 5: Apply UMAP
umap_model = umap.UMAP(n_components=2, random_state=42)
X_umap = umap_model.fit_transform(X_scaled)

# Step 6: Plot results
def plot_projection(X_proj, title, labels):
    df_proj = pd.DataFrame(X_proj, columns=['Dim1', 'Dim2'])
    df_proj['Genre'] = labels
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df_proj, x='Dim1', y='Dim2', hue='Genre', palette='Set2', s=60, edgecolor='k')
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

# Visualize all 3
plot_projection(X_pca, "PCA Projection of Songs", y)
plot_projection(X_tsne, "t-SNE Projection of Songs", y)
plot_projection(X_umap, "UMAP Projection of Songs", y)
