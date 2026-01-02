import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import OLSInfluence
# --- 1. Data with an Outlier ---
# Notice the last point (Study=5, Score=100) is crazy
df = pd.DataFrame({
    'Study': [1, 2, 3, 4, 5],
    'Score': [10, 20, 30, 40, 100] 
})
X=sm.add_constant(df['Study'])
model=sm.OLS(df['Score'],X).fit()

# # --- 2. Calculate Cook's Distance ---
# influence = OLSInfluence(model)
# (c, p) = influence.cooks_distance

# # --- 3. Plot ---
# plt.stem(df.index, c, markerfmt=",")
# plt.title("Cook's Distance Plot")
# plt.xlabel("Observation Index")
# plt.ylabel("Cook's Distance")
# plt.show()

# --- 4. Box Plot ---
df2=pd.DataFrame({
    "values":[10,11,12,12,13,15,25,37,40, 90,100]
})
plt.boxplot(df2['values'])
plt.show()