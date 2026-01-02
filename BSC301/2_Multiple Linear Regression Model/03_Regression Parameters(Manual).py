import numpy as np
from scipy import stats

# --- 1. Data Setup ---
# X: [Intercept, Study_Hours]
X = np.array([
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5]
])
Y = np.array([2, 4, 5, 4, 5]) # Scores
n,k=X.shape

# --- 2. Calculate Beta (OLS) ---
# Formula: (X'X)^-1 X'Y
XtX_inv=np.linalg.inv(X.T @ X)
Beta_hat=XtX_inv @ X.T @ Y

# --- 3. Calculate Variance of Beta ---
# Step A: Get Residuals (e = Y - Y_hat)
Y_hat=X @ Beta_hat
residuals=Y - Y_hat

# Step B: Calculate Unbiased Estimator of Error Variance (s^2)
# s^2 = SSE / (n - k)
SSE=np.sum(np.square(residuals))
s2=SSE/(n-k)

# Step C: Variance-Covariance Matrix of Beta
# Var(Beta) = s^2 * (X'X)^-1
Var_Beta=s2*(XtX_inv)
SE_Beta=np.sqrt(np.diag(Var_Beta)) #Matrix

# T-statistics = Beta / SE
t_stat=Beta_hat/SE_Beta #Matrix

print(f"Coefficients: {Beta_hat}")
print(f"Standard Errors: {SE_Beta}")
print(f"T-statistics: {t_stat}")

# Check significance (Critical t for alpha=0.05, df=3 is approx 2.18)
is_significant=np.abs(t_stat)>2.18
print(f"Significant Coefficients (alpha=0.05): {is_significant}")
