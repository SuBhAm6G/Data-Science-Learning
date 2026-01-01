# Demonstrating the difference between MLE (biased) and Unbiased covariance.
import numpy as np

# Sample Data (3 points, 2 dimensions)
X = np.array([[2, 4], 
              [4, 2], 
              [6, 6]])

# --- 1. MLE for Mean ---
mean_vector = np.mean(X, axis=0)
print(f"MLE Mean Vector: {mean_vector}")

# --- 2. MLE for Covariance (Biased, divides by n) ---
# numpy.cov defaults to unbiased (n-1). To get MLE, set bias=True or ddof=0
cov_mle = np.cov(X, rowvar=False, ddof=0)
print(f"\nMLE Covariance (Divides by n=3):\n{cov_mle}")

# --- 3. Unbiased Covariance (Divides by n-1) ---
cov_unbiased = np.cov(X, rowvar=False, ddof=1)
print(f"\nUnbiased Covariance (Divides by n-1=2):\n{cov_unbiased}")

# Notice the Unbiased values are larger (more conservative).