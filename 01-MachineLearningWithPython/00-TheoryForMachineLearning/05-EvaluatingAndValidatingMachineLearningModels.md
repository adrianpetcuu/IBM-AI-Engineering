# Fișă de sinteză: Evaluarea și Validarea Modelelor ML

## Metrici și metode de evaluare

| Metodă | Descriere | Cod Python |
|--------|-----------|------------|
| **classification_report** | Generează un raport cu precizie, recall, F1-score și suport pentru fiecare clasă. Util pentru evaluarea modelelor de clasificare. <br> **Hyperparametri:** `target_names` (lista de clase). <br> ✅ **Avantaj:** Oferă o evaluare completă. <br> ❌ **Limitare:** Nu este suficient pentru seturi dezechilibrate. | ```python<br>from sklearn.metrics import classification_report<br><br>report = classification_report(y_true, y_pred, target_names=["class1", "class2"])<br>``` |
| **confusion_matrix** | Creează o matrice de confuzie pentru evaluarea performanței de clasificare (TP, FP, TN, FN). <br> **Hyperparametri:** `labels` (lista de clase). <br> ✅ **Avantaj:** Esențială pentru a înțelege erorile. <br> ❌ **Limitare:** Nu oferă informații despre probabilități. | ```python<br>from sklearn.metrics import confusion_matrix<br><br>conf_matrix = confusion_matrix(y_true, y_pred)<br>``` |
| **mean_squared_error (MSE)** | Calculează eroarea pătratică medie, metrică comună în regresie. Valori mici → performanță mai bună. <br> **Hyperparametri:** `sample_weight`. <br> ✅ **Avantaj:** Simplu și folosit pe scară largă. <br> ❌ **Limitare:** Sensibil la outlieri (erorile mari sunt pătrate). | ```python<br>from sklearn.metrics import mean_squared_error<br><br>mse = mean_squared_error(y_true, y_pred)<br>``` |
| **root_mean_squared_error (RMSE)** | Rădăcina pătrată din MSE, mai interpretabilă pentru că are aceleași unități ca ținta. <br> **Hyperparametri:** `sample_weight`. <br> ✅ **Avantaj:** Mai intuitiv decât MSE. <br> ❌ **Limitare:** Sensibil la erori mari/outlieri. | ```python<br>from sklearn.metrics import root_mean_squared_error<br><br>rmse = root_mean_squared_error(y_true, y_pred)<br>``` |
| **mean_absolute_error (MAE)** | Măsoară magnitudinea medie a erorilor, ignorând direcția. <br> **Hyperparametri:** `sample_weight`. <br> ✅ **Avantaj:** Mai robust la outlieri decât MSE. <br> ❌ **Limitare:** Nu penalizează la fel de mult erorile mari precum MSE/RMSE. | ```python<br>from sklearn.metrics import mean_absolute_error<br><br>mae = mean_absolute_error(y_true, y_pred)<br>``` |
| **r2_score** | Calculează coeficientul de determinare (R²), proporția varianței explicată de model. Valori mai mari → potrivire mai bună. <br> ✅ **Avantaj:** Indicator clar al performanței. <br> ❌ **Limitare:** Poate fi înșelător pentru modele neliniare. | ```python<br>from sklearn.metrics import r2_score<br><br>r2 = r2_score(y_true, y_pred)<br>``` |
| **silhouette_score** | Măsoară calitatea clusteringului prin coeziunea intra-cluster și separarea inter-cluster. <br> **Hyperparametri:** `metric` (ex. `euclidean`). <br> ✅ **Avantaj:** Bun pentru validarea clusteringului. <br> ❌ **Limitare:** Sensibil la outlieri și la alegerea metricii. | ```python<br>from sklearn.metrics import silhouette_score<br><br>score = silhouette_score(X, labels, metric='euclidean')<br>``` |
| **silhouette_samples** | Returnează scoruri de siluetă pentru fiecare eșantion, arătând cât de bine se potrivește clusterului său. <br> ✅ **Avantaj:** Oferă detalii granular despre calitatea fiecărui eșantion. <br> ❌ **Limitare:** Aceleași sensibilități ca `silhouette_score`. | ```python<br>from sklearn.metrics import silhouette_samples<br><br>samples = silhouette_samples(X, labels, metric='euclidean')<br>``` |
| **davies_bouldin_score** | Măsoară asemănarea medie între fiecare cluster și cel mai apropiat cluster. Valori mai mici → clustering mai bun. <br> ✅ **Avantaj:** Simplu, eficient pentru evaluarea clusterelor. <br> ❌ **Limitare:** Poate să nu fie robust pentru clustere dezechilibrate. | ```python<br>from sklearn.metrics import davies_bouldin_score<br><br>db_score = davies_bouldin_score(X, labels)<br>``` |
| **Voronoi** | Calculează diagrama Voronoi, care împarte spațiul pe baza celui mai apropiat vecin. <br> ✅ **Avantaj:** Util pentru analiză spațială și clustering. <br> ❌ **Limitare:** Se aplică doar cazurilor spațiale. | ```python<br>from scipy.spatial import Voronoi<br><br>vor = Voronoi(points)<br>``` |
| **voronoi_plot_2d** | Plotează diagrama Voronoi în 2D pentru vizualizare. <br> **Hyperparametri:** `show_vertices` (afișează vârfurile). <br> ✅ **Avantaj:** Bun pentru vizualizarea clusteringului spațial. <br> ❌ **Limitare:** Limitat la 2D și seturi mari de date pot cauza probleme de performanță. | ```python<br>from scipy.spatial import voronoi_plot_2d<br><br>voronoi_plot_2d(vor, show_vertices=True)<br>``` |
| **matplotlib.patches.Patch** | Creează forme personalizate (dreptunghiuri, cercuri, elipse) pentru grafice. <br> **Hyperparametri:** `color` (culoarea formei). <br> ✅ **Avantaj:** Versatil pentru personalizare vizuală. <br> ❌ **Limitare:** Nu suportă toate formele/complexitățile. | ```python<br>import matplotlib.patches as patches<br><br>rectangle = patches.Rectangle((0, 0), 1, 1, color='blue')<br>``` |
| **explained_variance_score** | Măsoară proporția varianței explicată de predicțiile modelului. Scor mai mare → performanță mai bună. <br> ✅ **Avantaj:** Bun pentru regresie. <br> ❌ **Limitare:** Nu se aplică pentru clasificare. | ```python<br>from sklearn.metrics import explained_variance_score<br><br>ev_score = explained_variance_score(y_true, y_pred)<br>``` |
| **Ridge Regression** | Regresie cu regularizare L2 → penalizează coeficienții mari pentru a reduce overfitting-ul. <br> **Hyperparametri:** `alpha` (forța regularizării). <br> ✅ **Avantaj:** Reduce overfitting-ul. <br> ❌ **Limitare:** Mai slab pentru date rare (sparse). | ```python<br>from sklearn.linear_model import Ridge<br><br>ridge = Ridge(alpha=1.0)<br>``` |
| **Lasso Regression** | Regresie cu regularizare L1 → penalizează coeficienții și promovează soluții sparse (feature selection). <br> **Hyperparametri:** `alpha`. <br> ✅ **Avantaj:** Selectează automat variabile importante. <br> ❌ **Limitare:** Probleme cu multicoliniaritatea. | ```python<br>from sklearn.linear_model import Lasso<br><br>lasso = Lasso(alpha=0.1)<br>``` |
| **Pipeline** | Conectează mai mulți pași de preprocesare și modelare într-un singur obiect → workflow eficient. <br> ✅ **Avantaj:** Simplifică codul, reproducibil. <br> ❌ **Limitare:** Mai greu pentru configurații dinamice. | ```python<br>from sklearn.pipeline import Pipeline<br>from sklearn.preprocessing import StandardScaler<br><br>pipeline = Pipeline(steps=[('scaler', StandardScaler()), ('model', Ridge(alpha=1.0))])<br>``` |
| **GridSearchCV** | Caută exhausiv parametri optimi pe o grilă definită de utilizator. <br> **Hyperparametri:** `param_grid`. <br> ✅ **Avantaj:** Asigură cei mai buni parametri. <br> ❌ **Limitare:** Costisitor computațional pe grile mari. | ```python<br>from sklearn.model_selection import GridSearchCV<br><br>grid_search = GridSearchCV(estimator=Ridge(), param_grid={'alpha': [0.1, 1.0, 10.0]})<br>``` |

