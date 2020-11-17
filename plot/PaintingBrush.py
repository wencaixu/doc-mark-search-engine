import numpy as np
import matplotlib.pyplot as plt

# 必须指定
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

data = np.arange(0, 1, 0.01)

plt.figure()

plt.title("函数模拟")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim((0, 1))
plt.ylim((0, 1))
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.plot(data, data ** 2)
plt.plot(data, data ** 4)
plt.legend(['y=x^2', 'y=x^4'])
plt.show()
