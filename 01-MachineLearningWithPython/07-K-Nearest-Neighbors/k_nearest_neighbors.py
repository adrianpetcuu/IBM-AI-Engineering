import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv')
print(df.head())

print(df['custcat'].value_counts())

correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.show()

correlation_values = abs(df.corr()['custcat'].drop('custcat')).sort_values(ascending=False)
print(correlation_values)

X = df.drop('custcat', axis=1)
y = df['custcat']

X_norm = StandardScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2, random_state=4)

k = 3
# train model and predict
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_model = knn_classifier.fit(X_train, y_train)

yhat = knn_model.predict(X_test)

print("k = 3 => Test set Accuracy: ", accuracy_score(y_test, yhat))

# build model with k = 6
k = 6
knn_model_6 = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
yhat6 = knn_model_6.predict(X_test)
print('k = 6 => Test set Accuracy: ', accuracy_score(y_test, yhat))

# choosing the correct value of k
Ks = 10
acc = np.zeros((Ks))
std_acc = np.zeros((Ks))
for n in range(1, Ks+1):
    # train model and predict
    knn_model_n = KNeighborsClassifier(n_neighbors=n).fit(X_train, y_train)
    yhat = knn_model_n.predict(X_test)
    acc[n-1] = accuracy_score(y_test, yhat)
    std_acc[n-1] = np.std(yhat==y_test) / np.sqrt(yhat.shape[0])

plt.plot(range(1, Ks+1), acc, 'g')
plt.fill_between(range(1, Ks+1), acc - 1 * std_acc, acc + 1 * std_acc, alpha = 0.10)
plt.legend(('Accuracy value', 'Standard Deviation'))
plt.ylabel('Model Accuracy')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()

print('The best accuracy was with', acc.max(), "with k = ", acc.argmax() + 1)

# training set for 100 value of Ks
Ks = 100
acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))
for n in range(1, Ks):
    # train model and predict
    knn_model_n = KNeighborsClassifier(n_neighbors=n).fit(X_train, y_train)
    yhat = knn_model_n.predict(X_train)
    acc[n-1] = accuracy_score(y_train, yhat)
    std_acc[n-1] = np.std(yhat==y_train) / np.sqrt(yhat.shape[0])

plt.plot(range(1, Ks), acc, 'g')
plt.fill_between(range(1, Ks), acc - 1 * std_acc, acc + 1 * std_acc, alpha = 0.10)
plt.legend(('Accuracy value', 'Standard Deviation'))
plt.ylabel('Model Accuracy')
plt.xlabel('Number ofm Neighbors (K)')
plt.tight_layout()
plt.show()