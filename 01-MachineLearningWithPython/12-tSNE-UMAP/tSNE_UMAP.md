# t-SNE (t-distributed Stochastic Neighbor Embedding)

## Descriere generală
t-SNE este o tehnică **neliniară** de reducere a dimensionalității folosită în special pentru **vizualizarea datelor de înaltă dimensiune** în spații 2D sau 3D.  
Este foarte eficientă în păstrarea **structurilor locale** ale datelor (puncte apropiate în spațiul original rămân apropiate și în proiecția redusă).

---

## Cum funcționează (pe scurt)
1. Calculează **similarități** între puncte în spațiul original folosind o distribuție Gaussiană.
2. În spațiul țintă (2D/3D), creează o distribuție similară folosind o distribuție Student t.
3. Optimizează aranjarea punctelor astfel încât **diferențele între distribuții să fie minime** (folosind entropia Kullback–Leibler).

---

## Avantaje
- Excelent pentru vizualizarea **structurilor complexe**.
- Reprezintă clar **grupuri și separații** între clustere.
- Funcționează bine pentru date neliniare.

---

## Dezavantaje
- **Computațional costisitor** pentru seturi mari de date.
- Rezultatul poate varia între rulări (algoritm stocastic).
- Nu este ideal pentru seturi foarte mari fără eșantionare.

---

## Parametri cheie
- **n_components**: Dimensiunea spațiului țintă (de obicei 2 sau 3).
- **perplexity**: Influentează echilibrul între structura locală și cea globală (tipic 5–50).
- **learning_rate**: Pasul de învățare pentru optimizare.
- **n_iter**: Numărul de iterații (mai multe = rezultate mai stabile).

---

## Aplicații
- Vizualizarea clusterelor descoperite de algoritmi precum K-Means, DBSCAN.
- Analiza datelor în bioinformatică (gene, proteine).
- Reducerea dimensionalității pentru date de imagine, text sau audio.


# UMAP (Uniform Manifold Approximation and Projection)

## Descriere generală
UMAP este o tehnică **neliniară** de reducere a dimensionalității bazată pe concepte de **topologie și teoria grafurilor**.  
Este mai **rapidă** decât t-SNE și păstrează atât **structura locală**, cât și pe cea globală a datelor.

---

## Cum funcționează (pe scurt)
1. Construiește un **graf** al vecinilor apropiați în spațiul original.
2. Optimizează o reprezentare în spațiul redus astfel încât **distanțele relative** să fie păstrate.
3. Utilizează **metode topologice** pentru a păstra structura globală.

---

## Avantaje
- Mult mai **rapid** decât t-SNE, mai ales pe seturi mari de date.
- Păstrează atât structura locală, cât și globală.
- Permite **proiecții repetabile** (rezultatele sunt mai stabile).
- Scalabil la milioane de puncte.

---

## Dezavantaje
- Necesită reglarea atentă a parametrilor pentru rezultate optime.
- Poate pierde detalii fine pentru date foarte zgomotoase.

---

## Parametri cheie
- **n_neighbors**: Controlează câtă structură locală se păstrează (valori mici → mai multă structură locală, valori mari → mai multă structură globală).
- **min_dist**: Controlează distanța minimă între puncte în spațiul redus (valori mici → puncte mai compacte).
- **n_components**: Dimensiunea spațiului țintă (de obicei 2 sau 3).

---

## Aplicații
- Vizualizarea datelor de înaltă dimensiune.
- Preprocesare pentru clustering sau clasificare.
- Recunoaștere facială, analiză genomică, recomandări de conținut.
