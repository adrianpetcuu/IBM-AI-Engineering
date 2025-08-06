# 🤖 K Nearest Neighbors (KNN)

## 🔍 Ce este KNN?

KNN este un algoritm de învățare supravegheată (supervised learning) folosit pentru **clasificare** și **regresie**.  
Este un **algoritm bazat pe instanțe (lazy learning)** – nu învață un model în prealabil, ci face predicții folosind **vecinii cei mai apropiați** din setul de antrenament.

---

## ⚙️ Cum funcționează?

1. Se alege un număr `K` (număr de vecini).
2. Pentru o nouă observație, se calculează distanța față de toate datele din setul de antrenament.
3. Se selectează cei mai apropiați `K` vecini.
4. Se face predicția:
   - **Clasificare**: se alege clasa cea mai frecventă dintre vecini.
   - **Regresie**: se face media valorilor vecinilor.

---

## 📏 Metode de calcul al distanței

- **Distanța Euclidiană** (cel mai frecvent):
  \[
  d(p, q) = \sqrt{ \sum_{i=1}^{n} (p_i - q_i)^2 }
  \]
- Distanța Manhattan
- Distanța Minkowski
- Distanță Cosinus, etc.

---

## 🔧 Parametri importanți în KNN

| Parametru | Descriere |
|-----------|-----------|
| `n_neighbors` | Numărul de vecini `K`. Trebuie ajustat cu grijă – prea mic → overfitting, prea mare → underfitting. |
| `weights`     | Modul de ponderare a vecinilor: `'uniform'` (toți egal) sau `'distance'` (vecinii apropiați au mai multă influență). |
| `metric`      | Măsura de distanță folosită (`'euclidean'`, `'manhattan'`, `'minkowski'` etc.). |
| `algorithm`   | Algoritm de căutare: `'auto'`, `'ball_tree'`, `'kd_tree'`, `'brute'`. Poate influența viteza de execuție. |

---

## ✅ Avantaje

- Ușor de înțeles și implementat.
- Fără antrenare propriu-zisă (lazy learner).
- Funcționează bine pentru seturi de date mici și bine etichetate.

---

## ❌ Dezavantaje

- Devine lent pentru seturi de date mari.
- Sensibil la **scalarea datelor** și la **dimensionalitate mare**.
- Performanță slabă în caz de **date zgomotoase** sau dezechilibrate.

---

## 🎯 Când să folosești KNN?

- Pentru **probleme de clasificare** cu puține caracteristici.
- Când interpretabilitatea modelului este importantă.
- Când ai date puține și nu vrei antrenare lungă.

---

## 🧪 Recomandări practice

- Folosește **StandardScaler** sau **MinMaxScaler** înainte de a aplica KNN (pentru că se bazează pe distanțe).
- Testează mai multe valori ale lui `K` (de ex. `1, 3, 5, 7, 11`) folosind **cross-validation**.
- Evită KNN pe seturi de date foarte mari fără optimizări (ex: folosirea de KD-trees).

