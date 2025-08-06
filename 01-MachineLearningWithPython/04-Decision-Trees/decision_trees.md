# 🌳 Decision Trees (Arbori de decizie)

## 🔍 Ce este un arbore de decizie?

Un **arbore de decizie** este un algoritm de învățare automată supravegheat care poate fi folosit pentru **clasificare** sau **regresie**. Funcționează împărțind setul de date în subseturi mai mici, pe baza unui set de condiții, construind o structură de tip arbore.

---

## 🧠 Cum funcționează?

1. Se selectează o caracteristică (feature) care împarte cel mai bine datele.
2. Se creează un nod în arbore pe baza acestei caracteristici.
3. Se repetă procesul recursiv pentru fiecare subset de date, construind ramuri și frunze.
4. Frunza finală conține predicția (clasă sau valoare numerică).

---

## ✳️ Tipuri

- **Classification Tree** – folosit pentru a clasifica date în clase (ex: spam / non-spam).
- **Regression Tree** – folosit pentru a prezice valori continue (ex: prețul unei case).

---

## 📊 Exemple de criterii de împărțire

- **Gini impurity**
- **Entropy (Information Gain)**
- **Mean Squared Error (pentru regresie)**

---

## ✅ Avantaje

- Ușor de înțeles și interpretat
- Nu necesită preprocesare extinsă
- Poate gestiona atât date numerice cât și categorice

---

## ❌ Dezavantaje

- Predispus la **overfitting** (modelul învață prea bine datele de antrenament)
- Sensibil la variații în date

---

## 🧪 Cod exemplu (Classification Tree)

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Date de exemplu
data = load_iris()
X = data.data
y = data.target

# Împărțire train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf.fit(X_train, y_train)

# Predictie
y_pred = clf.predict(X_test)

# Evaluare
print(classification_report(y_test, y_pred))

# Matrice de confuzie
ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test)
plt.show()
```