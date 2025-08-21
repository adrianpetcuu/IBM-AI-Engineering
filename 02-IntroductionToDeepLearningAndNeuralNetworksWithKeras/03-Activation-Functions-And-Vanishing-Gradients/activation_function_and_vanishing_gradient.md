# 📘 Vanishing Gradient & Activation Functions

## 🔹 Vanishing Gradient

### ✅ Ce este?
- **Problema vanishing gradient** apare atunci când **valorile gradientului devin extrem de mici** în timpul backpropagation.  
- Aceasta face ca **straturile inițiale ale rețelei neuronale să învețe foarte greu sau aproape deloc**.  

---

### ✅ Cum apare?
1. În rețele adânci (cu multe straturi), la fiecare pas de backpropagation gradientul este **înmulțit cu valori < 1**.  
2. După mai multe înmulțiri, gradientul devine **aproape zero**.  
3. Astfel, **actualizarea greutăților din straturile timpurii (aproape de input) încetinește** drastic.  

---

### ✅ Exemple de funcții afectate
- **Sigmoid** → gradient mic pentru valori mari pozitive sau negative.  
- **Tanh** → similar, gradient mic pentru valori extreme.  

---

### ✅ Consecințe
- Straturile din față învață foarte încet.  
- Modelul converge greu și poate avea o **acuratețe scăzută**.  

---

### ✅ Soluții
- Folosirea altor funcții de activare:
  - **ReLU (Rectified Linear Unit)** → menține gradient constant pentru valori pozitive.  
  - **Leaky ReLU** → reduce problema neuronilor „morți”.  
- **Batch Normalization** → normalizează activările și reduce scăderea gradientului.  
- Optimizatori mai buni: **Adam, RMSProp**.  

---

---

## 🔹 Activation Functions (Funcții de activare)

### ✅ Ce sunt?
- Funcțiile de activare introduc **non-liniaritate** în rețele neuronale.  
- Ele decid dacă un neuron trebuie să fie activat sau nu, permițând rețelelor să învețe **relații complexe**.  

---

### ✅ Tipuri principale

1. **Sigmoid Function**
   \[
   \sigma(x) = \frac{1}{1 + e^{-x}}
   \]
   - Transformă valorile între **0 și 1**.  
   - Utilă pentru probleme de **clasificare binară**.  
   - ❌ Dezavantaj: suferă de **vanishing gradient**.

---

2. **Hyperbolic Tangent (tanh)**
   \[
   \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
   \]
   - Output între **-1 și 1**.  
   - Mai bună decât sigmoid (simetrică față de origine).  
   - ❌ Totuși, și ea poate cauza **vanishing gradient**.  

---

3. **ReLU (Rectified Linear Unit)**
   \[
   f(x) = \max(0, x)
   \]
   - Output: **0 pentru valori negative**, **x pentru valori pozitive**.  
   - ✅ Avantaj: **evită vanishing gradient** pentru valori pozitive.  
   - ❌ Problemă: „neuroni morți” pentru valori negative.  

---

4. **Leaky ReLU**
   \[
   f(x) = \begin{cases} x & x > 0 \\ \alpha x & x \leq 0 \end{cases}
   \]
   - Mică pantă (α) pentru valori negative.  
   - ✅ Evită problema neuronilor morți.  

---

5. **Softmax**
   \[
   \text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}
   \]
   - Normalizează output-ul astfel încât suma să fie **1**.  
   - ✅ Utilizată în **stratul de ieșire** pentru probleme de **clasificare multi-clasă**.  

---

### ✅ Concluzie
- **Sigmoid / Tanh** → simple, dar predispun la vanishing gradient.  
- **ReLU / Leaky ReLU** → preferate pentru straturile ascunse (hidden layers).  
- **Softmax** → obligatorie pentru stratul de ieșire în clasificare multi-class.  
