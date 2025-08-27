# 📘 Classification Models with Keras

## 🔹 Ce este clasificarea?
- **Clasificarea** este o tehnică de învățare supravegheată folosită pentru a prezice **categorii sau etichete**.  
- Spre deosebire de regresie (care prezice valori continue), clasificarea decide în ce **clasă** se încadrează un input.  
- Exemple de probleme de clasificare:
  - Recunoașterea imaginilor (pisică vs. câine)  
  - Detectarea emailurilor spam vs. non-spam  
  - Clasificarea recenziilor (pozitiv, negativ, neutru)  

---

## 🔹 Tipuri de clasificare
1. **Clasificare binară** – două clase (ex: 0 sau 1, adevărat sau fals).  
2. **Clasificare multi-clasă** – mai multe clase exclusive (ex: recunoaștere cifre 0–9).  
3. **Clasificare multi-label** – un input poate aparține simultan mai multor clase.  

---

## 🔹 Etapele construirii unui model de clasificare în Keras

### 1. Pregătirea datelor
- Încărcarea și curățarea dataset-ului.  
- Împărțirea datelor în **predictors (X)** și **target (y)**.  

### 2. Transformarea etichetelor (target)
- Pentru clasificare, etichetele trebuie convertite în format numeric:  
  - **Clasificare binară** → etichetele devin valori binare (0 sau 1).  
  - **Clasificare multi-clasă** → etichetele se transformă în **vectori one-hot** folosind funcția `to_categorical`.  

### 3. Construirea rețelei neurale
- **Input Layer**: dimensiunea intrării = numărul de predictori.  
- **Hidden Layers**: mai multe straturi dense, cu funcții de activare ReLU.  
- **Output Layer**:
  - Pentru **clasificare binară** → 1 neuron + activare **sigmoid**.  
  - Pentru **clasificare multi-clasă** → un neuron pentru fiecare clasă + activare **softmax**.  

### 4. Compilarea modelului
- **Optimizer**: Adam este cel mai utilizat.  
- **Loss Function**:
  - Clasificare binară → `binary_crossentropy`.  
  - Clasificare multi-clasă → `categorical_crossentropy`.  

### 5. Antrenarea modelului
- Se folosește **validation_split** sau un set separat de validare pentru a monitoriza performanța.  
- Se rulează pentru un număr de epoci, ajustând batch size și optimizer dacă e nevoie.  

### 6. Evaluarea modelului
- După antrenare, modelul se evaluează pe un set de test.  
- Metrice comune pentru clasificare:
  - **Accuracy** (acuratețe)  
  - **Precision** (precizie)  
  - **Recall** (sensibilitate)  
  - **F1-score** (echilibru între precizie și recall)  

---

## 🔹 Avantaje ale folosirii Keras pentru clasificare
- Ușor de construit și testat modele complexe.  
- Suportă funcții de activare și de pierdere standardizate.  
- Integrare rapidă cu TensorFlow pentru rulare pe CPU și GPU.  
- Posibilitatea de a monitoriza metrici precum accuracy, precision și recall în timp real.  

---

## 🔹 Concluzie
Modelele de clasificare cu Keras sunt esențiale pentru probleme unde răspunsul este o **etichetă**.  
Pașii principali sunt: **pregătirea datelor → transformarea etichetelor → definirea rețelei → compilare → antrenare → evaluare**.  
Astfel, Keras oferă o modalitate simplă și rapidă de a dezvolta modele de clasificare eficiente.
