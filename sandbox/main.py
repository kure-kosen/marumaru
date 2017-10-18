import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = 'sample.csv'

df = pd.read_csv(file_name)

deg = df['Phi [deg]']
values = df.iloc[:, 1:]

lines = ['-', '--', '-.', ':', '.', ',']

ax = plt.subplot(111, projection='polar')

ax.axes.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rlabel_position(0)

theta = deg*np.pi/180
r = values

for i in range(len(values.columns)):
    label = values.columns[i]
    line = lines[i%len(lines)]
    ax.plot(theta, values.iloc[:, i], line, label=label)

plt.legend(bbox_to_anchor=(1.05, 1))
plt.savefig('sample.png', dpi=500)
plt.show()
