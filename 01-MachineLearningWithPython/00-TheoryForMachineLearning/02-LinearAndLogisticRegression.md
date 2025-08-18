# Fișă de sinteză: Regressie Liniară și Logistică

## Compararea diferitelor tipuri de regresie

| Model | Descriere | Ecuație de modelare |
|---|---|---|
| **Regresie liniară simplă** | **Scop:** prezice o variabilă dependentă dintr-o singură variabilă independentă. <br> **Avantaje:** ușor de implementat și interpretat; eficientă pe seturi mici. <br> **Dezavantaje:** nu surprinde relații complexe; poate sub-ajusta. | `y = b₀ + b₁x` |
| **Regresie polinomială** | **Scop:** surprinde relații neliniare între variabile. <br> **Avantaje:** mai bună decât liniara pentru date neliniare. <br> **Dezavantaje:** risc de supra-ajustare la grade mari. | `y = b₀ + b₁x + b₂x² + …` |
| **Regresie liniară multiplă** | **Scop:** prezice din mai multe variabile independente. <br> **Avantaje:** permite includerea mai multor factori. <br> **Dezavantaje:** presupune relație liniară între predictori și țintă. | `y = b₀ + b₁x₁ + b₂x₂ + …` |
| **Regresie logistică** | **Scop:** prezice probabilități pentru rezultate categoriale (mai ales binare). <br> **Avantaje:** eficientă pentru clasificare binară. <br> **Dezavantaje:** presupune relație liniară între variabile și log-odds. | `log(p/(1−p)) = b₀ + b₁x₁ + …` |

---

## Funcții / metode asociate folosite frecvent

| Funcție / Metodă | Descriere | Utilizare (conceptuală) |
|---|---|---|
| **`train_test_split`** | Împarte datele în antrenare și test pentru a evalua performanța. | `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)` |
| **`StandardScaler`** | Standardizează caracteristicile (media 0, varianță 1). | `X_scaled = StandardScaler().fit_transform(X)` |
| **`log_loss`** | Pierdere logaritmică (metrică pentru clasificare probabilistică). | `log_loss(y_true, y_pred_proba)` |
| **`mean_absolute_error` (MAE)** | Media absolută a erorilor dintre valori reale și prezise. | `mean_absolute_error(y_true, y_pred)` |
| **`mean_squared_error` (MSE)** | Media pătratelor erorilor (penalizează devierile mari). | `mean_squared_error(y_true, y_pred)` |
| **`root_mean_squared_error` (RMSE)** | Rădăcina pătrată a MSE; în aceleași unități ca ținta. | `RMSE = sqrt(MSE)` |
| **`r2_score` (R²)** | Proporția din variația țintei explicată de model. | `r2_score(y_true, y_pred)` |



# 📊 Modele de Regresie – Rezumat

## 1) Ce este regresia?
- Modelele de **regresie** stabilesc relații între o **variabilă țintă continuă** și un set de **variabile explicative**.
- Tipuri de regresie:
  - **Regresie simplă** → o singură variabilă independentă.
  - **Regresie multiplă** → mai multe variabile independente.

---

## 2) Aplicații ale regresiei
- Prognozarea vânzărilor.
- Estimarea costurilor de întreținere.
- Predicția cantității de precipitații.
- Modelarea răspândirii bolilor.

---

## 3) Regresie Liniară Simplă
- Utilizează **o linie de regresie (best-fit line)** pentru a aproxima relația dintre X și Y.
- Eroarea se măsoară prin **MSE (Mean Squared Error)**.
- Metoda folosită: **OLS (Ordinary Least Squares)** → minimizează suma pătratelor erorilor.
- Avantaje: interpretare simplă.
- Limitări: sensibilitate la **outlieri**, care pot distorsiona predicțiile.

---

## 4) Regresie Liniară Multiplă
- Extinde regresia simplă prin folosirea mai multor variabile explicative.
- Permite analiza relațiilor complexe între factori.
- Pericol: **overfitting** dacă se includ prea multe variabile → modelul "învață zgomotul".
- Soluție: **selecția atentă a variabilelor**.

---

## 5) Regresie Non-Lineară
- Folosită când relația nu poate fi descrisă printr-o linie dreaptă.
- Exemple:
  - **Regresie polinomială** → folosește termeni de ordin mai mare (X², X³ etc.).
  - **Regresie exponențială**.
  - **Regresie logaritmică**.
- Atenție: regresia polinomială poate **supraajusta (overfit)** datele, captând zgomotul și nu tiparele reale.

---

## 6) Regresie Logistică
- Nu este regresie în sens strict, ci **clasificator binar** și **predictor de probabilități**.
- Ținta: variabilă binară (ex.: 0/1, da/nu).
- Măsoară impactul variabilelor asupra probabilității.
- Funcția de cost: **Log-loss**.
- Optimizare: **Gradient Descent** sau **Stochastic Gradient Descent** pentru eficiență.

---

## 7) Gradient Descent
- Metodă iterativă de **minimizare a funcției de cost**.
- Pași:
  1. Se pornește de la o valoare inițială a coeficienților.
  2. Se ajustează coeficienții treptat, urmând direcția pantei negative a gradientului.
  3. Procesul continuă până la atingerea unui minim (ideal, global).
- Esențial pentru antrenarea modelelor de regresie logistică.

---

