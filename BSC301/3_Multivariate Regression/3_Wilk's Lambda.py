import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# --- 1. Data Setup ---
# Group: A (Control) vs B (Test)
# Y1: Speed, Y2: Accuracy
df = pd.DataFrame({
    'Group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'Speed': [10, 12, 11, 20, 22, 21],    # Group B is faster
    'Accuracy': [90, 88, 89, 85, 84, 86]  # Group B is less accurate
})

# --- 2. Run MANOVA ---
# Formula: "Dependent_Vars ~ Independent_Var"
ma = MANOVA.from_formula('Speed + Accuracy ~ Group', data=df)

# --- 3. Print Results ---
print(ma.mv_test())

# Output Explanation:
# Look for the section "Group".
# Look for "Wilks' lambda".
# Check the "Pr > F" (P-value). If < 0.05, Groups are different.