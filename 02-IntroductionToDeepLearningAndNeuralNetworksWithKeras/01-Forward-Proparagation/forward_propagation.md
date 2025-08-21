# 📘 Introduction to Deep Learning, Neurons and Neural Networks

## 🔹 1. Introduction to Deep Learning
- Deep Learning este o ramură a Machine Learning bazată pe **rețele neuronale artificiale cu multe straturi** (Deep Neural Networks).
- Inspirat din modul în care funcționează creierul uman.
- Aplicații:
  - recunoaștere imagini
  - procesarea limbajului natural (NLP)
  - recunoaștere vocală
  - sisteme autonome (mașini self-driving)

---

## 🔹 2. Neurons and Neural Networks
- **Neuron artificial** = unitate de calcul care primește intrări, le combină cu **greutăți (weights)** și **bias**, apoi trece rezultatul printr-o **funcție de activare**.
- Structura unei rețele neuronale:
  - **Input layer** (strat de intrare)
  - **Hidden layers** (straturi ascunse)
  - **Output layer** (strat de ieșire)
- Rețelele neuronale permit modelarea **relațiilor complexe și neliniare**.

---

## 🔹 3. Artificial Neural Networks (ANN)
- O rețea neuronală artificială este formată din **neuroni conectați între straturi**.
- **Weights și bias** sunt parametrii ajustați în timpul antrenării.
- Procesul de învățare:
  1. Inițializare greutăți și bias la valori mici random.
  2. Calculul ieșirii rețelei (**Forward Propagation**).
  3. Calculul erorii față de valorile reale.
  4. Corectarea greutăților prin **Backpropagation + Gradient Descent**.

---

## 🔹 4. Forward Propagation (Detaliat)
Forward Propagation este procesul prin care datele de intrare sunt transmise prin rețea, strat cu strat, până la ieșirea finală.  

### 🔸 Pașii principali:
1. **Intrările sunt primite în stratul de input** (ex: imagine, text, date numerice).
2. **Calculul sumei ponderate pentru fiecare neuron**:
   \[
   z = sum (w_i * x_i) + b
   \]
   - `x_i` = valorile de intrare  
   - `w_i` = greutățile asociate conexiunilor  
   - `b` = bias (constanta care deplasează funcția)

3. **Aplicarea funcției de activare**:
   - Sigmoid: produce valori între 0 și 1 → utilă pentru probabilități.
   - tanh: produce valori între -1 și 1 → mai centrată în jurul originii.
   - ReLU: păstrează doar valorile pozitive → accelerează învățarea.
   - Softmax: folosită în stratul de ieșire pentru clasificare multi-clasă.

   \[
   a = f(z)
   \]
   unde `f` este funcția de activare.

4. **Transmiterea rezultatelor la stratul următor**:
   - Ieșirea fiecărui neuron devine **intrarea** neuronilor din stratul următor.
   - Acest proces se repetă pentru toate **hidden layers**.

5. **Predicția finală la Output Layer**:
   - În clasificare binară → Sigmoid.  
   - În clasificare multi-clasă → Softmax.  
   - În regresie → funcție liniară.

---

### 🔸 Exemplu simplificat:
- Input: [x1, x2]  
- Stratul ascuns calculează:
  \[
  z_1 = w_1 * x_1 + w_2 * x_2 + b
  \]
  \[
  a_1 = f(z_1)
  \]
- Output layer:
  \[
  \hat{y} = f(w * a_1 + b)
  \]

---

### 🔸 Rolul Forward Propagation:
✅ Permite **calculul predicției** pentru orice intrare.  
✅ Este prima etapă înainte de **calculul erorii** și **Backpropagation**.  
✅ Introduce **non-liniaritate** prin funcțiile de activare → esențial pentru învățarea relațiilor complexe.  

---

## ✅ Concluzie
- Deep Learning permite antrenarea de modele complexe inspirate din biologia creierului.
- Neuronii artificiali folosesc **weights + bias + funcții de activare**.
- Artificial Neural Networks se antrenează prin:
  - **Forward Propagation** → calculul predicției
  - **Backpropagation + Gradient Descent** → ajustarea greutăților.
