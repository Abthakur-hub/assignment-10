import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("heart.csv")

# Display first five records
print("\nFirst Five Records:\n")
print(df.head())

# Display numerical features
print("\nNumerical Features:")
print(df.select_dtypes(include=["int64", "float64"]).columns.tolist())

# Target variable
print("\nTarget Variable: target")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Split features and target
X = df.drop("target", axis=1)
y = df["target"]

# Train-test split (80:20)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "model.pkl")

print("\nModel saved successfully as model.pkl")