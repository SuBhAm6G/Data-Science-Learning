# This code demonstrates how to define a distribution, calculate the density for a specific point (useful for checking "likelihood"), and visualize it.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
# Let's say X = [Math Score, Physics Score]
mean_vector=np.array([50,60])
print(f"Mean Vector:\n{mean_vector}")
# Covariance Matrix
# Variance of Math=100, Physics=100, Covariance=50 (Positive correlation)
cov_mat=np.array([[100,50],[50,100]])
print(f"Covariance Matrix:\n{cov_mat}")

# --- 1. DEFINE THE MULTIVARIATE NORMAL DISTRIBUTION ---
# Create the random variable object
mvn=multivariate_normal(mean=mean_vector, cov=cov_mat)

# --- 2. CALCULATE PROBABILITY DENSITY ---
# Let's check the density for a student with scores [55, 65]
student_marks=np.array([50,60])
pdf=mvn.pdf(student_marks)
print(f"The probability density for marks {student_marks} is: {pdf:.6f}")

# --- 3. VISUALIZATION (Bivariate Normal) ---
# Create a grid of points (X and Y coordinates)
x, y = np.mgrid[20:80:.5, 30:90:.5] 
pos = np.dstack((x, y))

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
# This shows the "Mountain" shape mentioned in the intuition section
ax.plot_surface(x, y, mvn.pdf(pos), cmap='viridis', linewidth=0.2)

ax.set_xlabel('Math Score')
ax.set_ylabel('Physics Score')
ax.set_zlabel('Probability Density')
plt.title('Bivariate Normal Distribution')
plt.show()