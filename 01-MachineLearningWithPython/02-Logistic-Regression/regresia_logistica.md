# 📊 Regresie Logistică

Regresia logistică este un model de învățare automată supravegheată folosit pentru **clasificare binară** (ex: spam vs. non-spam, boală vs. sănătos, etc.).

---

## 🧠 Ce este Regresia Logistică?

Este un algoritm statistic care estimează **probabilitatea** ca o observație să aparțină uneia dintre cele două clase posibile, folosind o funcție logistică (sigmoid).

---

## 📈 Formula

Modelul pornește de la o combinație liniară:

z = w₀ + w₁·x₁ + w₂·x₂ + ... + wₙ·xₙ

Se aplică funcția **sigmoid**:

ŷ = σ(z) = 1 / (1 + e^(-z))

Aici:
- `ŷ` este probabilitatea ca exemplul să aparțină clasei pozitive (`1`)
- `w₀` este bias-ul (interceptul)
- `wᵢ` sunt coeficienții (greutățile) asociați fiecărei caracteristici `xᵢ`

---

## 🔍 Clasificare

După ce se calculează `ŷ`, se aplică un prag (`threshold`) pentru clasificare:

ŷ ≥ 0.5 → Clasa 1
ŷ < 0.5 → Clasa 0


Acest prag poate fi ajustat în funcție de problemă.

---

## 🧪 Funcția de pierdere

Se folosește **log-loss** (pierdere logaritmică / entropie încrucișată):

Loss = - [ y·log(ŷ) + (1 - y)·log(1 - ŷ) ]


Pentru întreg setul de date, se ia media pe toate exemplele.

---

## 📉 Optimizare

- Se folosește **Gradient Descent** pentru a ajusta coeficienții `wᵢ` astfel încât să minimizeze funcția de pierdere.
- Algoritmul este iterativ și se oprește când convergența este atinsă.

---

## ✅ Avantaje

- Simplu și eficient
- Ușor de interpretat
- Bun pentru probleme binare
- Performant pe seturi de date liniare

---

## ❌ Limitări

- Nu funcționează bine când relația dintre date nu este liniară
- Sensibil la outlieri
- Nu suportă în mod nativ clasificarea multi-clasă (se poate extinde cu **One-vs-Rest**)

---

## 📦 Implementare în Python (cu `scikit-learn`)

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X: caracteristici, y: etichete binare
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Acuratețea modelului: {acc:.2f}")


