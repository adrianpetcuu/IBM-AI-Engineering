# Fișă de sinteză: Modele de Învățare Supravegheată

## Modele comune de învățare supravegheată

| Model | Descriere                                                                       | Avantaje (Pros) | Dezavantaje (Cons) | Aplicații comune | Cod Python                                                                                                                                                                                                                                                                                                                               |
|---|---------------------------------------------------------------------------------|---|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **One vs One Classifier** (folosind regresie logistică) | Antrenează un clasificator pentru fiecare pereche de clase.                     | Funcționează bine pentru seturi mici de date. | Consum mare de resurse pentru seturi mari. | Clasificare multiclasa cu puține clase. | ```python<br/>from sklearn.multiclass import OneVsOneClassifier<br>from sklearn.linear_model import LogisticRegression<br><br>model = OneVsOneClassifier(LogisticRegression())<br>```                                                                                                                                                         |
| **One vs All Classifier** (folosind regresie logistică) | Antrenează un clasificator per clasă, fiecare distingând între o clasă și restul. | Mai simplu și mai scalabil decât One vs One. | Mai puțin precis pentru clase dezechilibrate. | Clasificare multiclasa (ex. clasificare imagini). | ```python<br>from sklearn.multiclass import OneVsRestClassifier<br>from sklearn.linear_model import LogisticRegression<br><br>model = OneVsRestClassifier(LogisticRegression())<br>``` <br> **sau** <br> ```python<br>from sklearn.linear_model import LogisticRegression<br><br>model_ova = LogisticRegression(multi_class='ovr')<br>``` |
| **Clasificator cu arbori de decizie** | Arbore care împarte datele în subseturi mai mici după valorile caracteristicilor. | Ușor de interpretat și vizualizat. | Predispus la overfitting dacă nu este tăiat (pruned). | Clasificare (ex. evaluare risc de credit). | ```python<br>from sklearn.tree import DecisionTreeClassifier<br><br>model = DecisionTreeClassifier(max_depth=5)<br>```                                                                                                                                                                                                                   |
| **Regresor cu arbori de decizie** | Similar cu clasificatorul pe arbori de decizie, dar pentru valori continue.     | Ușor de interpretat, captează relații neliniare. | Poate overfitta și performa slab pe date zgomotoase. | Regresie (ex. predicția prețurilor locuințelor). | ```python<br>from sklearn.tree import DecisionTreeRegressor<br><br>model = DecisionTreeRegressor(max_depth=5)<br>```                                                                                                                                                                                                                     |
| **Linear SVM Classifier** | Clasificator liniar care găsește hiperplanul optim ce separă clasele cu marjă maximă. | Eficient pentru seturi de date cu multe dimensiuni. | Nu este ideal pentru probleme neliniare fără kernel tricks. | Clasificare text, recunoaștere imagini. | ```python<br>from sklearn.svm import SVC<br><br>model = SVC(kernel='linear', C=1.0)<br>``` |
| **K-Nearest Neighbors Classifier (KNN)** | Clasifică datele pe baza majorității claselor vecinilor cei mai apropiați. | Simplu și eficient pentru seturi mici de date. | Costisitor computațional pentru seturi mari. | Sisteme de recomandare, recunoaștere imagini. | ```python<br>from sklearn.neighbors import KNeighborsClassifier<br><br>model = KNeighborsClassifier(n_neighbors=5, weights='uniform')<br>``` |
| **Random Forest Regressor** | Metodă ensemble ce folosește mai mulți arbori de decizie pentru a crește acuratețea și a reduce overfitting-ul. | Mai puțin predispus la overfitting decât arborii individuali. | Complexitatea crește odată cu numărul de arbori. | Regresie: predicții vânzări, prețuri acțiuni. | ```python<br>from sklearn.ensemble import RandomForestRegressor<br><br>model = RandomForestRegressor(n_estimators=100, max_depth=5)<br>``` |
| **XGBoost Regressor** | Gradient boosting ce construiește arbori secvențial pentru a corecta erorile anterioare. | Acuratețe ridicată, performant pe seturi mari. | Computațional intens și dificil de reglat. | Modelare predictivă (foarte folosit în competițiile Kaggle). | ```python<br>import xgboost as xgb<br><br>model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)<br>``` |

# Fișă de sinteză: Funcții asociate în Învățarea Supravegheată

## Funcții / metode frecvent utilizate

