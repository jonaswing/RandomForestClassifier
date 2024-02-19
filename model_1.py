import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Import dataset
data = pd.read_csv('updated_water_potability.csv')
data = pd.DataFrame(data)


# CLASSIFICATION MODEL

# Choose target to predict for classification
X = data.drop('Potability', axis=1)
y = data['Potability']

# Split into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
predictions_classification = model.predict(X_test)

# Evaluate the model
accuracy_classification = accuracy_score(y_test, predictions_classification)
print("Accuracy classification potability:", accuracy_classification)
print("Accuracy classification potability: {}%".format(round(accuracy_classification * 100)))

