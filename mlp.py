import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, silhouette_score

df = pd.read_csv('output_4.csv')

X = df.drop('label', axis=1)

#drop the feature for url features
# X =df.drop('-' ,axis= 1)
# X =df.drop('@' ,axis= 1)
# X =df.drop('~' ,axis= 1)
# X =df.drop('_' ,axis= 1)
# X =df.drop('%' ,axis= 1)
# X =df.drop('?' ,axis= 1)
# X =df.drop('&' ,axis= 1)
# X =df.drop('#' ,axis= 1)
# X =df.drop('urlength' ,axis= 1)

#drop the feature for HTML content features
# X =df.drop('digitnum' ,axis= 1)
# X =df.drop('sensitivenum' ,axis= 1)
# X =df.drop('hostlength' ,axis= 1)
# X =df.drop('querylength' ,axis= 1)
# X =df.drop('registrar' ,axis= 1)
# X =df.drop('state' ,axis= 1)
# X =df.drop('emptyHTML' ,axis= 1)
# X =df.drop('javascript' ,axis= 1)
# X =df.drop('hrefs_empty_cnt' ,axis= 1)
# X =df.drop('hrefs_jsFunc_cnt' ,axis= 1)
# X =df.drop('hrefs_relative_cnt' ,axis= 1)
# X =df.drop('hrefs_external_cnt' ,axis= 1)
# X =df.drop('eval_cnt' ,axis= 1)
# X =df.drop('exec_cnt' ,axis= 1)
# X =df.drop('search_cnt' ,axis= 1)
# X =df.drop('duration' ,axis= 1)


y = df['label']

#scaler data to small region
scaler = StandardScaler()
X['urlength'] = scaler.fit_transform(X[['urlength']])
X['digitnum'] = scaler.fit_transform(X[['digitnum']])
X['hostlength'] = scaler.fit_transform(X[['hostlength']])
X['querylength'] = scaler.fit_transform(X[['querylength']])
X['state'] = scaler.fit_transform(X[['state']])
X['registrar'] = scaler.fit_transform(X[['registrar']])
X['hrefs_external_cnt'] = scaler.fit_transform(X[['hrefs_external_cnt']])
X['duration'] = scaler.fit_transform(X[['duration']])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)

print(classification_report(y_test, y_pred,zero_division=1))