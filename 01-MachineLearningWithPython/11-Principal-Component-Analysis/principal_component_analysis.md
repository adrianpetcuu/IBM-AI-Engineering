# PCA (Principal Component Analysis) – Analiza Componentelor Principale

## Descriere generală
PCA este o tehnică de **reducere a dimensionalității** liniară folosită pentru a transforma un set de date cu multe variabile într-un set de **componente principale** care păstrează cât mai mult din variația originală a datelor.  
Scopul său este să **simplifice datele** reducând zgomotul și corelațiile dintre variabile, păstrând în același timp informațiile esențiale.

---

## Cum funcționează
1. **Standardizarea datelor**  
   - Variabilele sunt scalate pentru a avea aceeași unitate de măsură.

2. **Calcularea matricei de covarianță**  
   - Măsoară cum variază variabilele împreună.

3. **Calculul valorilor proprii și vectorilor proprii**  
   - Vectorii proprii reprezintă direcțiile noilor axe (componente principale).
   - Valorile proprii indică importanța fiecărei componente.

4. **Selectarea componentelor principale**  
   - Se aleg primele `n` componente care păstrează cea mai mare parte a varianței.

5. **Transformarea datelor**  
   - Datele originale sunt proiectate pe noile axe (componentele principale).

---

## Avantaje
- **Reduce dimensionalitatea** păstrând informația esențială.
- **Îmbunătățește performanța** modelelor de învățare automată.
- Elimină **corelațiile** dintre variabile.
- Ușor de interpretat în cazul datelor liniare.

---

## Dezavantaje
- Este o metodă **liniară** – nu captează relațiile complexe neliniare.
- Poate pierde informații importante dacă numărul de componente ales este prea mic.
- Componentele principale nu au mereu **o interpretare directă**.

---

## Parametri cheie
- **n_components**: Numărul de componente principale reținute.
- **whiten**: Scalarea componentelor pentru a avea varianță unitară (opțional).
- **svd_solver**: Algoritmul folosit pentru calcul (`auto`, `full`, `randomized`).

---

## Aplicații
- **Recunoaștere facială** (eigenfaces).
- Reducerea zgomotului din date.
- Vizualizarea datelor în 2D sau 3D.
- Preprocesarea datelor pentru algoritmi de clustering sau clasificare.

---

## Interpretarea rezultatului
- **Explained Variance Ratio**: Procentul de variație din date explicat de fiecare componentă principală.  
  Exemplu: Prima componentă poate explica 70% din variație, a doua 20%, etc.
