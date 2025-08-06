# 💻 Support Vector Machines (SVM)

## 🔍 Ce este SVM?

**SVM (Support Vector Machine)** este un algoritm de învățare supervizată folosit pentru **clasificare** și **regresie**. Scopul său este să găsească o **linie de separare optimă** (sau un hiperplan în spații multidimensionale) care **maximizează marginea** între clase.

---

## ✳️ Cum funcționează?

1. SVM caută acel **hiperplan** care separă clasele cu **cea mai mare distanță** față de cele mai apropiate puncte de fiecare clasă (numite **vectori de suport**).
2. Dacă datele nu sunt liniar separabile, SVM folosește o tehnică numită **kernel trick** pentru a le proiecta într-un spațiu mai mare unde devin separabile.

---

## 🧠 Tipuri de SVM

- **SVC (Support Vector Classification)** – pentru clasificare
- **SVR (Support Vector Regression)** – pentru regresie

---

## 🧪 Kernel-uri disponibile

| Kernel      | Descriere                                  | Utilizare tipică               |
|-------------|---------------------------------------------|--------------------------------|
| linear      | linie dreaptă sau hiperplan                 | când datele sunt liniar separabile |
| poly        | polinomial                                  | pentru relații neliniare mai simple |
| rbf (gaussian) | radial basis function (default)         | majoritatea problemelor neliniare |
| sigmoid     | funcție sigmoid                            | asemănător cu rețele neuronale |

---

## ✅ Avantaje

- Funcționează bine în **spații cu dimensiuni mari**
- Eficient când numărul de caracteristici > numărul de eșantioane
- **Flexibil** prin utilizarea de kernel-uri
- Robust la overfitting (în cazul datelor curate)

---

## ❌ Dezavantaje

- Mai lent pe seturi de date foarte mari
- Performanța scade dacă datele sunt foarte zgomotoase
- Necesită **scalarea caracteristicilor** (standardizare)

---

## 🧪 Cod exemplu (SVM pentru clasificare)

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Încărcare date
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Standardizare
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Împărțire în train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Model SVM cu kernel RBF
clf = SVC(kernel='rbf', C=1.0, gamma='scale')
clf.fit(X_train, y_train)

# Predicții
y_pred = clf.predict(X_test)

# Evaluare
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

## 📌 Parametri importanți în SVC

| Parametru | Descriere |
|-----------|-----------|
| `C`       | Controlul overfitting-ului. Valori mari → overfit, valori mici → subfit. |
| `kernel`  | Tipul de funcție kernel folosit (`linear`, `rbf`, `poly`, `sigmoid`). |
| `gamma`   | Definirea influenței fiecărui punct de date în cazul kernel-ului RBF. |

---

### 🎯 Când să folosești SVM?

- Pentru **clasificare binară** sau **multi-clasă**, când datele sunt **curate** și **nu extrem de numeroase**.
- În probleme de **bioinformatică**, **clasificare de text**, **recunoaștere facială** etc.
- Când alte modele (**Logistic Regression**, **KNN**) nu oferă performanță bună.

---

### 📚 Notă

SVM este un algoritm **clasic**, dar **extrem de puternic**.  
În ciuda apariției multor modele moderne, el rămâne competitiv pentru **seturi de date mici și medii**, **bine prelucrate**.
