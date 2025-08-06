# 🌳 Random Forest

## 🔍 Ce este Random Forest?

Random Forest este un algoritm de **învățare supravegheată** bazat pe **ensemble learning**, care creează o „pădure” de **mai mulți arbori de decizie** (decision trees) și ia decizia finală pe baza **votului majoritar** (pentru clasificare) sau **mediei** (pentru regresie).

---

## ⚙️ Cum funcționează?

1. Se creează mai mulți arbori de decizie, fiecare antrenat pe un subset diferit al datelor (prin **bootstrap sampling**).
2. La fiecare split al unui arbore, se selectează aleatoriu doar un subset de caracteristici.
3. Se face predicția:
   - **Clasificare**: votul majoritar al arborilor.
   - **Regresie**: media predicțiilor arborilor.

---

## 🔧 Parametri importanți

| Parametru          | Descriere |
|--------------------|-----------|
| `n_estimators`     | Numărul de arbori din pădure. Valori mari → stabilitate, dar cost computațional mai mare. |
| `max_depth`        | Adâncimea maximă a fiecărui arbore. Evită overfitting-ul. |
| `max_features`     | Numărul maxim de caracteristici considerate la fiecare split. |
| `bootstrap`        | Dacă să folosească bootstrap sampling (True/False). |
| `random_state`     | Pentru reproducibilitate. |
| `criterion`        | Funcția de impurețe (`gini`, `entropy` pentru clasificare, `mse`, `mae` pentru regresie). |

---

## ✅ Avantaje

- Robust la overfitting.
- Poate gestiona date lipsă și categorii.
- Bună performanță pe date complexe.
- Poți obține **importanța caracteristicilor**.

---

## ❌ Dezavantaje

- Mai lent decât un singur arbore de decizie.
- Mai greu de interpretat.
- Nu e ideal pentru date extrem de mari fără optimizări.

---

## 🧠 Când să folosești Random Forest?

- Când vrei un model solid, cu performanță bună, fără multă reglare.
- Când ai multe caracteristici și/sau date cu zgomot.
- Pentru probleme de clasificare și regresie generală.
# ⚡ XGBoost (Extreme Gradient Boosting)

## 🔍 Ce este XGBoost?

XGBoost este un algoritm de boosting foarte performant, bazat pe arbori de decizie. Este o **tehnică de ensemble learning**, care creează arbori secvențial, fiecare încercând să **corecteze greșelile** anterioare.

---

## 🚀 De ce este „extreme”?

- Optimizare avansată a vitezei și memoriei.
- Regularizare `L1` și `L2` pentru prevenirea overfitting-ului.
- Suport paralelizat și scalabil.
- Foarte folosit în competiții (ex: Kaggle).

---

## ⚙️ Cum funcționează?

1. Se pornește de la un model slab (de obicei un arbore mic).
2. Fiecare arbore nou este construit pentru a reduce erorile modelului anterior.
3. Se folosește **Gradient Boosting** pentru actualizarea greutăților.

---

## 🔧 Parametri importanți

| Parametru          | Descriere |
|--------------------|-----------|
| `n_estimators`     | Numărul total de arbori (iterații). |
| `learning_rate`    | Cât de mult influențează fiecare arbore nou modelul final. Valori mai mici → învățare mai lentă, dar mai stabilă. |
| `max_depth`        | Adâncimea maximă a fiecărui arbore. |
| `subsample`        | Procentul de date folosite pentru fiecare arbore. Ajută la regularizare. |
| `colsample_bytree` | Procentul de caracteristici selectate pentru fiecare arbore. |
| `gamma`            | Minimul necesar de reducere a pierderii pentru a face un split. |
| `reg_alpha`, `reg_lambda` | Termeni de regularizare L1 și L2. |

---

## ✅ Avantaje

- Extrem de precis.
- Scalabil și rapid.
- Previne overfitting-ul.
- Acceptă date lipsă și categorice (în unele implementări).

---

## ❌ Dezavantaje

- Mai greu de înțeles și ajustat.
- Necesită reglaj de parametri (`grid search`, `optuna` etc.).
- Nu e ideal pentru date extrem de zgomotoase fără filtrare.

---

## 🧠 Când să folosești XGBoost?

- Pentru competiții și aplicații unde performanța e critică.
- Pentru seturi de date tabulare, mari și complexe.
- Când ai timp și resurse pentru tuning.

---


