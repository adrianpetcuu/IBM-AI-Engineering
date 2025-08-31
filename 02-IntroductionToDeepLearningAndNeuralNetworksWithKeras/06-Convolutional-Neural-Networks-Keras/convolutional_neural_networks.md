``# Shallow vs Deep Neural Networks, CNNs și RNNs

## 1. Shallow vs Deep Neural Networks
- O rețea neuronală cu **un singur strat ascuns** este numită **shallow neural network**.  
- O rețea neuronală cu **mai multe straturi ascunse** și cu un număr mare de neuroni este numită **deep neural network**.  
- Rețelele shallow funcționează mai bine pentru probleme simple.  
- Rețelele deep pot modela **relații complexe** și pot învăța direct din date brute (ex: imagini, text).  

---

## 2. Convolutional Neural Networks (CNNs)
- CNN-urile fac **presupunerea explicită că input-ul este o imagine**.  
- Sunt ideale pentru:
  - recunoaștere de imagini,
  - detecția obiectelor,
  - aplicații de **computer vision**.  
- Input-ul este de forma:
  - **(n × m × 1)** pentru imagini grayscale,
  - **(n × m × 3)** pentru imagini color.  
- Convolutional layer aplică **filtre** peste imagine pentru a extrage caracteristici.  
- ReLU layer trece mai departe doar valori pozitive.  
- Pooling layer reduce dimensiunea spațială și păstrează informațiile esențiale.  
- Fully connected layer conectează toți neuronii și trimite output către stratul final de clasificare.  

---

## 3. Convolutional Neural Networks with Keras
- În Keras, CNN-urile se construiesc adăugând straturi succesive:
  - **Conv2D** → pentru detecția caracteristicilor,
  - **MaxPooling2D / AveragePooling2D** → pentru reducerea dimensiunilor,
  - **Flatten** → transformă matricea într-un vector,
  - **Dense** → conectează straturile complet.  
- Funcția de activare frecvent folosită în straturile ascunse este **ReLU**, iar pentru stratul final în clasificare multi-clasă este **Softmax**.  
- Aceste rețele pot fi antrenate pe seturi mari de imagini și optimizează parametrii cu algoritmi precum **Adam** sau **SGD**.  

---

## 4. Recurrent Neural Networks (RNNs)
- RNN-urile procesează secvențe de date.  
- Nu primesc doar input nou, ci și **output-ul de la pasul anterior**.  
- Sunt utile pentru:
  - text și procesare limbaj natural,
  - predicția seriilor temporale,
  - recunoaștere voce și scris de mână.  
- Varianta lor îmbunătățită, **LSTM (Long Short-Term Memory)**, poate reține dependențe pe termen lung și rezolvă problema gradientului care dispare.  
- Exemple de aplicații:
  - traducere automată,
  - generare text,
  - predicția burselor,
  - descriere automată a imaginilor și videoclipurilor.  
