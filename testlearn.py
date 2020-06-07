import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
import scipy.stats as stats



file = open("registro_de_ejercicios.txt")
lines = file.readlines()
processedList = []
for i, line in enumerate(lines):
    try:
        line = line.split(",")
        temp = [line[0],line[1],line[2],line[3],line[4],line[5],line[6]]
        processedList.append(temp)
    except:
        print("Error en la línea: ", i)
columns = ["ejercicio","tiempo","x1","y1","z1","x2","y2"]

data = pd.DataFrame(data = processedList,columns = columns)
print(data.head())

print(data.shape)

print(data.isnull().sum())
print(data["ejercicio"].value_counts())
data["tiempo"] = data["tiempo"].astype("float")
data["x1"] = data["x1"].astype("float")
data["y1"] = data["y1"].astype("float")
data["z1"] = data["z1"].astype("float")
data["x2"] = data["x2"].astype("float")
data["y2"] = data["y2"].astype("float")
print(data.info())
Fs = 10
ejercicios = data["ejercicio"].value_counts().index
print(ejercicios)
def plot_ejercicio(ejercicio,data):
    fig, (ax0,ax1,ax2,ax3,ax4) = plt.subplots(nrows=5, figsize =(15,7), sharex = True)
    plot_axis(ax0, data["tiempo"],data["x1"], " Eje X1")
    plot_axis(ax1, data["tiempo"],data["y1"], " Eje Y1")    
    plot_axis(ax2, data["tiempo"],data["z1"], " Eje Z1")
    plot_axis(ax3, data["tiempo"],data["x2"], " Eje X2")
    plot_axis(ax4, data["tiempo"],data["y2"], " Eje Y2")
    plt.subplots_adjust(hspace = 0.2)
    fig.suptitle(ejercicio)
    plt.subplots_adjust(top = 0.9)
    plt.show()

def plot_axis(ax,x,y,title):
    ax.plot(x,y,'g')
    ax.set_title(title)
    ax.xaxis.set_visible(False)
    ax.set_ylim([min(y) - np.std(y),max(y)+np.std(y)])
    ax.set_xlim([min(x),max(x)])
    ax.grid(True)     
"""
for ejercicio in ejercicios:
    data_for_plot = data[(data["ejercicio"] == ejercicio)][:Fs*10]
    plot_ejercicio(ejercicio,data_for_plot)    
"""
df = data.drop(["tiempo"],axis = 1).copy()
print(df.head())

print(df ["ejercicio"].value_counts())

etiqueta = LabelEncoder()
df ["etiqueta"] = etiqueta.fit_transform(df["ejercicio"])

etiqueta.classes
