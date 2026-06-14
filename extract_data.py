import pandas as pd
import numpy as np
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Read dataset
df = pd.read_csv("data.csv.csv")

# Drop Loan_ID
df.drop("Loan_ID", axis=1, inplace=True)

# Missing values handling
num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include="object").columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Label encoding
label_encoders = {}
mappings = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
    mappings[col] = list(le.classes_)

# Features and target
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

# Print mappings
print("LABEL MAPPINGS:")
for col, classes in mappings.items():
    print(f"  {col}: {classes}")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model check
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train_scaled, y_train)
train_acc = knn.score(X_train_scaled, y_train)
test_acc = knn.score(X_test_scaled, y_test)
print(f"\nModel Check:")
print(f"  Train Accuracy: {train_acc*100:.2f}%")
print(f"  Test Accuracy: {test_acc*100:.2f}%")

# Save values to JSON
model_data = {
    "columns": X.columns.tolist(),
    "categorical_columns": cat_cols.tolist(),
    "numeric_columns": num_cols.tolist(),
    "label_mappings": mappings,
    "scaler_mean": scaler.mean_.tolist(),
    "scaler_scale": scaler.scale_.tolist(),
    "X_train_scaled": X_train_scaled.tolist(),
    "y_train": y_train.tolist()
}

with open("knn_data.json", "w") as f:
    json.dump(model_data, f, indent=2)

print("\nModel data exported successfully to knn_data.json!")
