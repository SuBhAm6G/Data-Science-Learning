import numpy as np
import pandas as pd
import statsmodels.api as sm
# --- 1. Data Setup ---
# 2 Predictors (X), 2 Targets (Y)
data = {
    'Study': [1, 2, 3, 4, 5],
    'Sleep': [8, 7, 6, 5, 4],     # Predictors
    'Math_Score': [40, 50, 55, 62, 68],  # Target 1
    'Phys_Score': [38, 48, 58, 60, 70]   # Target 2 (Highly correlated with Math)
}
df=pd.DataFrame(data)
X=df[['Study','Sleep']]
X=sm.add_constant(X)
Y=df[['Math_Score','Phys_Score']]
# --- 2. Fit Multivariate Model ---
# In statsmodels, we can just pass the DataFrame Y
# This is technically fitting 2 separate OLS models, but the object allows MANOVA testing
model=sm.OLS(Y,X).fit()

# --- 3. View Parameters ---
print("Coefficient Matrix B (3x2):")
print(model.params)
# Column 0: Betas for Math_Score
# Column 1: Betas for Phys_Score