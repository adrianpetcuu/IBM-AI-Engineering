# Fișă de sinteză: Modele de Învățare Nesupravegheată

## Modele comune de învățare nesupravegheată

| Model | Descriere | Avantaje (Pros) | Dezavantaje (Cons) | Aplicații comune | Hyperparametri cheie | Cod Python |
|---|---|---|---|---|---|---|
| **UMAP** (Uniform Manifold Approximation and Projection) | Folosit pentru reducerea dimensionalității, păstrează structura globală. | Performanță ridicată, păstrează structura globală. | Sensibil la parametri. | Vizualizare date, extragere de caracteristici. | - `n_neighbors`: dimensiunea vecinătății locale (default=15). <br> - `min_dist`: distanța minimă între puncte (default=0.1). <br> - `n_components`: dimensionalitatea embedding-ului (default=2). | ```python<br>from umap import UMAP<br><br>umap = UMAP(n_neighbors=15, min_dist=0.1, n_components=2)<br>``` |
| **t-SNE** (t-Distributed Stochastic Neighbor Embedding) | Tehnică neliniară de reducere a dimensionalității. | Bun pentru vizualizarea datelor de dimensiuni mari. | Costisitor computațional, predispus la overfitting. | Vizualizare date, detecție de anomalii. | - `n_components`: nr. dimensiuni output (default=2). <br> - `perplexity`: echilibru între aspecte locale și globale (default=30). <br> - `learning_rate`: pasul de învățare (default=200). | ```python<br>from sklearn.manifold import TSNE<br><br>tsne = TSNE(n_components=2, perplexity=30, learning_rate=200)<br>``` |
| **PCA** (Principal Component Analysis) | Reducere liniară a dimensionalității. | Ușor de interpretat, reduce zgomotul. | Metodă liniară, poate pierde informații în date neliniare. | Extragere de caracteristici, compresie. | - `n_components`: nr. de componente păstrate (default=2). <br> - `whiten`: scalează componentele (default=False). <br> - `svd_solver`: algoritmul folosit pentru decompoziție (default='auto'). | ```python<br>from sklearn.decomposition import PCA<br><br>pca = PCA(n_components=2)<br>``` |
| **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) | Algoritm de clustering bazat pe densitate. | Identifică outliers, nu necesită numărul de clustere. | Dificil de aplicat la densități variabile. | Detecție anomalii, clustering spațial. | - `eps`: distanța maximă între două puncte pentru a fi considerate vecine (default=0.5). <br> - `min_samples`: nr. minim de puncte pentru a forma un cluster (default=5). | ```python<br>from sklearn.cluster import DBSCAN<br><br>dbscan = DBSCAN(eps=0.5, min_samples=5)<br>``` |
| **HDBSCAN** (Hierarchical DBSCAN) | Extinde DBSCAN pentru a trata mai bine densitățile variabile. | Gestionează mai bine densitățile variabile. | Mai lent decât DBSCAN. | Seturi de date mari, clustering complex. | - `min_cluster_size`: dimensiunea minimă a clusterelor (default=5). <br> - `min_samples`: nr. minim de puncte pentru un cluster (default=10). | ```python<br>import hdbscan<br><br>clusterer = hdbscan.HDBSCAN(min_cluster_size=5)<br>``` |
| **K-Means Clustering** | Algoritm de clustering bazat pe centroid, împarte datele în k clustere. | Eficient, simplu de implementat. | Sensibil la alegerea inițială a centroizilor. | Segmentare clienți, recunoaștere tipare. | - `n_clusters`: numărul de clustere (default=8). <br> - `init`: metoda de inițializare a centroizilor (`k-means++`, `random`, default=`k-means++`). <br> - `n_init`: nr. de reporniri cu centroizi diferiți (default=10). | ```python<br>from sklearn.cluster import KMeans<br><br>kmeans = KMeans(n_clusters=3)<br>``` |

# Funcții asociate folosite (Clustering & Vizualizare)

| Metodă | Descriere | Cod Python |
|---|---|---|
| **make_blobs** | Generează bloburi gaussiene izotrope pentru clustering. | ```python<br>from sklearn.datasets import make_blobs<br>X, y = make_blobs(n_samples=100, centers=2, random_state=42)<br>``` |
| **multivariate_normal** | Generează eșantioane dintr-o distribuție normală multivariată. | ```python<br>from numpy.random import multivariate_normal<br>samples = multivariate_normal(mean=[0, 0], cov=[[1, 0], [0, 1]], size=100)<br>``` |
| **plotly.express.scatter_3d** | Creează un scatter 3D folosind Plotly Express. | ```python<br>import plotly.express as px<br>fig = px.scatter_3d(df, x='x', y='y', z='z')<br>fig.show()<br>``` |
| **geopandas.GeoDataFrame** | Creează un `GeoDataFrame` dintr-un `Pandas DataFrame`. | ```python<br>import geopandas as gpd<br>gdf = gpd.GeoDataFrame(df, geometry='geometry')<br>``` |
| **geopandas.to_crs** | Transformă sistemul de coordonate al unui `GeoDataFrame`. | ```python<br>gdf = gdf.to_crs(epsg=3857)<br>``` |
| **contextily.add_basemap** | Adaugă un basemap unui plot `GeoDataFrame` pentru context. | ```python<br>import contextily as ctx<br>ax = gdf.plot(figsize=(10, 10))<br>ctx.add_basemap(ax)<br>``` |
| **pca.explained_variance_ratio_** | Returnează proporția de varianță explicată de fiecare componentă principală. | ```python<br>from sklearn.decomposition import PCA<br>pca = PCA(n_components=2)<br>pca.fit(X)<br>variance_ratio = pca.explained_variance_ratio_<br>``` |


# Fișă de sinteză: Clustering și Reducerea Dimensionalității

- **Clustering** este o tehnică de învățare automată folosită pentru a grupa datele pe baza similarității.  
  🔹 Aplicații: segmentarea clienților, detectarea anomaliilor.

- **K-Means clustering** împarte datele în clustere pe baza distanței dintre puncte și centroizi.  
  ❌ Limitări: are dificultăți cu clustere dezechilibrate sau forme neconvexe.  
  🔹 Evaluare: se folosesc metode euristice precum *silhouette analysis*, *elbow method* și *Davies-Bouldin Index*.

- **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) creează clustere pe baza densității.  
  ✅ Funcționează bine pentru tipare naturale și neregulate.  

- **HDBSCAN** este o variantă a DBSCAN care nu necesită parametri stricți și folosește stabilitatea clusterelor pentru identificarea lor.  

- **Clustering ierarhic** poate fi:  
  - *Diviziv* (top-down)  
  - *Agregativ* (bottom-up)  
  ✅ Produce un **dendrogram** pentru vizualizarea ierarhiei clusterelor.

- **Reducerea dimensionalității** simplifică structura datelor și îmbunătățește rezultatele clustering-ului.  
  🔹 Aplicații: recunoașterea facială (ex. *eigenfaces*).  
  ✅ Ajută la reducerea zgomotului și la selecția caracteristicilor relevante.  

- **PCA** (Principal Component Analysis) este o metodă liniară de reducere a dimensionalității.  
  ✅ Minimiza pierderea de informație și zgomotul.

- **t-SNE** și **UMAP** sunt tehnici neliniare de reducere a dimensionalității.  
  ✅ Proiectează datele de înaltă dimensiune în spații cu dimensiuni reduse pentru **vizualizare și analiză**.
