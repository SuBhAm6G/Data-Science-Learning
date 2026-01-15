import numpy as np
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson

# --- 1. Create Autocorrelated Data ---
# e_t depends heavily on e_{t-1} (Positive Autocorrelation)
errors = [1.0]
for t in range(1, 20):
    errors.append(0.8 * errors[t-1] + np.random.normal(0, 0.2))

print([round(t,3) for t in errors])
# --- 2. Run Test ---
# The input is just the array of residuals
dw_stat=durbin_watson(errors)
print(f"Durbin-Watson Statistic: {dw_stat:.4f}")

if dw_stat<1.5:
    print("Result: Positive Autocorrelation detected.")
elif dw_stat>2.5:
    print("Result: Negative Autocorrelation detected.")
else:
    print("Result: No significant autocorrelation.")
    