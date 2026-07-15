import pickle
from sklearn.tree import DecisionTreeClassifier

# sample data
X = [[50000, 200000, 1],
     [20000, 100000, 0],
     [30000, 150000, 1],
     [10000, 50000, 0]]

y = [1, 1, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("model.pkl created successfully")