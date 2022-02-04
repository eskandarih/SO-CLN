import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

df = pd.read_csv('SOCLNresults.csv')

numRows = np.sqrt(len(df))
numRows = numRows.astype(int)
h1 = df["h1"].to_numpy().reshape(numRows,numRows)
h3 = df["h3"].to_numpy().reshape(numRows,numRows)
G0 = df["lambda_0"].to_numpy().reshape(numRows,numRows)
L1 = df["lambda_1"].to_numpy().reshape(numRows,numRows)
G2 = df["lambda_2"].to_numpy().reshape(numRows,numRows)
L3 = df["lambda_3"].to_numpy().reshape(numRows,numRows)
G4 = df["lambda_4"].to_numpy().reshape(numRows,numRows)
L5 = df["lambda_5"].to_numpy().reshape(numRows,numRows)
G6 = df["lambda_6"].to_numpy().reshape(numRows,numRows)
L7 = df["lambda_7"].to_numpy().reshape(numRows,numRows)
G8 = df["lambda_8"].to_numpy().reshape(numRows,numRows)


fig, ax = plt.subplots()
ax.set(xlabel='h1 (A)',ylabel='h3 (A)',title="L1") #,xscale='log',yscale='log'
pos = ax.contourf(h1, h3, L1, 20, cmap='RdGy')
fig.colorbar(pos,ax=ax)
plt.savefig("res/L1.png")
# plt.show()


fig3d, ax3d = plt.subplots(subplot_kw={"projection": "3d"})
pos3d = ax3d.plot_surface(h3,h3,L1, cmap='RdGy')
# pos3d = ax3d.scatter(h1,h3,L1, cmap='RdGy')
plt.show()