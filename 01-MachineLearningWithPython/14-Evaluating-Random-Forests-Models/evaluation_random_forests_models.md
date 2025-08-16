# 📊 Evaluarea modelelor de regresie & Random Forest

Acest ghid rezumă teoria esențială pentru evaluarea modelelor de **regresie** și, în particular, a unui **Random Forest Regressor** pe un set de date precum *California Housing*.

---

## 1) Setarea experimentului

- Împărțirea datelor în **train/test** pentru a estima performanța reală.  
- Alegerea unui **model de regresie** (în exemplul nostru Random Forest).  
- Compararea performanței pe **train** și **test** pentru a identifica supraînvățarea (overfitting).  

---

## 2) Metrici esențiale de evaluare (regresie)

| Metrica | Ce măsoară | Observații |
|---------|------------|------------|
| **MAE (Mean Absolute Error)** | Eroarea medie în valoare absolută | Interpretabilă în unitățile țintei; mai robustă la outlieri decât MSE |
| **MSE (Mean Squared Error)** | Media erorilor pătrate | Penalizează puternic erorile mari; sensibilă la outlieri |
| **RMSE (Root Mean Squared Error)** | Rădăcina pătrată a MSE | În aceleași unități cu ținta; comparabilă cu MAE |
| **R² (Coefficient of Determination)** | Proporția varianței țintei explicată de model | 1 = perfect, 0 ≈ model de medie, poate fi negativ pe test |

🔑 **Reguli simple:**  
- **Mai mic** e mai bine pentru MAE, MSE, RMSE.  
- **Mai mare** e mai bine pentru R² (atenție la diferențe mari între train și test → overfitting).  

---

## 3) Analiza distribuției țintei

- Plotează histograma valorilor țintă pentru a verifica **asimetria (skewness)**.  
- Dacă distribuția este foarte dezechilibrată, erorile pot fi distorsionate.  
- Transformările logaritmice sau Box-Cox pot ajuta la reducerea skewness-ului.  

---

## 4) Diagnosticare vizuală

### a) Actual vs Predicted
- Scatter plot între valorile reale și cele prezise.  
- Dacă punctele sunt apropiate de linia diagonală → predicții bune.  
- Devieri sistematice de la linie → bias al modelului.  

### b) Reziduuri (y_true − y_pred)
- **Histogramă**: ar trebui să fie centrată pe 0; cozi lungi sugerează outlieri.  
- **Reziduuri vs. valori reale**: dacă există pattern-uri (de ex. creștere cu valoarea țintei), modelul are bias dependent de magnitudinea țintei.  

---

## 5) Importanța caracteristicilor (Feature Importance)

- Random Forest poate calcula cât de importante sunt variabilele pentru predicții.  
- Rezultatul se prezintă ca procentaj pentru fiecare variabilă.  
- **Atenție**: Importanțele nu implică **cauzalitate**. Dacă două variabile sunt corelate, importanța poate fi împărțită între ele.  

---

## 6) Random Forest – bune practici

### Parametri importanți
- **n_estimators**: numărul de arbori (mai mulți → stabilitate, dar cost computațional mai mare).  
- **max_depth**: limitează adâncimea arborilor (reduce overfitting).  
- **min_samples_leaf** / **min_samples_split**: impun regularizare suplimentară.  
- **max_features**: nr. de variabile candidate la fiecare split (de obicei sqrt sau log2).  

### Recomandări
- Nu necesită **scalarea datelor**.  
- Funcționează bine cu **relații neliniare** și interacțiuni între variabile.  
- Folosește **validare încrucișată** pentru alegerea parametrilor.  
- Verifică stabilitatea rezultatelor prin rulări repetate (schimbă seed-ul).  

---

## 7) Raport de evaluare – checklist

1. **Config experiment**: împărțirea datelor, model ales, parametri folosiți.  
2. **Metrici pe test**: MAE, MSE, RMSE, R² (compară cu train).  
3. **Grafice utile**:  
   - Actual vs Predicted  
   - Histograma reziduurilor  
   - Reziduuri vs. valori reale  
   - Feature Importances  
4. **Interpretare**:  
   - Identificarea biasului și a varianței.  
   - Subestimarea sau supraestimarea anumitor intervale de valori.  
   - Care variabile par cele mai influente.  
5. **Pași următori**:  
   - Optimizarea parametrilor.  
   - Transformări de variabile (dacă există skewness).  
   - Analiză suplimentară a outlierilor.  

---

## 8) Exemple de concluzii

- **Performanță**: raportarea numerică (ex: „R² = 0.82 pe test”).  
- **Diagnoză**: modelul subestimează valorile mari (casele cele mai scumpe).  
- **Importanțe**: venitul median și locația geografică sunt factori majori.  
- **Îmbunătățiri**: tuning parametri, adăugare de features derivate, transformarea țintei.  

---

## 9) Capcane frecvente

- **Data leakage**: nu introduce informații viitoare în setul de antrenare.  
- **Overfitting**: diferență mare între performanța pe train și test.  
- **Interpretare greșită**: feature importance ≠ cauzalitate.  
- **Distribuții diferite**: dacă train și test provin din surse diferite, performanța scade în realitate.  

---

✅ **Ideea centrală**: Evaluarea unui model de regresie nu se face cu o singură metrică, ci prin combinarea **indicatorilor numerici**, a **graficelor de diagnosticare** și a **analizei critice** a rezultatelor.
