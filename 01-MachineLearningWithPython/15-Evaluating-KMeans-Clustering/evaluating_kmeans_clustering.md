# 🔍 Evaluarea modelelor de învățare nesupravegheată (Clustering)

Acest ghid rezumă conceptele esențiale pentru **evaluarea modelelor de clustering**, cu accent pe algoritmul **K-Means** și tehnici de analiză a calității clusterelor.

---

## 1) Ce este evaluarea clustering-ului?

- În **învățarea nesupravegheată** nu avem etichete reale pentru a compara rezultatele.  
- Evaluarea se face pe baza **calității structurii clusterelor**:  
  - cât de compacte sunt clusterele;  
  - cât de bine sunt separate între ele.  

---

## 2) Metrici principale de evaluare

### 🔹 Silhouette Score
- Măsoară **coerența internă** și **separarea externă** a clusterelor.  
- Variază între **-1 și 1**:
  - Aproape de **1** → clustere bine separate și compacte.  
  - Aproape de **0** → clustere care se suprapun.  
  - **<0** → probe atribuite greșit.  

### 🔹 Davies-Bouldin Index (DBI)
- Raport între **distanța dintre clustere** și **dimensiunea lor internă**.  
- **Mai mic** este mai bine → clusterele sunt compacte și bine separate.  

### 🔹 Inertia (Within-Cluster Sum of Squares – WCSS)
- Suma distanțelor pătrate între puncte și centrul clusterului.  
- Folosită în **Elbow Method** pentru alegerea lui *k*.  

---

## 3) Stabilitatea clustering-ului

- Deoarece K-Means depinde de **inițializarea centroidelor**, rulări diferite pot produce rezultate diferite.  
- Analiza stabilității presupune rularea algoritmului de mai multe ori și compararea rezultatelor (inertia, formele clusterelor).  

---

## 4) Alegerea numărului optim de clustere (k)

### 🔹 Elbow Method
- Se plotează **Inertia vs. k**.  
- Se caută „cotul” curbei unde scăderea se stabilizează.  

### 🔹 Silhouette Analysis
- Se plotează **Silhouette Score vs. k**.  
- Valoarea maximă indică un număr adecvat de clustere.  

### 🔹 Davies-Bouldin Index
- Se plotează **DBI vs. k**.  
- Căutăm minimul curbei pentru alegerea lui k.  

---

## 5) Limitările K-Means

- Funcționează bine doar pentru clustere **sferice și de dimensiuni similare**.  
- Sensibil la **outlieri** și **scalarea datelor**.  
- Nu detectează forme neregulate (ex: clustere alungite sau cu densități diferite).  
- Necesită alegerea manuală a lui **k** (numărul de clustere).  

---

## 6) Vizualizări utile

1. **Scatter plot** cu clustere și centroizi.  
2. **Silhouette plots** → vizualizarea distribuției coeficienților pentru fiecare cluster.  
3. **Voronoi diagrams** → arată regiunile de influență ale centroidelor.  

---

## 7) Pași practici pentru evaluarea clustering-ului

1. Rulează K-Means pentru mai multe valori de *k*.  
2. Calculează și compară:
   - Inertia (Elbow Method)  
   - Silhouette Score  
   - Davies-Bouldin Index  
3. Analizează **stabilitatea** rezultatelor prin rulări multiple.  
4. Interpretează vizual rezultatele prin scatter plots și silhouette plots.  
5. Verifică dacă **forma clusterelor** este potrivită pentru K-Means (altfel → DBSCAN, Agglomerative Clustering).  

---

## 8) Exemple de concluzii

- „Silhouette Score maxim la k=3 → alegem 3 clustere.”  
- „DBI minim la k=4 → sugerează că 4 clustere sunt mai bine separate.”  
- „Clusterele nu sunt sferice → K-Means nu e potrivit, recomand DBSCAN.”  

---

✅ **Ideea centrală**: evaluarea clustering-ului combină **metrici interne (Silhouette, DBI, Inertia)**, **analiza stabilității** și **vizualizări grafice** pentru a decide calitatea și numărul optim de clustere.
