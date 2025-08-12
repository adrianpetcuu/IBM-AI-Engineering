# DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

## Descriere generală
DBSCAN este un algoritm de **clustering bazat pe densitate** folosit pentru a grupa puncte care sunt apropiate între ele (zone dense) și pentru a marca punctele izolate ca **zgomot (noise)**. Nu necesită specificarea numărului de clustere în avans.

---

## Cum funcționează
1. **Definirea vecinătății**  
   - Folosește o rază `eps` pentru a determina dacă două puncte sunt vecine.
   
2. **Clasificarea punctelor**  
   - **Core Points**: Puncte cu cel puțin `min_samples` vecini în raza `eps`.  
   - **Border Points**: Puncte aflate în vecinătatea unui punct core, dar cu mai puțini vecini decât `min_samples`.  
   - **Noise Points**: Puncte care nu aparțin niciunui cluster (izolate).

3. **Formarea clusterelor**  
   - Punctele core conectate între ele formează clustere.
   - Punctele border sunt atașate clusterelor vecine.
   - Punctele noise rămân neatribuite.

---

## Avantaje
- **Nu necesită k** (numărul de clustere) ca parametru.
- Detectează **forme neregulate** de clustere.
- Identifică **outliers** (zgomot) natural.

---

## Dezavantaje
- Performanța scade cu **variații mari de densitate**.
- Sensibil la alegerea parametrilor `eps` și `min_samples`.
- Mai puțin eficient în **date foarte mari și de înaltă dimensiune**.

---

## Parametri cheie
- **eps**: Distanța maximă pentru a considera două puncte vecine.  
- **min_samples**: Numărul minim de puncte necesare pentru ca un punct să fie considerat core.

---

## Aplicații
- Detectarea anomaliilor (ex. tranzacții suspecte).
- Clustering geospațial (ex. gruparea punctelor GPS).
- Identificarea zonelor dense în seturi de date științifice.
# HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise)

## Descriere generală
HDBSCAN este o extensie a DBSCAN care **gestionează mai bine densitățile variabile** și produce o ierarhie de clustere. Poate găsi clustere **mai stabile** fără a seta manual `eps`.

---

## Cum funcționează
1. **Construirea unui grafic de vecinătate ponderat**  
   - Creează o reprezentare a distanțelor dintre puncte.
   
2. **Formarea unei ierarhii de clustere**  
   - Clusterele se formează și se sparg în funcție de densitatea locală.

3. **Selecția finală a clusterelor**  
   - Se folosesc **măsuri de stabilitate** pentru a decide care clustere sunt păstrate.

---

## Avantaje
- Detectează clustere cu **densități diferite**.
- **Nu necesită parametru `eps`**.
- Produce rezultate mai stabile decât DBSCAN.
- Identifică zgomotul și outliers cu acuratețe ridicată.

---

## Dezavantaje
- Poate fi **mai lent** decât DBSCAN.
- Necesită înțelegerea unor parametri suplimentari.
- Rezultatele pot fi mai greu de interpretat pentru începători.

---

## Parametri cheie
- **min_cluster_size**: Dimensiunea minimă a unui cluster.
- **min_samples**: Controlează sensibilitatea la zgomot și outliers.

---

## Aplicații
- Analiza seturilor mari și complexe de date.
- Clustering în date cu densități variabile (ex. biologie, astronomie).
- Analize geospațiale complexe.

