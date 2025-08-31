## 5. Transformers
- Transformers sunt modele avansate pentru **secvențe de date**, în special în **procesarea limbajului natural (NLP)**.  
- În loc să proceseze datele secvențial ca RNN-urile, folosesc un mecanism numit **Self-Attention**.  
- **Self-Attention** permite modelului să acorde importanță diferită fiecărui cuvânt din propoziție, indiferent de poziția lui.  
- Avantaje:
  - procesează secvențele **în paralel** (mult mai rapid decât RNN-urile),
  - captează **relații pe termen lung** dintre elementele secvenței,
  - este foarte scalabil.  
- Exemple de modele bazate pe Transformers:
  - **BERT** (Bidirectional Encoder Representations from Transformers),
  - **GPT** (Generative Pretrained Transformer),
  - **Vision Transformers (ViT)** pentru imagini.  
- Aplicații:
  - traducere automată,
  - chatbot-uri,
  - generare text,
  - clasificare documente,
  - analiză de sentimente.  

---

## 6. Autoencoders
- Autoencoderele sunt rețele neuronale folosite pentru **compresia și reconstrucția datelor**.  
- Structura lor:
  - **Encoder** → comprimă datele într-o reprezentare mai mică (latent space).  
  - **Decoder** → reconstruiește datele originale din reprezentarea comprimată.  
- Funcționează în mod **nesupravegheat** (nu au nevoie de etichete).  
- Proprietăți:
  - sunt **data-specific** (funcționează bine pe tipuri de date pe care au fost antrenate),
  - învață să surprindă caracteristicile esențiale ale datelor.  
- Aplicații:
  - reducere de dimensiuni,
  - **denoising** (curățarea zgomotului din imagini sau date),
  - **anomaly detection** (detectarea anomaliilor),
  - generare de imagini și date noi.  
 

## 7. Pretrained Models și Transfer Learning
- **Pretrained Models** sunt rețele neuronale mari antrenate pe seturi de date vaste (ex. ImageNet, COCO, Wikipedia).  
- În loc să începem antrenarea unui model de la zero, putem folosi greutățile deja învățate și le putem adapta la problema noastră.  
- Acest proces se numește **Transfer Learning**.  

### Avantaje:
- Economisește **timp și resurse de calcul** (nu e nevoie să antrenezi milioane de parametri de la zero).  
- Oferă **performanțe mai bune pe seturi mici de date**, deoarece modelul are deja învățate caracteristici generale.  
- Reduce riscul de **overfitting**.  

### Exemple de modele pre-antrenate:
- **VGG16 / VGG19** – simple, dar foarte utilizate în clasificarea imaginilor.  
- **ResNet** – rezolvă problema gradientului dispărut prin conexiuni reziduale.  
- **Inception (GoogleNet)** – folosește multiple dimensiuni de filtre în paralel.  
- **BERT, GPT** – pentru procesarea limbajului natural.  
- **Vision Transformers (ViT)** – modele bazate pe Transformers pentru imagini.  

### Scenarii de utilizare:
- **Feature extraction** – folosim modelul pre-antrenat ca extractor de caracteristici și adăugăm un clasificator nou.  
- **Fine-tuning** – ajustăm greutățile modelului pre-antrenat prin re-antrenare pe setul nostru de date.  
- **Transfer cross-domain** – aplicăm modele antrenate pe un tip de date (ex. imagini naturale) la alt domeniu (ex. imagini medicale).  
