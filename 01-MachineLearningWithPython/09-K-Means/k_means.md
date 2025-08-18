# K-Means Clustering

## Descriere generală
K-Means este un algoritm de **învățare nesupervizată** folosit pentru a grupa datele în **k clustere** pe baza similarității dintre ele. Algoritmul atribuie fiecare punct de date celui mai apropiat **centroid** (centrul clusterului), apoi recalculă pozițiile centroidelor până la convergență.

---

## Cum funcționează K-Means

1. **Alegerea numărului de clustere (k)**  
   - Utilizatorul specifică din start valoarea lui **k**.
   
2. **Inițializarea centroidelor**  
   - Centroidele pot fi alese aleator sau cu metode speciale (ex. *k-means++* pentru o distribuție mai bună).

3. **Atribuirea punctelor**  
   - Fiecare punct de date este atribuit celui mai apropiat centroid folosind, de obicei, **distanța Euclidiană**.

4. **Recalcularea centroidelor**  
   - Se calculează media tuturor punctelor din fiecare cluster, rezultând noile poziții ale centroidelor.

5. **Iterare până la convergență**  
   - Procesul de atribuire și recalculare se repetă până când centroidele nu se mai schimbă semnificativ sau se atinge numărul maxim de iterații.

---

## Avantaje
- **Simplicitate**: Ușor de implementat și rapid de rulat.
- **Scalabilitate**: Poate lucra eficient cu seturi de date mari.
- **Interpretabilitate**: Rezultatele sunt intuitive și ușor de vizualizat (pentru 2D și 3D).

---

## Dezavantaje
- **Necesită specificarea lui k** dinainte.
- **Sensibil la valori extreme (outliers)**.
- **Nu funcționează bine cu clustere ne-convexe** sau cu dimensiuni/densități foarte diferite.
- **Sensibil la inițializarea centroidelor** (rezultatele pot varia).

---

## Alegerea numărului optim de clustere (k)
Metode populare:
- **Metoda cotului (Elbow Method)** – analizează variația intra-cluster în funcție de k.
- **Scorul siluetei (Silhouette Score)** – măsoară cât de bine este separat fiecare cluster.
- **Indicele Davies–Bouldin** – mai mic înseamnă clustere mai bine definite.

---

## Parametri importanți (scikit-learn)
- **n_clusters** *(default=8)* – numărul de clustere.
- **init** *(‘k-means++’ sau ‘random’)* – metoda de inițializare a centroidelor.
- **n_init** *(default=10)* – de câte ori se rulează algoritmul cu inițializări diferite și se alege cel mai bun rezultat.
- **max_iter** *(default=300)* – numărul maxim de iterații.
- **random_state** – pentru rezultate reproductibile.

---

## Exemple de utilizare
- Segmentarea clienților în marketing.
- Gruparea documentelor pe subiecte.
- Compresia imaginilor.
- Detectarea tiparelor în seturi mari de date.

---

## Cod exemplu (Python - scikit-learn)
```python
from sklearn.cluster import KMeans
import numpy as np

# Generăm date de exemplu
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Inițializăm modelul K-Means
kmeans = KMeans(n_clusters=2, random_state=0)

# Antrenăm modelul
kmeans.fit(X)

# Obținem etichetele clusterelor
print(kmeans.labels_)

# Obținem coordonatele centroidelor
print(kmeans.cluster_centers_)
```