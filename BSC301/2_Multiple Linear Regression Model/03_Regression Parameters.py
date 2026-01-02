import numpy as np
import statsmodels.api as sm
import pandas as pd

# --- 1. Data Setup ---
# Let's use a clear example: Predicting Exam Score based on Study Hours
data = {
    'Study_Hours': [1, 2, 3, 4, 5],
    'Score':       [2, 4, 5, 4, 5]
}
df = pd.DataFrame(data)

# Define X (Predictor) and Y (Target)
X = df['Study_Hours']
Y = df['Score']

# CRITICAL STEP: Add the Intercept constant (Beta_0) manually
# Statsmodels requires you to explicitly add the column of 1s
X = sm.add_constant(X)

# --- 2. Fit the OLS Model ---
# This one line handles all the matrix math, inverse, and variance calculations
model = sm.OLS(Y, X).fit()

# --- 3. Get the "Module" Solution ---

# A. The Summary Table (The "All-in-One" Report)
print(model.summary())

# B. Accessing Specific Values Programmatically
print("\n" + "="*30)
print("SPECIFIC VALUES (Programmatic Access):")
print(f"Coefficients (Beta):    \n{model.params}")
print(f"Standard Errors (SE):   \n{model.bse}")
print(f"T-Statistics (t-ratio): \n{model.tvalues}")
print(f"P-Values:               \n{model.pvalues}")
print(f"95% Confidence Intervals:\n{model.conf_int()}")