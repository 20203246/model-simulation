from sklearn.datasets import load_iris
from sklearn.linear_model import RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
X, y = load_iris(return_X_y=True)
print(type(X))
X_train, X_test, Y_train,Y_test = train_test_split(X,y,test_size=0.2)
model = AdaBoostClassifier(DecisionTreeClassifier(),n_estimators=800).fit(X_train,Y_train)
print(model.score(X_test,Y_test))