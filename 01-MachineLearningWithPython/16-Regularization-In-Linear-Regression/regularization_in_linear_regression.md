# 📘 Regularizarea în regresie și clasificare

Regularizarea este o tehnică folosită pentru a **controla complexitatea modelelor** și pentru a preveni **supraînvățarea (overfitting)**. Ea adaugă o penalizare asupra coeficienților modelului pentru a evita valori exagerat de mari și pentru a îmbunătăți **generalizarea** pe date noi.

---

## 1) Probleme în regresia obișnuită

- Regresia liniară obișnuită ajustează coeficienții pentru a minimiza **eroarea pătratică medie (MSE)**.  
- În prezența:
  - **zgomotului**,
  - **outlierilor**,
  - sau a unui număr foarte mare de **caracteristici (features)**,  
  coeficienții pot deveni foarte mari → ceea ce duce la instabilitate și predicții slabe pe date noi.

---

## 2) Regularizarea

Regularizarea rezolvă aceste probleme adăugând un termen de **penalizare** în funcția de cost:

### 🔹 Ridge Regression (L2 regularization)
- Adaugă penalizare proporțională cu **suma pătratelor coeficienților**.  
- Funcția de cost devine:  
  \[
  J(\theta) = MSE + \alpha \sum \theta_i^2
  \]
- Efect: coeficienții sunt **micșorați**, dar rămân diferiți de zero.  
- Bun pentru situații cu multe variabile corelate.  

---

### 🔹 Lasso Regression (L1 regularization)
- Adaugă penalizare proporțională cu **suma valorilor absolute ale coeficienților**.  
- Funcția de cost devine:  
  \[
  J(\theta) = MSE + \alpha \sum |\theta_i|
  \]
- Efect: unele coeficiente devin **exact zero** → selectează automat caracteristicile importante.  
- Bun pentru **reducerea dimensionalității** și **feature selection**.  

---

### 🔹 Elastic Net
- Combinație între Ridge și Lasso.  
- Controlează echilibrul dintre micșorarea coeficienților și eliminarea unor variabile.  

---

## 3) Efectele regularizării

- **Coeficienți mai mici** → modelul devine mai simplu.  
- **Rezistență mai mare la outlieri** → nu mai este puternic influențat de valori extreme.  
- **Generalizare mai bună** → performanță mai stabilă pe datele de test.  
- **Selectarea caracteristicilor** → Lasso elimină variabile irelevante.  

---

## 4) Comparație vizuală

- **Regresie liniară simplă** → se potrivește prea mult pe date, afectată de outlieri.  
- **Ridge** → linie de regresie mai robustă, nu exagerează coeficienții.  
- **Lasso** → linie de regresie robustă + elimină caracteristici inutile.  

---

## 5) Evaluarea modelelor de regresie

Metrici folosiți pentru compararea regresiei obișnuite, Ridge și Lasso:

- **Explained Variance (EV)** → cât de mult din variația datelor este explicată de model.  
- **R² Score** → proporția variației explicate.  
- **MAE (Mean Absolute Error)** → eroarea medie absolută.  
- **MSE (Mean Squared Error)** → eroarea pătratică medie.  
- **RMSE (Root Mean Squared Error)** → abaterea standard a erorii.  

---

## 6) Regularizarea în regresie multivariată (high-dimensional)

- În dataseturi cu **mii de features**, regresia simplă poate fi instabilă.  
- **Ridge** → păstrează toate caracteristicile, dar le micșorează coeficienții.  
- **Lasso** → păstrează doar caracteristicile cu impact semnificativ, setând coeficienții altora la zero.  
- **Feature selection cu Lasso** → permite reducerea dimensionalității și simplificarea modelului.  

---

## 7) Concluzii

- **Linear Regression**: sensibilă la outlieri și la multe variabile.  
- **Ridge Regression**: bună pentru multicoliniaritate, reduce magnitudinea coeficienților.  
- **Lasso Regression**: bună pentru reducerea dimensionalității, elimină caracteristici irelevante.  
- **Elastic Net**: echilibrul optim între Ridge și Lasso.  

---

✅ **Ideea centrală**:  
Regularizarea (Ridge și Lasso) face modelele **mai robuste, mai generalizabile și mai simple**, prevenind supraînvățarea și permițând **selecția automată a caracteristicilor**.
