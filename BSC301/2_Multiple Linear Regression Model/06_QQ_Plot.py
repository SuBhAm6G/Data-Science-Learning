import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# --- 1. Generate Non-Normal Residuals ---
# Using an Exponential distribution (highly skewed)
residuals = np.random.exponential(scale=1.0, size=100)

# --- 2. Shapiro-Wilk Test ---
# H0: Distribution is Normal
shapiro_stat, p_value = stats.shapiro(residuals)

print(f"Shapiro Statistic: {shapiro_stat:.4f}")
print(f"P-Value: {p_value:.10f}")

if p_value < 0.05:
    print("Result: Reject H0. Residuals are NOT Normal.")
else:
    print("Result: Fail to reject H0. Residuals look Normal.")

# --- 3. Q-Q Plot ---
# Visual check against a theoretical Normal line
plt.figure(figsize=(6, 4))
stats.probplot(residuals, dist="norm", plot=plt)
plt.title("Q-Q Plot of Residuals")
plt.show()

# Observe how the blue dots curve away from the red line.