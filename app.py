import numpy as np
import matplotlib.pyplot as plt

population = 1000

steps = 10000
delta_t = 0.01

i0 = 1 / population
s0 = population / population

gama = 1 / 10  # 1 / numero de dias de infecção
beta = 0.3  # propabilidade de infecção no tempo


def Euler(steps, delta_t):
    s_arr = [s0]
    i_arr = [i0]
    t_arr = [0]

    s = s0
    i = i0

    for k in range(1, steps - 1):
        new_s = s - beta * s * i * delta_t
        new_i = i + beta * s * i * delta_t - gama * i * delta_t

        s_arr.append(new_s)
        i_arr.append(new_i)
        t_arr.append(k*delta_t)

        s = new_s
        i = new_i

    return {"s": s_arr, "i": i_arr, "t": t_arr}


euler = Euler(steps, delta_t)

plt.plot(euler["t"], euler["i"])
plt.plot(euler["t"], euler["s"])

plt.show()
