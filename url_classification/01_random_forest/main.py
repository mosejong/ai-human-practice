import numpy as np
import pandas as pd
from randomforest_comparison.read import load_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
import matplotlib.pyplot as plt

X,y,X_test = load_data()

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size= 0.2, random_state=42)
'''
model_1 = LogisticRegression(max_iter=1000)
model_1.fit(X_train,y_train)
pred_1 = model_1.predict(X_valid)

model_2 = SVC()
model_2.fit(X_train,y_train)
pred_2 = model_2.predict(X_valid)

model_3 = GaussianNB()
model_3.fit(X_train,y_train)
pred_3 = model_3.predict(X_valid)

model_4 = KNeighborsClassifier()
model_4.fit(X_train,y_train)
pred_4 = model_4.predict(X_valid)

print("accuracy:", accuracy_score(y_valid, pred_1))
print("precision:", precision_score(y_valid, pred_1))
print("recall:", recall_score(y_valid, pred_1))
print("f1:", f1_score(y_valid, pred_1))
'''
model_rf = RandomForestClassifier(random_state=42, n_estimators=100)
model_rf.fit(X_train, y_train)

importance_df = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model_rf.feature_importances_
})

importance_df = importance_df.sort_values(by='importance', ascending=False)

print(importance_df)

plt.figure(figsize=(8, 6))
plt.barh(importance_df['feature'], importance_df['importance'])
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance')
plt.show()

pred_rf = model_rf.predict(X_valid)

'''
model_rf_2 = RandomForestClassifier(n_estimators=200, random_state=42)
model_rf_2.fit(X_train, y_train)
pred_rf_2 = model_rf_2.predict(X_valid)


model_rf_3 = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
model_rf_3.fit(X_train, y_train)
pred_rf_3 = model_rf_3.predict(X_valid)
'''

print("RF n=100")
print("accuracy:", accuracy_score(y_valid, pred_rf))
print("precision:", precision_score(y_valid, pred_rf))
print("recall:", recall_score(y_valid, pred_rf))
print("f1:", f1_score(y_valid, pred_rf))

'''
print('-------------------------------')

print("RF n=200")
print("accuracy:", accuracy_score(y_valid, pred_rf_2))
print("precision:", precision_score(y_valid, pred_rf_2))
print("recall:", recall_score(y_valid, pred_rf_2))
print("f1:", f1_score(y_valid, pred_rf_2))

print('-------------------------------')

print("RF n=200 depth=10")
print("accuracy:", accuracy_score(y_valid, pred_rf_3))
print("precision:", precision_score(y_valid, pred_rf_3))
print("recall:", recall_score(y_valid, pred_rf_3))
print("f1:", f1_score(y_valid, pred_rf_3))
'''





'''
sample_submission = pd.read_csv('./data/sample_submission.csv')
test_pred = model_rf.predict_proba(X_test)[:, 1]
sample_submission['probability'] = test_pred
sample_submission.to_csv('submission.csv', index=False)
'''

'''
- n_estimators를 100에서 200으로 증가시켰지만 성능 변화는 거의 없었다.
  → 일정 수준 이상의 트리 개수에서는 성능 향상이 크지 않음을 확인했다.

- max_depth=10으로 제한했을 때 accuracy, precision, recall, f1 score 모두 감소하였다.
  → 특히 recall이 크게 감소하여 모델이 실제 양성을 놓치는 경우가 증가했다.

- 이는 트리 깊이 제한으로 인해 모델의 표현력이 부족해져 과소적합(underfitting)이 발생한 것으로 해석된다.

- 따라서 RandomForest에서는 적절한 깊이 설정이 중요하며,
  무조건 제한한다고 해서 성능이 좋아지는 것은 아니다.
  '''