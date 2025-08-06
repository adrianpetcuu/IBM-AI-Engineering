# 📊 Clasificare în Învățarea Automată (Classification)

## 🔍 Ce este Clasificarea?

Clasificarea este o sarcină de **învățare supravegheată** în care obiectivul este de a **prezice o etichetă (clasă)** dintr-un set fix de categorii, pe baza unor caracteristici de intrare (features).

### Exemple:
- Clasificare binară: Email spam sau non-spam
- Clasificare multiclasa: Recunoașterea cifrelor scrise de mână (0–9)
- Clasificare multilabel: Un text poate aparține mai multor categorii

---

## 🧠 Strategii de clasificare multi-clasă

### ✅ One-vs-All (OvA) — *"Unul împotriva tuturor"*

În această strategie:
- Se antrenează un **clasificator binar pentru fiecare clasă**.
- Fiecare model învață să distingă o clasă de toate celelalte.
- La testare, se evaluează toate modelele și se alege clasa cu **scorul cel mai mare**.

#### Avantaje:
- ✔️ Simplu de implementat
- ✔️ Mai puține clasificatoare decât OvO
- ✔️ Suportat direct de modele ca `LogisticRegression` sau `SVC`

#### Dezavantaje:
- ❌ Poate suferi din cauza claselor dezechilibrate
- ❌ Scorurile pot fi apropiate → predicție ambiguă

#### Cod exemplu:
```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(multi_class='ovr', max_iter=1000)
model.fit(X_train, y_train)
```

### ⚔️ One-vs-One (OvO) — *"Unul împotriva unuia"*

În această strategie:
- Se antrenează câte un **clasificator pentru fiecare pereche posibilă de clase**.
- Dacă avem `k` clase, se antrenează `k * (k - 1) / 2` modele.
- Fiecare model votează pentru o clasă.
- Clasa care primește **cele mai multe voturi** este aleasă ca predicție.

#### Avantaje:
- ✔️ Poate fi mai precis, deoarece fiecare model învață doar două clase
- ✔️ Reduce ambiguitatea între clase apropiate

#### Dezavantaje:
- ❌ Necesită multe modele (ex: 10 clase → 45 modele)
- ❌ Mai lent la predicție
- ❌ Voturi egale → posibilă ambiguitate

#### Cod exemplu:
```python
from sklearn.multiclass import OneVsOneClassifier
from sklearn.linear_model import LogisticRegression

model = OneVsOneClassifier(LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
```

---

## ✅ Evaluarea Performanței Modelului

Pentru a evalua cât de bine se comportă un model de clasificare, folosim metrici precum:

### 📏 Accuracy (Acuratețe)

Procentul de predicții corecte față de totalul probelor:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Acuratețea modelului:", accuracy)
```

## 📊 Matricea de Confuzie în Clasificare

### Ce este?

Matricea de confuzie este un tabel care arată performanța unui model de clasificare, comparând predicțiile modelului cu valorile reale (adevărate).

---

### 🧩 Structura matricei (pentru două clase)

|                 | Prezis: Pozitiv | Prezis: Negativ |
|-----------------|------------------|------------------|
| **Real: Pozitiv** | True Positive (TP) | False Negative (FN) |
| **Real: Negativ** | False Positive (FP) | True Negative (TN) |

---

### 🎯 Metrici importante calculate din matrice

- **Acuratețe (Accuracy):**
  > Procentul total de predicții corecte
  ```python
  from sklearn.metrics import accuracy_score
  accuracy = accuracy_score(y_test, y_pred)
```