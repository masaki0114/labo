import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# seabornがあると、グラフがきれいにかける
import seaborn as sns
sns.set_style("darkgrid")

from mpl_toolkits.mplot3d import Axes3D

file = 'sample.csv'
usecols = [1,133]
skiprows = [0,1,2,3,4,5]
names = ["Time","Between-the-hand"]
df = pd.read_csv(file,usecols=usecols,skiprows=skiprows,names=names,header=None)
# print(df)
print(df["Between-the-hand"])
# print(df.query("Time <= 10"))

# これより下で３次元プロットを試す。
# Top.head_Xだけ抽出する
limit_time = 20
X = df.query("Time <= %i"%limit_time)[names[0]]
Y = df.query("Time <= %i"%limit_time)[names[1]]
# Z = df.query("Time <= %i"%limit_time)["Top.head_Z"]
# print(len(X))
# fig = plt.figure()
plt.figure()
# ax = Axes3D(fig)
l=0
t = len(X)-1
b=0
a=0
s=t-b
while(l<=t):
  while(a<=s):
    plt.plot(X[l:t+1],Y[l:t+1],
    c=((a/s)*1.0,0.0,((s-a)/s)*1.0),lw=0.5)
    l=l+1
    a=a+1
plt.xlabel(names[0])
plt.ylabel(names[1])
# ax.set_zlabel("Top.head_Z")
plt.show()