# Strategii de vizualizare pentru evaluarea K-Means

## Rulări multiple ale K-Means
- **Descriere**: Rulează algoritmul KMeans de mai multe ori cu inițializări aleatoare diferite pentru a evalua variabilitatea asignării clusterelor.  
- **Avantaj**: Ajută la vizualizarea consistenței.  
- **Limitare**: Costisitor computațional pentru seturi mari de date.  

---

## Metoda "Elbow"
- **Descriere**: Evaluează numărul optim de clustere prin reprezentarea inerției (suma pătratelor intra-cluster) pentru valori diferite ale lui k.  
- **Avantaj**: Ușor de interpretat.  
- **Limitare**: Punctul de „cot” este subiectiv.  

---

## Metoda Silhouette
- **Descriere**: Determină numărul optim de clustere prin calcularea scorurilor Silhouette pentru diferite valori ale lui k.  
- **Avantaj**: Ia în considerare atât coeziunea, cât și separarea.  
- **Limitare**: Necesită multă putere de calcul pentru seturi mari de date.  

---

## Indexul Davies-Bouldin
- **Descriere**: Evaluează performanța clusterizării prin calculul DBI pentru diferite valori ale lui k.  
- **Avantaj**: Măsoară compactitatea și separarea.  
- **Limitare**: Sensibil la formele și densitatea clusterelor.  


