import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 7, 10])
ypoints = np.array([0, 250, 70])

# plt.plot(xpoints, ypoints, marker="o", linestyle="dotted", c="r")
# plt.show()
dataPie = np.array([100, 80, 85, 50])
matkul = ["mtk", "alpro", "agama", "inggris"]

plt.pie(dataPie, labels=matkul, autopct="%1.0f%%")
plt.show()
