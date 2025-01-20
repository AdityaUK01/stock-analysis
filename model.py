# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Function to train a machine learning model
def train_model(data):
    # Assuming the data is a pandas DataFrame with 'features' and 'target' columns
    features = data.drop(columns='target')  # Replace 'target' with the name of your target column
    target = data['target']  # Replace 'target' with the name of your target column

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize the model (RandomForest as an example)
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Predict on the test data
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')

    # Return the trained model for further use (like making predictions)
    return model

# Example usage:
# data = pd.read_csv('your_data.csv')
# trained_model = train_model(data)
