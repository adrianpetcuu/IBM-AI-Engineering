# 🧪 Pipelines & GridSearchCV + Data Leakage (pe scurt, fără cod)

## 1) De ce **Pipeline**?
Un *pipeline* leagă mai mulți pași de preprocesare și modelare într-un singur obiect antrenabil:
- **Consecvență**: aceiași pași aplicați la train se aplică identic și la test.
- **Fără scurgeri (data leakage)**: transformările sunt învățate **numai pe setul de train**.
- **Reproductibilitate**: un singur `.fit()` → tot lanțul (scaler, reduceri de dim., model).
- **Tuning ușor**: hiperparametrii oricărui pas pot fi optimizați prin GridSearchCV.

### Pași tipici într-un pipeline de clasificare
1. **Standardizare** (ex. `StandardScaler`) – pune feature-urile pe aceeași scară.
2. **Reducerea dimensionalității** (ex. `PCA`) – comprimă informația, reduce zgomotul.
3. **Modelul** (ex. `KNeighborsClassifier`, SVM, Logistic Regression etc.).

> Notă: în pipeline, hiperparametrii se adresează cu prefixul numelui pasului  
> (ex.: `pca__n_components`, `knn__n_neighbors`).

---

## 2) De ce **GridSearchCV**?
**GridSearchCV** caută combinația optimă de hiperparametri folosind **cross-validation**:
- **Separă** validarea de setul de test → evită supraînvățarea pe test.
- **Scor robust**: media pe fold-uri (ex. `StratifiedKFold` pentru clase echilibrate pe fold).
- **Rezultate replicabile** cu `random_state` și `shuffle=True` (unde are sens).

### Elemente cheie
- **`param_grid`**: dicționar cu alegerile de testat (ex.: `{'pca__n_components':[2,3], 'knn__n_neighbors':[3,5,7]}`).
- **`cv`**: strategia de cross-validare (ex.: `StratifiedKFold(n_splits=5)`).
- **`scoring`**: metrica (ex.: `accuracy`, `f1_macro`, `roc_auc_ovr`).
- **`best_params_` / `best_score_`**: hiperparametrii și scorul câștigător pe CV.

---

## 3) Evaluarea finală
- **Antrenezi** GridSearchCV pe **train** (cu CV intern).
- **Evaluezi** modelul *cel mai bun* pe **setul de test** (niciodată folosit în CV).
- **Confusion Matrix**: verifici erorile pe clase (TP, TN, FP, FN).
  - Din ea poți deriva: **precision**, **recall**, **F1**, **specificitate** etc.

---

## 4) Data leakage (scurgeri de informație)

### Ce este?
Modelul „vede” informații din viitor sau din test în timpul antrenării.  
Consecință: scoruri „magice” în validare, dar prăbușire pe date reale.

### Cauze comune
- **Fit pe întregul set** pentru transformări (scaler/PCA/selector) înainte de split.
- Feature-uri care **conțin targetul** sau derivate directe ale lui.
- **Agregări temporale** care folosesc date viitoare (în time series).
- „*Target encoding*” făcut greșit, fără CV intern.
- **Scurgeri pe rute de date** (îmbinări/join-uri care trag etichete viitoare).

### Cum previi leakage-ul?
- Folosește **Pipeline** – transformările fac `.fit()` doar pe **train** în fiecare fold.
- **Split corect cronologic** pentru time series (fără amestecarea viitorului).
- Verifică **feature-urile suspecte** (post-event info, etichete, variabile „oracol”).
- Fă **validări realiste** (ex. `StratifiedKFold`, `TimeSeriesSplit`).
- Păstrează **setul de test** neatins până la final.

---

## 5) Recomandări practice

- **Standardizează** înainte de KNN/SVM/PCA; în pipeline se face corect.
- **Stratifică** la `train_test_split` pentru clase echilibrate pe train/test.
- Alege `scoring` în funcție de problemă:
  - dezechilibru → **`f1_macro`**, **`balanced_accuracy`**,
  - ranking/ROC → **`roc_auc`** (bin) / **`roc_auc_ovr`** (multi-clasă).
- **Salvează** pipeline-ul final (ex. cu `joblib`) – îl poți folosi direct în producție.
- **Interpretează** `best_params_` și învață din el (ex. PCA cu 2 vs. 3 componente, K=5 vs. 7).

---

## 6) Ce trebuie să știi pentru examen/interviu

- **Pipeline** = lanț sigur de preprocesare + model, previne leakage.
- **GridSearchCV** = căutare pe grilă cu **cross-validation**; nu folosește testul.
- **StratifiedKFold** = împarte păstrând proporția claselor pe fiecare fold.
- **Confusion matrix** = instrumentul de bază pentru a vedea tiparul de erori.
- **Data leakage** = cel mai periculos pitfall; rezolvare: pipeline + split corect + CV potrivit.