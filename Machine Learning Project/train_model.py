import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import numpy as np
from sklearn.decomposition import PCA

# Load the dataset
car_data_path = 'car_data.csv'  
car_data = pd.read_csv(car_data_path)

# Copy dataset for preprocessing
data = car_data.copy()

# Feature Engineering: Add the car age as a new feature
data['car_age'] = 2025 - data['year']  # Assuming the current year is 2025

# Transform km_driven to log scale to handle large values
data['km_driven'] = np.log1p(data['km_driven'])

# Check for outliers in selling_price and km_driven
# For simplicity, let's consider removing rows where selling_price is too high or too low
data = data[data['selling_price'] < 5000000]  # Example threshold for unrealistic prices
data = data[data['km_driven'] < 15]  # Example threshold for unrealistic km_driven values

# Encode all non-numeric columns
categorical_cols = data.select_dtypes(include=['object']).columns
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Define features (X) and target (y)
X = data.drop(columns=['selling_price'])
y = data['selling_price']

# Feature Scaling (Standardization)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Optionally, apply PCA for dimensionality reduction (if needed)
pca = PCA(n_components=0.95)  # Keeps 95% variance
X_pca = pca.fit_transform(X_scaled)

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

# Hyperparameter tuning using GridSearchCV for RandomForestRegressor
param_grid = {
    'n_estimators': [100, 200, 300, 400],
    'max_depth': [10, 20, 30, 40, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2']
}

# Initialize the RandomForestRegressor and GridSearchCV
rf = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)

# Fit the model with GridSearchCV
grid_search.fit(X_train, y_train)

# Get the best model from the grid search
best_model = grid_search.best_estimator_

# Evaluate the model
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)

# Save the trained model and encoders for use in Flask
model_path = 'Car_sales_model.pkl'  # Save in the current working directory
encoder_path = 'label_encoders.pkl'  # Save in the current working directory

# Save the best model and label encoders
joblib.dump(best_model, model_path)
joblib.dump(label_encoders, encoder_path)

# Output the evaluation results
print(f"Best Model Parameters: {grid_search.best_params_}")
print(f"Model saved to {model_path}")
print(f"Encoders saved to {encoder_path}")
print(f"Mean Squared Error: {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared: {r2}")
