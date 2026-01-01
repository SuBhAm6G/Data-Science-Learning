from sklearn.linear_model import LinearRegression
import numpy as np
# --- 1. The Data ---
X_raw = np.array([
    [1, 60],
    [2, 70],
    [3, 75],
    [4, 80],
    [5, 85]
]) #5 samples, 2 features
Y = np.array([40, 50, 55, 62, 68])

# --- 2. Model Initialization ---
model=LinearRegression(fit_intercept=True)
# --- 3. Training (Fitting) ---
model.fit(X_raw,Y)
# --- 4. Results ---
print(f"Intercept (Beta_0): {model.intercept_:.2f}")
print(f"Coefficients (Beta_1, Beta_2): {model.coef_}")
print('-'*65)
print(f"The Equation of regression is Y = {model.intercept_:.2f} + {model.coef_[0]:.2f}*X1 + {model.coef_[1]:.2f}*X2")
print('-'*65)

# --- 5. Prediction ---
new_student=np.array([[6,90]])
prediction = model.predict(new_student)
print(f"Predicted Score: {prediction[0]:.2f}")