# Evaluarea și Validarea Modelelor de Învățare Automată

## Învățare supervizată
- Evaluarea modelelor supervizate măsoară capacitatea unui model de a prezice rezultate pentru date nevăzute.  
- De obicei se folosește o împărțire **train/test** pentru a estima performanța.

### Metrici pentru clasificare
- **Acuratețe (Accuracy)**
- **Matrice de confuzie (Confusion Matrix)**
- **Precizie (Precision)**
- **Recall (Sensibilitate)**
- **F1-Score** – echilibrează precizia și recall-ul.

### Metrici pentru regresie
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**
- **R² (R-squared)**
- **Varianță explicată (Explained Variance)**

---

## Învățare nesupervizată
- Evaluarea modelelor nesupervizate se face prin calitatea și consistența tiparelor descoperite.  

### Metrici utilizate
- **Silhouette Score**  
- **Indicele Davies-Bouldin**  
- **Adjusted Rand Index**

---

## Reducerea dimensionalității
- Evaluată prin:
  - **Raportul varianței explicate (Explained Variance Ratio)**
  - **Eroarea de reconstrucție (Reconstruction Error)**
  - **Păstrarea vecinătăților (Neighborhood Preservation)**

---

## Validarea modelelor
- Împărțirea datelor în **train/validation/test** previne **overfitting-ul**.  
- Reglarea hiperparametrilor trebuie făcută cu atenție.  

### Metode de validare
- **Cross-validation (CV)**
- **K-fold CV**
- **Stratified CV** – mai robust pentru clase dezechilibrate.  

---

## Regularizare
- Ajută la prevenirea **overfitting-ului**.  
- **Ridge Regression (L2)** – penalizează coeficienții mari.  
- **Lasso Regression (L1)** – încurajează selecția de variabile (sparse solutions).  

---

## Probleme frecvente
- **Scurgerea de date (Data Leakage):** apare când setul de antrenare conține informații care nu ar fi disponibile în scenarii reale.  
  → Se previne prin separarea corectă a datelor și selecția atentă a caracteristicilor.  

- **Capcane în modelare:**
  - Interpretarea greșită a importanței caracteristicilor.  
  - Ignorarea dezechilibrului de clasă.  
  - Dependința excesivă de procese automate fără analiză cauzală.  

- **Evaluarea importanței caracteristicilor** trebuie să țină cont de:
  - Redundanță  
  - Sensibilitatea la scară  
  - Evitarea presupunerilor incorecte despre cauzalitate  

---
