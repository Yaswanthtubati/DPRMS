#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("dataset.csv")
data = np.array(data)

X = data[1:, 1:-1]
y = data[1:, -1]
y = y.astype('int')
X = X.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)

inputt=[int(x) for x in "45 32 60".split(' ')]
final=[np.array(inputt)]

b = log_reg.predict_proba(final)


pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")

data = pd.read_csv("Forest_fire.csv")

X = data.iloc[:, 1:6].values
y = data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Create and train the Random Forest classifier
random_forest = RandomForestClassifier()
random_forest.fit(X_train, y_train)

# Dump the trained Random Forest model into a pickle file
pickle.dump(random_forest, open('randomForest.pkl', 'wb'))
#model=pickle.load(open('randomForest.pkl','rb'))

