import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

df = pd.read_csv('res/SOCLNresults.csv')

numRows = 20+1
numCols = 2*20+1
h1 = df["h1"].to_numpy().reshape(numRows,numCols)
h3 = df["h3"].to_numpy().reshape(numRows,numCols)
G0 = df["lambda_0"].to_numpy().reshape(numRows,numCols)
L1 = df["lambda_1"].to_numpy().reshape(numRows,numCols)
G2 = df["lambda_2"].to_numpy().reshape(numRows,numCols)
L3 = df["lambda_3"].to_numpy().reshape(numRows,numCols)
G4 = df["lambda_4"].to_numpy().reshape(numRows,numCols)
L5 = df["lambda_5"].to_numpy().reshape(numRows,numCols)
G6 = df["lambda_6"].to_numpy().reshape(numRows,numCols)
L7 = df["lambda_7"].to_numpy().reshape(numRows,numCols)
G8 = df["lambda_8"].to_numpy().reshape(numRows,numCols)

# Contour Plot
fig, ax = plt.subplots()
ax.set(xlabel='h1 (A)',ylabel='h3 (A)',title="L1") #,xscale='log',yscale='log'
pos = ax.contourf(h1, h3, L1, 20, cmap='RdGy')
fig.colorbar(pos,ax=ax)
# plt.savefig("res/L1.png")
plt.show()

# # Triangular Plot
# x = df["h1"].to_numpy()
# y = df["h3"].to_numpy()
# z = df["lambda_1"].to_numpy()
# ax = plt.figure().add_subplot(projection='3d')
# ax.set(xlabel='h1 (A)',ylabel='h3 (A)',title="L1")
# ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True, cmap='RdGy')
# plt.show()

# Interpolation
intpL1 = interpolate.interp2d(h1,h3,L1)
h1Fine = np.linspace(h1.min(),h1.max(),201)
h3Fine = np.linspace(h3.min(),h3.max(),401)
H1Fine,H3Fine = np.meshgrid(h1Fine,h3Fine)
L1Fine = intpL1(h1Fine,h3Fine)

fig, ax = plt.subplots()
ax.set(xlabel='h1 (A)',ylabel='h3 (A)',title="L1 interpolated") #,xscale='log',yscale='log'
pos = ax.contourf(H1Fine, H3Fine, L1Fine, 20, cmap='RdGy')
fig.colorbar(pos,ax=ax)
# plt.savefig("res/L1.png")
plt.show()

