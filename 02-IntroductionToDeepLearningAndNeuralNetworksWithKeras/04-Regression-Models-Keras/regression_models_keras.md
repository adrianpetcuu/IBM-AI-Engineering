# 📘 Regression Models with Keras

## 🔹 Ce este regresia?
- **Regresia** este o tehnică de învățare supravegheată folosită pentru a prezice **valori continue**.  
- Spre deosebire de clasificare (unde output-ul este o etichetă sau clasă), în regresie output-ul este numeric.  
- Exemple de probleme de regresie:
  - Prezicerea rezistenței betonului  
  - Estimarea prețului unei case  
  - Prezicerea temperaturii  

---

## 🔹 Etapele construirii unui model de regresie în Keras

### 1. Pregătirea datelor
- Încărcarea dataset-ului într-un DataFrame.  
- Verificarea formelor datelor (rânduri și coloane).  
- Tratarea valorilor lipsă (dacă există).  

### 2. Separarea datelor
- **Predictors (X)**: variabilele de intrare (feature-urile).  
- **Target (y)**: variabila pe care vrem să o prezicem (valoarea numerică continuă).  

### 3. Normalizarea datelor
- Se aplică pentru a aduce toate variabilele pe aceeași scară.  
- Ajută modelul să învețe mai repede și să evite probleme legate de convergență.  

### 4. Construirea rețelei neurale
- **Input Layer**: dimensiunea intrării este egală cu numărul de predictori.  
- **Hidden Layers**: straturi ascunse cu un număr de neuroni și funcții de activare (de obicei ReLU).  
- **Output Layer**: un singur neuron pentru a prezice valoarea numerică.  

### 5. Compilarea modelului
- **Optimizer**: Adam este cel mai folosit pentru regresie.  
- **Loss Function**: Mean Squared Error (MSE) este standard pentru probleme de regresie.  

### 6. Antrenarea modelului
- Împărțirea datelor în **set de antrenament** și **set de validare**.  
- Rularea antrenamentului pentru un număr de **epoci**.  
- Monitorizarea funcției de cost (loss) pe train și validation.  

### 7. Evaluarea modelului
- Se evaluează performanța pe un set de test.  
- Metrice comune pentru regresie:
  - **MSE** (Mean Squared Error)  
  - **RMSE** (Root Mean Squared Error)  
  - **MAE** (Mean Absolute Error)  
  - **R²** (R-squared)  

---

## 🔹 Avantaje ale folosirii Keras pentru regresie
- Cod simplu și intuitiv.  
- Posibilitatea de a construi rețele complexe cu câteva linii.  
- Integrare ușoară cu TensorFlow.  
- Suportă optimizatori și funcții de pierdere standardizate.  

---

## 🔹 Concluzie
Modelele de regresie cu Keras sunt foarte utile pentru prezicerea valorilor continue.  
Pașii principali sunt: **pregătirea datelor → normalizare → definirea rețelei → compilare → antrenare → evaluare**.  
Astfel, Keras oferă o metodă rapidă și eficientă pentru construirea de rețele neurale de regresie.
