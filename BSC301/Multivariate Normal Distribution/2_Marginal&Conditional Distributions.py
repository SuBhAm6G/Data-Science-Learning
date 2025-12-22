import numpy as np
# Define Mean and Covariance
mu=np.array([170,60])
sigma=np.array([[100,50],[50,100]])

# We want distribution of X1 (index 0) given X2 (index 1) = 70
x2=70
mu1=mu[0]
mu2=mu[1]
sigma11=sigma[0,0]
sigma22=sigma[1,1]
sigma12=sigma[0,1]

# 2. Calculate Conditional Mean
# formula: mu1 + sigma12 * inv(sigma22) * (x2 - mu2)
cond_mean=mu1 + (sigma12 * (1/(sigma22)) * (x2-mu2))

# 3. Calculate Conditional Variance
# formula: sigma11 - sigma12 * inv(sigma22) * sigma21
cond_var=sigma11 - (sigma12 * (1/(sigma22)) * sigma12)

print(f"Given Weight={x2}, Expected Height={cond_mean}")
print(f"New Uncertainty (Variance)={cond_var}")
