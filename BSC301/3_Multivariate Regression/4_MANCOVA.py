import pandas as pd
from statsmodels.multivariate.manova import MANOVA

# --- 1. Data Setup ---
df = pd.DataFrame({
    'Method': ['Online', 'Online', 'Online', 'Offline', 'Offline', 'Offline'],
    'IQ':     [110, 112, 108, 95, 98, 100],      # Covariate (Online is smarter)
    'Math':   [85, 88, 84, 75, 78, 76],          # Outcome 1
    'Phys':   [80, 82, 79, 70, 72, 71]           # Outcome 2
})

# --- 2. Run MANCOVA ---
# Formula: "Y1 + Y2 ~ Group + Covariate"
mancova = MANOVA.from_formula('Math + Phys ~ Method + IQ', data=df)

# --- 3. Results ---
print(mancova.mv_test())

# Output Explanation:
# You will see tests for "Method" (Group effect) AND "IQ" (Covariate effect).
# If "Method" is significant AFTER including IQ, then Online implies real learning gains.