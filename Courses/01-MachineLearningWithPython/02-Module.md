# Modulul 2: Modele de Regresie in Machine Learning

Acest modul acoperă conceptele esențiale legate de regresie în machine learning, incluzând regresia liniară simplă, multiplă, polinomială și logistică. Vom explora diferențele dintre aceste tehnici, când se folosesc, cum se implementează și cum se evaluează performanța lor.

---

## 1. Regresia Liniară Simplă

**Scop:** Prezicerea unei variabile dependente continue pe baza unei singure variabile independente.

* Model matematic: `y = b0 + b1 * x`
* Măsura performanței: Mean Squared Error (MSE)
* Implementare: `LinearRegression()` din `sklearn.linear_model`

### Exemplu:

Prezicerea emisiilor CO2 în funcție de mărimea motorului (`ENGINESIZE`).

---

## 2. Regresia Liniară Multiplă

**Scop:** Prezicerea unei variabile dependente folosind mai multe variabile independente.

* Model: `y = b0 + b1 * x1 + b2 * x2 + ... + bn * xn`
* Avantaje: Permite captarea influenței mai multor factori
* Riscuri: Overfitting dacă se includ prea multe variabile

### Exemplu:

Prezicerea emisiilor CO2 în funcție de `ENGINESIZE` și `FUELCONSUMPTION_COMB_MPG`

---

## 3. Regresia Polinomială

**Scop:** Modelarea relațiilor neliniare între variabile.

* Model: `y = b0 + b1 * x + b2 * x^2 + ... + bn * x^n`
* Utilă când datele nu urmează o relație liniară
* Se folosesc `PolynomialFeatures` din `sklearn.preprocessing`

---

## 4. Regresia Logistică

**Scop:** Clasificarea binară (ex: churn vs non-churn)

* Model: `log(p / (1 - p)) = b0 + b1 * x1 + ... + bn * xn`
* Predicții: Probabilitatea de apartenență la o clasă
* Măsură de performanță: `log_loss`
* Se folosește `LogisticRegression()` din `sklearn`

### Exemplu:

Prezicerea probabilității de a anula o rezervare sau de a părăsi serviciul (churn).

---

## 5. Evaluarea Performanței

| Metrică               | Tip Model   | Descriere                                             |
| --------------------- | ----------- | ----------------------------------------------------- |
| `mean_absolute_error` | regresie    | eroare medie absolută                                 |
| `mean_squared_error`  | regresie    | eroare medie pătratică                                |
| `r2_score`            | regresie    | scorul R^2: proporția variabilității explicate        |
| `log_loss`            | clasificare | penalizare logaritmică pentru probabilități incorecte |

---

## 6. Funcții și metode utile

* `train_test_split`: împarte datele în seturi de antrenare și testare
* `StandardScaler`: standardizează caracteristicile (mean = 0, std = 1)
* `predict`, `predict_proba`: metode pentru predicții

---

## 7. Concepte Cheie Recapitulative

* Regresia liniară simplă folosește o singură caracteristică.
* Regresia multiplă folosește mai multe caracteristici.
* Regresia polinomială extinde modelul liniar pentru date neliniare.
* Regresia logistică este folosită pentru clasificare binară.
* Metricile de performanță variază în funcție de tipul modelului (regresie sau clasificare).

---

## 8. Resurse de Cod & Exemplu

Am utilizat dataseturi precum:

* `FuelConsumptionCo2.csv` pentru regresii liniare
* `ChurnData.csv` pentru regresie logistică

Toate modelele au fost implementate folosind `scikit-learn`, iar rezultatele au fost vizualizate cu `matplotlib`.

---

### Încheiere

Acest modul formează fundamentul pentru înțelegera algoritmilor de regresie și cum pot fi folosiți pentru predicții sau clasificare în machine learning.
