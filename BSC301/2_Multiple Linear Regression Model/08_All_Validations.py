import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
import scipy.stats as stats
import matplotlib.pyplot as plt

# --- 1. Setup Data ---
# Simulate data with slight Heteroscedasticity (Variance increases with X)
np.random.seed(42)
X = np.linspace(1, 10, 50)
y = 3*X + np.random.normal(0, X*0.5, 50) # Noise grows with X
df = pd.DataFrame({'X': X, 'y': y})
X_const = sm.add_constant(df['X'])
print(X)
print(y)
print(X_const)

#Fit Model
model=sm.OLS(df['y'],X_const).fit()
residuals=model.resid
print("=== DIAGNOSTIC REPORT ===")

# --- Check 1: Normality (Jarque-Bera) ---
jb_stat, jb_p = stats.jarque_bera(residuals)
print(f"1. Normality (Jarque-Bera): P-val = {jb_p:.4f} "
      f"{'(Normal)' if jb_p > 0.05 else '(Non-Normal)'}")

# --- Check 2: Autocorrelation (Durbin-Watson) ---
dw = durbin_watson(residuals)
print(f"2. Autocorrelation (DW):    Stat  = {dw:.2f} "
      f"{'(Good)' if 1.5 < dw < 2.5 else '(Bad)'}")

# --- Check 3: Multicollinearity (VIF) ---
# (Only 1 variable here, so VIF is trivial, but code is generic)
vif = variance_inflation_factor(X_const.values, 1)
print(f"3. Multicollinearity (VIF): Value = {vif:.2f}")

# --- Check 4: Heteroscedasticity (Visual) ---
plt.figure(figsize=(10, 4))

# Residual vs Fitted
plt.subplot(1, 2, 1)
plt.scatter(model.fittedvalues, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs Fitted (Check Linearity/Homoscedasticity)")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")

# Q-Q Plot
plt.subplot(1, 2, 2)
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("Q-Q Plot (Check Normality)")

plt.tight_layout()
plt.show()
#Look at Plot 1: Does the spread widen like a funnel? (Yes -> Heteroscedasticity)