#[image3.png]
import numpy as np

# --- 1. Define the Covariance Matrix ---
# We use the matrix from the previous "Tougher Example"
# Variables: [Y, X1, X2]
sigma = np.array([
    [10,  2,  1],  # Row 0: Y (Target)
    [ 2,  5, -1],  # Row 1: X1
    [ 1, -1,  2]   # Row 2: X2
])

# --- 2. Matrix Partitioning ---
sigma_yx=sigma[0,1:]
sigma_xx=sigma[1:,1:]
sigma_xx_inv=np.linalg.inv(sigma_xx)
print("Sigma_yx:\n", sigma_yx)
print("Sigma_xx:\n", sigma_xx)
print("Sigma_xx Inverse:\n", sigma_xx_inv)

# --- 3. Calculate Coefficients ---
Beta=np.matmul(sigma_yx, sigma_xx_inv)
print(f"Regression Coefficients (Beta): {Beta}")
print(f"\u03B2 \u2081 :{Beta[0]:.3f}\n\u03B2 \u2082 :{Beta[1]:.3f}")