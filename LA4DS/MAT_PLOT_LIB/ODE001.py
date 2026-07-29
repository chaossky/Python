import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, y):
    return -y

y0 = [0.5]   # 초기 조건 y(0) = 1
t_span = (0, 4)
t_eval = np.linspace(0, 4, 400)

sol = solve_ivp(f, t_span, y0, t_eval=t_eval)

plt.plot(sol.t, sol.y[0], label="y(t)")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()
