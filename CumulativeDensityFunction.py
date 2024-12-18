# Probability and Statistics
# Find Normal Cumulative Density Function (Normal CD or CDF)
# Use numerical integration
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

# Parameters for normal distribution
mu = 0  # E(X) = mu
sigma = 1  # sigma = SD(X)
x = float(input("Enter x: "))
lower = -10  # Very small number leads to inaccurate result
upper = x
f = lambda y: (1 / (sqrt(2 * pi))) * np.exp(-y ** 2 / 2)
val = np.linspace(upper, lower, 1000)
I_trapezoids = np.trapz(f(val), val)
res = abs(I_trapezoids)
print(f"CDF value at x = {x} is {res}")

# Plotting the bell curve (PDF)
x_values = np.linspace(-5, 5, 1000)
pdf_values = f(x_values)

plt.figure(figsize=(8, 5))
plt.plot(x_values, pdf_values, label="Normal Distribution PDF")
plt.fill_between(x_values, 0, pdf_values,
                 where=(x_values <= x), color="skyblue", alpha=0.4, label=f"CDF at x={x: .2f}")
plt.axvline(x, color='r', linestyle='--', label=f"x = {x}")
plt.title("Standard Normal Distribution")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
