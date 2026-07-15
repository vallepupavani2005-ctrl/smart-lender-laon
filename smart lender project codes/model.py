import pandas as pd

# Load dataset
df = pd.read_csv("loan.csv")

# Display first 5 rows
print(df.head())

# Display dataset shape
print("Shape:", df.shape)

# Display column names
print("Columns:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Fill numerical missing values with mean
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())

# Fill categorical missing values with mode
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0])
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

print("\nMissing Values After Filling:")
print(df.isnull().sum())
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])
df['Married'] = le.fit_transform(df['Married'])
df['Dependents'] = le.fit_transform(df['Dependents'])
df['Education'] = le.fit_transform(df['Education'])
df['Self_Employed'] = le.fit_transform(df['Self_Employed'])
df['Property_Area'] = le.fit_transform(df['Property_Area'])
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])

print("\nEncoded Data:")
print(df.head())
df = df.drop('Loan_ID', axis=1)
print(df.columns)
# Features and Target
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

print("X Shape:", X.shape)
print("y Shape:", y.shape)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dt = DecisionTreeClassifier()

dt.fit(X_train, y_train)

pred_dt = dt.predict(X_test)

print("Decision Tree Accuracy:",
      accuracy_score(y_test, pred_dt))
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=42)

rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

print("Random Forest Accuracy:",
      accuracy_score(y_test, pred_rf))
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

pred_knn = knn.predict(X_test)

print("KNN Accuracy:",
      accuracy_score(y_test, pred_knn))
from xgboost import XGBClassifier

xgb = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss'
)

xgb.fit(X_train, y_train)

pred_xgb = xgb.predict(X_test)

print("XGBoost Accuracy:",
      accuracy_score(y_test, pred_xgb))
import pickle

pickle.dump(rf, open("loan_model.pkl", "wb"))
import pickle

pickle.dump(rf, open("loan_model.pkl", "wb"))

print("Model Saved Successfully!")
import pickle

pickle.dump(rf, open("loan_model.pkl", "wb"))

print("Model Saved Successfully!")