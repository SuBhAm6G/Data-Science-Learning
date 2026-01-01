import numpy as np
import statsmodels.api as sm
import pandas as pd

# --- 1. Create Dummy Data ---
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Attendance':  [60, 70, 75, 80, 85, 90, 92, 95],
    'Score':       [40, 50, 55, 62, 68, 72, 80, 85]
}
df=pd.DataFrame(data)

# --- 2. Define X and Y ---
X=df[['Study_Hours','Attendance']]
Y=df['Score']

# CRITICAL STEP: Add Intercept (Beta_0)
X=sm.add_constant(X) #It allows a constant shift by adding column of 1s

# --- 3. Fit OLS Model ---
model=sm.OLS(Y,X).fit()

# --- 4. Print Summary (The ANOVA Table) ---
print(model.summary())

# - R-squared: How well the model fits (0 to 1).
# - F-statistic: Is the model significantly better than nothing?
# - Coef: The Beta values.
# - P>|t|: Is a specific variable significant? (If < 0.05, yes).