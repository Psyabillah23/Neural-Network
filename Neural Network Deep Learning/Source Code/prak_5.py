# -*- coding: utf-8 -*-
"""PRAK 5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tEO-BfGjwVSvk37Agm-ls0lpQMq1wFm0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold, cross_val_score , cross_validate
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import warnings
import missingno as msno
from scipy import stats

df_raw = pd.read_csv("final_test.csv")
print('Shape of the Dataset =', df_raw.shape)
df_raw.info()
df_raw.head()

# Handling missing values
df_raw['age'] = df_raw['age'].fillna(df_raw['age'].median())
df_raw['height'] = df_raw['height'].fillna(df_raw['height'].median())

df_raw['size'] = df_raw['size'].map({
    "XXS": 1,
    "S": 2,
    "M": 3,
    "L": 4,
    "XL": 5,
    "XXL": 6,
    "XXXL": 7
})

# Last check for missing values
msno.matrix(df_raw)

X = df_raw[['weight', 'age', 'height']]
y = df_raw['size']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)

# K-fold cross-validation with multiple metrics
cv_scores = cross_validate(mlp, X_train_scaled, y_train, cv=5,scoring=('accuracy', 'f1_weighted', 'precision_weighted', 'recall_weighted'))

# Extract the cross-validation scores
cv_accuracy = cv_scores['test_accuracy']
cv_f1 = cv_scores['test_f1_weighted']
cv_precision = cv_scores['test_precision_weighted']
cv_recall = cv_scores['test_recall_weighted']

# Print the cross-validation results
print('Cross-Validation Results for MLP Classifier')
print('Accuracy Scores:', cv_accuracy)
print('F1 Scores:', cv_f1)
print('Precision Scores:', cv_precision)
print('Recall Scores:', cv_recall)

# Mean scores across all folds
print('Mean Accuracy:', np.mean(cv_accuracy))
print('Mean F1 Score:', np.mean(cv_f1))
print('Mean Precision:', np.mean(cv_precision))
print('Mean Recall:', np.mean(cv_recall))

# Training the MLP Classifier
history = mlp.fit(X_train_scaled, y_train)

# Prediction
y_pred = mlp.predict(X_test_scaled)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred)}")

# Plotting training vs validation loss
plt.plot(mlp.loss_curve_, label='Training Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper left')
plt.show()

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

# Define the MLP model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape=(X_train_scaled.shape[1],)))
model.add(Dense(1, activation='softmax'))  # Gunakan 'softmax' jika lebih dari 2 kelas

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Ganti loss jika multi-class

# Fit the model and capture history
history = model.fit(X_train_scaled, y_train, epochs=100, validation_split=0.1, verbose=0)

# Plotting the learning curve
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss', color='blue')
plt.plot(history.history['val_loss'], label='Validation Loss', color='orange')
plt.title('Learning Curve')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(loc='upper left')
plt.grid()
plt.show()