| Funcție / Metodă | Descriere | Cod Python |
|---|---|---|
| **OneHotEncoder** | Transformă variabilele categorice în matrice one-hot encoded. | ```python<br>from sklearn.preprocessing import OneHotEncoder<br><br>encoder = OneHotEncoder(sparse=False)<br>encoded_data = encoder.fit_transform(categorical_data)<br>``` |
| **accuracy_score** | Calculează acuratețea unui clasificator comparând etichetele prezise cu cele reale. | ```python<br>from sklearn.metrics import accuracy_score<br><br>accuracy = accuracy_score(y_true, y_pred)<br>``` |
| **LabelEncoder** | Convertește etichetele (variabila țintă) în format numeric. | ```python<br>from sklearn.preprocessing import LabelEncoder<br><br>encoder = LabelEncoder()<br>encoded_labels = encoder.fit_transform(labels)<br>``` |
| **plot_tree** | Plotează un arbore de decizie pentru vizualizare. | ```python<br>from sklearn.tree import plot_tree<br><br>plot_tree(model, max_depth=3, filled=True)<br>``` |
| **normalize** | Scalează fiecare caracteristică pentru a avea medie zero și varianță unitară (standardizare). | ```python<br>from sklearn.preprocessing import normalize<br><br>normalized_data = normalize(data, norm='l2')<br>``` |
| **compute_sample_weight** | Calculează ponderi pentru eșantioane în cazul datelor dezechilibrate. | ```python<br>from sklearn.utils.class_weight import compute_sample_weight<br><br>weights = compute_sample_weight(class_weight='balanced', y=y)<br>``` |
| **roc_auc_score** | Calculează AUC (Area Under the Curve) pentru ROC în modele de clasificare binară. | ```python<br>from sklearn.metrics import roc_auc_score<br><br>roc_auc = roc_auc_score(y_true, y_score)<br>``` |


# Clasificare și Algoritmi de Învățare Supravegheată

## Clasificare
Clasificarea este o metodă de învățare supravegheată folosită pentru a prezice etichete pe date noi, cu aplicații în:
- predicția churn-ului (părăsirea clienților),
- segmentarea clienților,
- predicția neplății creditelor,
- clasificarea multiclasă (ex. prescrierea medicamentelor).

Clasificatoarele binare pot fi extinse la **clasificare multiclasă** folosind strategiile:
- *one-versus-all* (OvA),
- *one-versus-one* (OvO).

---

## Arbori de decizie
Un arbore de decizie clasifică datele prin testarea caracteristicilor la fiecare nod, ramificându-se în funcție de rezultate și atribuind clase la nodurile frunză.

### Procesul de antrenare a unui arbore de decizie:
- selectarea caracteristicilor care separă cel mai bine datele,
- *pruning* (tăierea arborelui) pentru a evita **overfitting**.

### Măsuri utilizate pentru calitatea split-urilor:
- **Information Gain**,
- **Gini impurity**.

---

## Arbori de regresie
Arborii de regresie sunt similari cu arborii de decizie, dar prezic **valori continue** prin împărțirea recursivă a datelor pentru a maximiza *information gain*.

- **Mean Squared Error (MSE)** este folosit pentru a măsura calitatea split-urilor în arborii de regresie.

---

## K-Nearest Neighbors (k-NN)
*k-NN* este un algoritm supravegheat folosit atât pentru clasificare, cât și pentru regresie.  
Funcționează prin atribuirea etichetei unui punct nou pe baza celor mai apropiați **k vecini** etichetați.

### Optimizarea k-NN:
- testarea diferitelor valori pentru `k`,
- măsurarea acurateței,
- analiza distribuției claselor și relevanței caracteristicilor.

---

## Support Vector Machines (SVM)
SVM construiește clasificatoare găsind un **hiperplan** care maximizează marginea dintre două clase.

- **Avantaje:** eficient în spații de dimensiuni mari.  
- **Dezavantaje:** sensibil la zgomot și seturi de date foarte mari.

---

## Bias-Variance Tradeoff
Echilibrul dintre bias și varianță influențează acuratețea modelului.

### Tehnici pentru reducerea biasului și varianței:
- **Bagging**,
- **Boosting**,
- **Random Forests**.

---

## Random Forests
Pădurile de arbori de decizie folosesc metoda **bagging**:  
- se antrenează mai mulți arbori de decizie pe seturi de date bootstrap,  
- predicțiile sunt combinate,  
- se obține o acuratețe mai mare prin reducerea varianței.
