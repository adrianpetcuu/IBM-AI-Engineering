# 🌳 Regression Trees (Arbori de regresie)

## 🔍 Ce este un arbore de regresie?

Un **arbore de regresie** este un tip de arbore de decizie folosit pentru **predicții numerice continue**. În loc să returneze o clasă (ca în clasificare), returnează o **valoare numerică** (ex: prețul unei case, temperatura, venitul etc.).

---

## 🧠 Cum funcționează?

1. Datele sunt împărțite recursiv pe baza valorilor caracteristicilor (features), astfel încât să minimizeze eroarea totală (de obicei **Mean Squared Error**).
2. La fiecare nod, algoritmul alege **cea mai bună caracteristică și prag de împărțire** care reduce eroarea.
3. În frunzele arborelui, valoarea prezisă este **media** valorilor din setul de date local.

---

## ⚙️ Funcții de evaluare folosite

- **Mean Squared Error (MSE)** – eroarea pătratică medie
- **Mean Absolute Error (MAE)** – eroarea absolută medie

---

## ✅ Avantaje

- Ușor de interpretat și explicat
- Poate modela relații non-liniare
- Nu necesită scalarea datelor

---

## ❌ Dezavantaje

- Predispus la **overfitting**
- Nu este foarte stabil (modificări mici în date pot duce la arbori diferiți)

---

## 🧪 Cod exemplu (Regression Tree)

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Date de exemplu
data = fetch_california_housing()
X = data.data
y = data.target

# Împărțire train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
reg = DecisionTreeRegressor(max_depth=4)
reg.fit(X_train, y_train)

# Predictie
y_pred = reg.predict(X_test)

# Evaluare
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")
```