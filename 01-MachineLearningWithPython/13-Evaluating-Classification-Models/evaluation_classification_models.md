# 📊 Evaluating Classification Models

## 1. Train/Test Split
- **Scop**: Evaluarea performanței modelului pe date **nevăzute**.
- Împărțim datele în:
  - **Training set** → modelul învață
  - **Test set** → modelul este evaluat

---

## 2. Principalele Metrici de Evaluare

### ✅ Accuracy (Acuratețe)
- Proporția de predicții corecte (TP + TN) din total.
- Bună când clasele sunt **echilibrate**, dar înșelătoare dacă există **clasă rară**.

---

### 🔁 Confusion Matrix (Matricea de confuzie)
- Arată distribuția predicțiilor față de realitate:
  - **TP** (True Positives) – cazuri pozitive corect clasificate
  - **TN** (True Negatives) – cazuri negative corect clasificate
  - **FP** (False Positives) – cazuri negative clasificate ca pozitive
  - **FN** (False Negatives) – cazuri pozitive clasificate ca negative

---

### 🎯 Precision (Precizie)
- Proporția predicțiilor pozitive care sunt corecte.
- Formula: `TP / (TP + FP)`
- Importantă când costul **fals-pozitivelor** este mare (ex: diagnostic greșit de cancer).

---

### 📌 Recall (Sensibilitate / TPR)
- Proporția cazurilor pozitive detectate corect.
- Formula: `TP / (TP + FN)`
- Importantă când costul **fals-negative** este mare (ex: fraudă nedetectată).

---

### ⚖️ F1-Score
- Media armonică dintre **Precision** și **Recall**.
- Utilă când există **clase dezechilibrate**.
- Formula: `2 * (Precision * Recall) / (Precision + Recall)`

---

## 3. Alte metrici utile
- **Specificitate (TNR)**: cât de bine detectează modelul cazurile negative → `TN / (TN + FP)`
- **ROC Curve & AUC**:
  - ROC = raport între **TPR și FPR**
  - AUC = aria de sub curbă (0.5 = aleatoriu, 1.0 = perfect)

---

## 4. Exemple practice: KNN și SVM
### 🔹 KNN (K-Nearest Neighbors)
- Algoritm bazat pe vecini.
- Sensibil la **scalarea datelor** și la **zgomot**.

### 🔹 SVM (Support Vector Machine)
- Creează un **hiperplan optim** pentru separarea claselor.
- Kernel `linear` sau `rbf` pentru date mai complexe.

---

## 5. Interpretarea Rezultatelor
- Evaluăm **atât pe train cât și pe test set** pentru a depista:
  - **Overfitting** (scor mare pe train, slab pe test)
  - **Underfitting** (scor slab pe ambele)

- **Confusion Matrix + Classification Report** → arată distribuția precisă a erorilor.

---

## 6. Concluzii
- Nu ne bazăm doar pe **accuracy**.
- Alegerea metricii depinde de **context**:
  - Cost ridicat al FP → **Precision**
  - Cost ridicat al FN → **Recall**
  - Clase dezechilibrate → **F1-score**, **ROC-AUC**
- Vizualizările (heatmap, ROC curve) ajută la interpretarea corectă a performanței.
