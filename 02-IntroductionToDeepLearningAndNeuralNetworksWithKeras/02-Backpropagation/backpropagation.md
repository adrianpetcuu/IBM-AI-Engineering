# 📘 Gradient Descent & Backpropagation

## 🔹 Gradient Descent (Algoritmul de coborâre a gradientului)

### ✅ Ce este?
- **Gradient Descent** este un **algoritm de optimizare iterativ** folosit pentru a găsi **minimum-ul unei funcții de cost** (loss function).
- Este folosit pentru **antrenarea rețelelor neuronale**, prin ajustarea **greutăților (weights)** și **biasurilor** pentru a reduce eroarea dintre predicție și adevăr.

---

### ✅ Cum funcționează?
1. **Se calculează funcția de cost (J)** → măsoară diferența între predicții și valorile reale.  
2. **Se calculează gradientul (derivata funcției de cost față de weights & bias)**.  
   - Gradientul arată **direcția creșterii erorii**.  
3. **Actualizare parametri (weights & bias)** în direcția opusă gradientului:  
   \[
   w := w - \eta \cdot \frac{\partial J}{\partial w}
   \]
   - `η` (eta) = **rata de învățare** (learning rate).  
   - `∂J/∂w` = gradientul erorii față de greutate.  

---

### ✅ Tipuri de Gradient Descent
- **Batch Gradient Descent** → folosește întreg setul de date pentru fiecare actualizare.  
- **Stochastic Gradient Descent (SGD)** → actualizează parametrii după fiecare eșantion (mai rapid, dar zgomotos).  
- **Mini-batch Gradient Descent** → compromis între cele două, folosește loturi mici de date (foarte des utilizat în deep learning).  

---

### ✅ Probleme & Soluții
- **Learning rate prea mare** → sare peste minim.  
- **Learning rate prea mic** → converge foarte lent.  
- **Local minima / saddle points** → rețeaua poate rămâne blocată.  
- Se folosesc **optimizatori avansați**: Adam, RMSProp, AdaGrad.  

---

---

## 🔹 Backpropagation (Algoritmul de propagare înapoi)

### ✅ Ce este?
- **Backpropagation** = algoritmul prin care rețeaua neuronală **învață ajustând greutățile** pe baza erorii.  
- Funcționează împreună cu **Gradient Descent**.  
- Esența: **error → backward → update weights**.  

---

### ✅ Cum funcționează?
1. **Forward Propagation**:
   - Se calculează predicția (output-ul rețelei).
   - Se compară cu **valoarea reală** → se obține **eroarea (loss)**.  

2. **Backward Propagation**:
   - Se aplică **teorema lanțului (chain rule)** pentru a calcula derivata erorii față de fiecare greutate și bias.  
   - Se obțin **gradientele pentru fiecare strat** al rețelei.  

   Exemplu simplu pentru un neuron:  
   \[
   \frac{\partial J}{\partial w} = \frac{\partial J}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}
   \]

   - `a` = activarea (ieșirea neuronului după funcția de activare).  
   - `z` = suma ponderată (w·x + b).  

3. **Actualizare parametri**:
   - Folosind regula Gradient Descent, se actualizează greutățile și biasurile.  

---

### ✅ De ce e important?
- Face posibil antrenamentul rețelelor neuronale **complexe cu multe straturi** (Deep Learning).  
- Fără backpropagation, nu am putea ajusta greutățile eficient.  
- Este cheia succesului în recunoaștere imagini, NLP, audio etc.  

---

### ✅ Probleme frecvente
- **Vanishing Gradient Problem** (mai ales cu funcții ca Sigmoid/tanh):  
  - gradientele devin extrem de mici → straturile inițiale învață foarte greu.  
  - Soluții: ReLU, Leaky ReLU, batch normalization, optimizatori avansați.  

- **Exploding Gradients** → valorile devin foarte mari → instabilitate.  
  - Soluții: gradient clipping, optimizatori avansați.  

---

## 📝 Concluzie
- **Gradient Descent** = metoda de optimizare prin care găsim greutățile potrivite pentru a minimiza eroarea.  
- **Backpropagation** = algoritmul care calculează gradientele erorii pentru fiecare parametru, astfel încât Gradient Descent să le poată actualiza.  

👉 Pe scurt:  
1. **Forward Propagation** → facem predicția  
2. **Calculăm eroarea**  
3. **Backpropagation** → calculăm gradientele  
4. **Gradient Descent** → actualizăm greutățile  
