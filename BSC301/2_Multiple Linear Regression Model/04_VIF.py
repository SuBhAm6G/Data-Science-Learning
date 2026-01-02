import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools import add_constant

# --- 1. Create Data with High Multicollinearity ---
# X1 and X2 are highly correlated
data = {
    'X1': [1, 2, 3, 4, 5],
    'X2': [2, 4, 6, 8, 10],       # X2 is exactly 2 * X1 (Perfect correlation)
    'X3': [5, 1, 3, 7, 2]         # X3 is random
}
df = pd.DataFrame(data)

# --- 2. Prepare Data ---
# Must add constant for VIF calculation to work correctly for intercepts
X=add_constant(df)

# --- 3. Calculate VIF ---
# We loop through each feature index

vif_data=pd.DataFrame()
vif_data['Feature']=X.columns
print(vif_data)
vif_data['VIF']=[variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
print(vif_data)
