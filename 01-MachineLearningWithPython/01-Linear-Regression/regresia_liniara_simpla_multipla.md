# 📘 README – Regresie Liniară Simplă și Multiplă

## 🔍 Ce este regresia liniară?
Regresia liniară este o tehnică de învățare automată supravegheată folosită pentru a prezice o variabilă dependentă continuă (`y`) pe baza uneia sau mai multor variabile independente (`X`). Modelul presupune o relație liniară între aceste variabile.

---

## 📈 1. Regresie Liniară Simplă
**Scop:** Prezice o valoare continuă pe baza unei singure caracteristici (variabilă independentă).

**Model matematic:**  
`y = b₀ + b₁ * x`

**Unde:**  
- `y` este valoarea prezisă  
- `x` este caracteristica (input)  
- `b₀` este interceptul (bias)  
- `b₁` este coeficientul de regresie (pantă)  

**Avantaje:**  
- Simplu de implementat și înțeles  
- Eficient pentru seturi de date mici  

**Dezavantaje:**  
- Poate subestima relațiile complexe  
- Nu captează curbe sau relații neliniare  

**Exemplu cod Python:**  
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y) 
```

## 📊 2. Regresie Liniară Multiplă

**Scop:** Prezice o valoare continuă pe baza mai multor caracteristici (inputuri).

**Model matematic:**  
`y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ`

**Unde:**  
- `y` este valoarea prezisă  
- `x₁, x₂, ..., xₙ` sunt caracteristicile independente  
- `b₀` este interceptul (bias)  
- `b₁, b₂, ..., bₙ` sunt coeficienții pentru fiecare variabilă  

**Avantaje:**  
- Permite încorporarea mai multor factori  
- Poate oferi predicții mai precise  

**Dezavantaje:**  
- Presupune relații liniare între toate variabilele  
- Poate duce la overfitting dacă sunt prea multe variabile  

**Exemplu cod Python:**
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
```

---

## 🧮 3. Regresie Polinomială

**Scop:** Extinde regresia liniară pentru a capta relații neliniare.

**Model matematic (grad 2):**  
`y = b₀ + b₁x + b₂x²`

**Avantaje:**  
- Mai precisă pentru relații curbilinii  
- Ușor de implementat cu `scikit-learn`

**Dezavantaje:**  
- Prone to overfitting la grade înalte  
- Necesită transformarea manuală a caracteristicilor

**Exemplu cod Python:**
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)
```

---

## 📊 4. Evaluarea modelului (metode comune):

| Funcție                  | Ce face                                                                 | Cod Python                                                              |
|--------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `train_test_split()`     | Împarte datele în seturi de antrenare/testare                            | `from sklearn.model_selection import train_test_split`                 |
| `mean_squared_error()`   | Eroarea pătratică medie între valori reale și prezise                    | `from sklearn.metrics import mean_squared_error`                       |
| `r2_score()`             | Proporția variabilității explicate de model                              | `from sklearn.metrics import r2_score`                                 |
| `mean_absolute_error()`  | Eroarea absolută medie între valorile reale și cele prezise              | `from sklearn.metrics import mean_absolute_error`                      |
| `StandardScaler()`       | Normalizează datele (centrat și scalat la deviație standard unitară)     | `from sklearn.preprocessing import StandardScaler`                     |

---

## 🧠 Notițe importante

- **R² (R-squared):** Cu cât este mai aproape de `1`, cu atât modelul explică mai bine variabilitatea din date.  
- **MSE (Mean Squared Error):** Măsoară eroarea pătratică medie – valori mai mici sunt mai bune.  
- **RMSE (Root Mean Squared Error):** Rădăcina pătrată a MSE – exprimată în aceleași unități ca și ținta (`y`).  
- **Overfitting:** Modelul învață prea bine datele de antrenament, dar are performanță slabă pe date noi.  
- **Underfitting:** Modelul este prea simplu pentru a capta structura reală a datelor.

---

## 🔧 Exemple de aplicații

- 📊 Prezicerea prețurilor imobiliare (folosind regresie liniară multiplă)  
- 💼 Estimarea salariului pe baza anilor de experiență (regresie simplă)  
- 🛒 Estimarea cererii de produse în funcție de preț și sezon (regresie multiplă)  

---



